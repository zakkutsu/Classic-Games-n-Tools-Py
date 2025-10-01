import flet as ft
import google.generativeai as genai
import textwrap

# --- KONFIGURASI PENTING ---
API_KEY = "AIzaSyDbB8HqNcMPgNv2Jgg8jGCLpKRzJa4e3rs"  # API Key Gemini
MAX_CHARS = 100000
MODEL_NAME = "gemini-2.5-flash"

# Konfigurasi model AI Google
try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(MODEL_NAME)
    API_CONFIGURED_SUCCESSFULLY = True
except Exception as e:
    API_CONFIGURED_SUCCESSFULLY = False
    API_ERROR_MESSAGE = f"Error Konfigurasi API: {e}\n\nPastikan API Key Anda sudah benar dan koneksi internet aktif."

def translate_text(text_to_translate, source_lang: str = "auto", target_lang: str = "id"):
    """Translate text between supported languages.

    source_lang/target_lang: 'id' (Indonesian), 'en' (English), 'jp' (Japanese), or 'auto' for automatic detection (only for source_lang).
    Returns translated text or an error message string.
    """
    if not text_to_translate or not text_to_translate.strip():
        return "Error: Tidak ada teks untuk diterjemahkan."

    if len(text_to_translate) > MAX_CHARS:
        return f"Error: Teks melebihi batas maksimal {MAX_CHARS} karakter."

    lang_names = {
        "id": "Indonesian",
        "en": "English",
        "jp": "Japanese",
        "auto": "the original language (detect automatically)"
    }

    if source_lang == target_lang:
        # Nothing to do
        return text_to_translate

    src_name = lang_names.get(source_lang, source_lang)
    tgt_name = lang_names.get(target_lang, target_lang)

    try:
        if source_lang == "auto":
            prompt = f"""
            Detect the language of the following text and translate it into {tgt_name}.
            Provide only the translated text as the result, without any additional comments, explanations, or introductions.

            --- TEXT TO TRANSLATE ---
            {text_to_translate}
            --- END OF TEXT ---
            """
        else:
            prompt = f"""
            Translate the following text from {src_name} to {tgt_name}.
            Provide only the translated text as the result, without any additional comments, explanations, or introductions.

            --- TEXT TO TRANSLATE ---
            {text_to_translate}
            --- END OF TEXT ---
            """

        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        error_message = str(e)
        wrapped_error = "\n".join(textwrap.wrap(error_message, 80))
        return f"Terjadi kesalahan saat menghubungi API:\n\n{wrapped_error}"

def main(page: ft.Page):
    # Konfigurasi halaman
    page.title = "🤖 Text Translator AI - Modern Edition"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 700
    page.window_height = 850
    page.padding = ft.padding.all(20)
    page.scroll = ft.ScrollMode.AUTO
    
    # Error dialog jika API key salah
    if not API_CONFIGURED_SUCCESSFULLY:
        error_dialog = ft.AlertDialog(
            title=ft.Text("❌ Gagal Memuat Aplikasi"),
            content=ft.Text(API_ERROR_MESSAGE),
            actions=[ft.TextButton("OK", on_click=lambda e: page.window_close())]
        )
        page.dialog = error_dialog
        error_dialog.open = True
        page.update()
        return
    
    # Header
    header = ft.Text("🤖 Text Translator AI", size=28, weight=ft.FontWeight.BOLD)
    
    # Input field
    input_field = ft.TextField(
        label="✍️ Masukkan teks yang ingin diterjemahkan...",
        multiline=True,
        min_lines=6,
        max_lines=10,
        border_color=ft.Colors.BLUE_400,
        text_size=14,
        helper_text="Mendukung bahasa: id, en, jp (pilih sumber & target)"
    )
    
    # Character counter
    input_char_count = ft.Text(f"0 / {MAX_CHARS:,} karakter", size=12)
    
    # Progress indicator
    progress_ring = ft.Row([
        ft.ProgressRing(width=16, height=16, stroke_width=2),
        ft.Text("Sedang menerjemahkan...", size=12, color=ft.Colors.BLUE_400)
    ], visible=False)
    
    # Translate button
    translate_button = ft.ElevatedButton(
        text="🚀 Terjemahkan",
        icon=ft.Icons.TRANSLATE,
        width=200,
        height=45,
        style=ft.ButtonStyle(
            color=ft.Colors.WHITE,
            bgcolor=ft.Colors.BLUE_600
        )
    )
    
    # Output field
    output_field = ft.TextField(
        label="📖 Hasil terjemahan",
        multiline=True,
        min_lines=6,
        max_lines=10,
        read_only=True,
        border_color=ft.Colors.GREEN_400,
        text_size=14,
        helper_text="Hasil akan muncul di sini"
    )
    
    # Output info
    output_char_count = ft.Text("Jumlah karakter hasil: 0", size=12, color=ft.Colors.GREEN_400)
    
    # Clear button
    clear_button = ft.OutlinedButton(
        text="🗑️ Bersihkan",
        icon=ft.Icons.CLEAR_ALL,
        width=150,
        height=35
    )
    
    def update_input_count(e):
        """Update character count."""
        char_count = len(input_field.value or "")
        input_char_count.value = f"{char_count:,} / {MAX_CHARS:,} karakter"
        
        if char_count > MAX_CHARS:
            input_char_count.color = ft.Colors.RED_400
            translate_button.disabled = True
        else:
            input_char_count.color = ft.Colors.GREY_400
            translate_button.disabled = False
        page.update()
    
    def start_translation(e):
        """Start translation process."""
        source_text = input_field.value
        source_lang = source_lang_dropdown.value or "auto"
        target_lang = target_lang_dropdown.value or "id"
        
        if not source_text or not source_text.strip():
            page.snack_bar = ft.SnackBar(ft.Text("⚠️ Teks input tidak boleh kosong!"))
            page.snack_bar.open = True
            page.update()
            return
        
        # Show loading
        progress_ring.visible = True
        translate_button.disabled = True
        output_field.value = ""
        page.update()
        # Translate
        translation_result = translate_text(source_text, source_lang=source_lang, target_lang=target_lang)

        # Hide loading
        progress_ring.visible = False
        translate_button.disabled = False

        # Show result
        output_field.value = translation_result
        result_length = len(translation_result)

        if translation_result.startswith("Error:") or translation_result.startswith("Terjadi"):
            output_char_count.color = ft.Colors.RED_400
            output_char_count.value = "❌ Terjadi kesalahan"
        else:
            output_char_count.color = ft.Colors.GREEN_400
            output_char_count.value = f"Jumlah karakter hasil: {result_length:,}"

        page.update()
        return
    
    def clear_all(e):
        """Clear all fields."""
        input_field.value = ""
        output_field.value = ""
        input_char_count.value = f"0 / {MAX_CHARS:,} karakter"
        input_char_count.color = ft.Colors.GREY_400
        output_char_count.value = "Jumlah karakter hasil: 0"
        output_char_count.color = ft.Colors.GREEN_400
        translate_button.disabled = False
        page.update()
    
    # Connect events
    input_field.on_change = update_input_count
    translate_button.on_click = start_translation
    clear_button.on_click = clear_all

    # Language selection dropdowns
    lang_options = [
        ft.dropdown.Option("auto", text="Auto Detect"),
        ft.dropdown.Option("id", text="Indonesian (id)"),
        ft.dropdown.Option("en", text="English (en)"),
        ft.dropdown.Option("jp", text="Japanese (jp)")
    ]

    source_lang_dropdown = ft.Dropdown(
        label="Dari (source)",
        width=220,
        options=lang_options,
        value="auto",
        helper_text="Pilih bahasa sumber atau Auto Detect"
    )

    target_lang_dropdown = ft.Dropdown(
        label="Ke (target)",
        width=220,
        options=[opt for opt in lang_options if opt.key != "auto"],
        value="id",
        helper_text="Pilih bahasa target"
    )
    
    # Add components to page
    page.add(
        header,
        ft.Divider(),
        ft.Row([source_lang_dropdown, ft.Container(width=20), target_lang_dropdown]),
        ft.Divider(),
        input_field,
        input_char_count,
        ft.Row([translate_button, progress_ring], alignment=ft.MainAxisAlignment.CENTER),
        ft.Divider(),
        output_field,
        output_char_count,
        clear_button
    )

if __name__ == "__main__":
    ft.app(target=main)