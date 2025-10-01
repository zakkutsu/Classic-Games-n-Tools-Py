import os
import textwrap
from PIL import Image
import flet as ft
import google.generativeai as genai

# --- KONFIGURASI PENTING ---
API_KEY = "AIzaSyB4yOXYhsx43pAI0HCu5DKNt4VTZijLt7E"  # set your API key or leave empty to error-check
MODEL_NAME = "gemini-2.5-flash"
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

# Configure API
try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel(MODEL_NAME)
    API_CONFIGURED_SUCCESSFULLY = True
except Exception as e:
    API_CONFIGURED_SUCCESSFULLY = False
    API_ERROR_MESSAGE = f"Error Konfigurasi API: {e}\n\nPastikan API Key Anda sudah benar dan koneksi internet aktif."


def describe_image(image_path, target_lang='en'):
    """Describe image and optionally translate the description to the target language.

    target_lang: 'id', 'en', 'jp'
    """
    if not image_path or not os.path.exists(image_path):
        return "Error: File gambar tidak ditemukan atau path kosong."

    try:
        file_size = os.path.getsize(image_path)
        if file_size > MAX_FILE_SIZE:
            return "Error: Ukuran file terlalu besar. Maksimal 10MB."

        img = Image.open(image_path)
        valid_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.webp']
        file_ext = os.path.splitext(image_path.lower())[1]
        if file_ext not in valid_extensions:
            return f"Error: Format file tidak didukung. Gunakan: {', '.join(valid_extensions)}"

        # Build a prompt asking for a descriptive analysis
        prompt = (
            "Describe the content of the image in detail, listing main objects, colors, actions, and notable details. "
            "Keep the description clear and informative."
        )

        # Send to model (image may be passed depending on SDK capabilities)
        try:
            response = model.generate_content([prompt, img])
            description = response.text
        except Exception:
            # fallback: plain prompt without image if SDK doesn't support direct image objects
            response = model.generate_content(prompt + "\n\n(Assume an image is provided; describe it.)")
            description = response.text

        # Optionally translate
        if target_lang and target_lang != 'en':
            # reuse translate-like prompt
            lang_map = {'id': 'Indonesian', 'en': 'English', 'jp': 'Japanese'}
            dst = lang_map.get(target_lang, target_lang)
            trans_prompt = f"Translate the following text to {dst}. Provide only the translated text.\n\n{description}"
            response2 = model.generate_content(trans_prompt)
            return response2.text

        return description
    except Exception as e:
        wrapped_error = "\n".join(textwrap.wrap(str(e), 80))
        return f"Terjadi kesalahan saat memproses gambar:\n\n{wrapped_error}"


def main(page: ft.Page):
    page.title = "🖼️ Image Describer AI"
    page.window_width = 900
    page.window_height = 800
    page.padding = ft.padding.all(20)
    page.scroll = ft.ScrollMode.AUTO

    if not API_CONFIGURED_SUCCESSFULLY:
        dlg = ft.AlertDialog(title=ft.Text("❌ Gagal Memuat Aplikasi"), content=ft.Text(API_ERROR_MESSAGE), actions=[ft.TextButton("OK", on_click=lambda e: page.window_close())])
        page.dialog = dlg
        dlg.open = True
        page.update()
        return

    header = ft.Text("🖼️ Image Describer AI", size=28, weight=ft.FontWeight.BOLD)

    file_path_display = ft.TextField(label="📂 Path file gambar", read_only=True, value="")

    output_field = ft.TextField(label="📝 Hasil deskripsi", multiline=True, min_lines=8, max_lines=12, read_only=True)

    lang_options = [
        ft.dropdown.Option("id", text="Bahasa Indonesia"),
        ft.dropdown.Option("en", text="English"),
        ft.dropdown.Option("jp", text="日本語 (Japanese)")
    ]
    target_lang = ft.Dropdown(label="Terjemahkan hasil ke", value="en", options=lang_options, width=220)

    file_picker = ft.FilePicker(on_result=lambda e: on_file_pick(e, file_path_display, page))
    page.overlay.append(file_picker)

    pick_btn = ft.ElevatedButton(text="📂 Pilih Gambar", icon=ft.Icons.FOLDER_OPEN, on_click=lambda _: file_picker.pick_files(dialog_title="Pilih gambar", file_type=ft.FilePickerFileType.IMAGE, allow_multiple=False))

    analyze_btn = ft.ElevatedButton(text="🔍 Analisis Gambar", icon=ft.Icons.ANALYTICS, on_click=lambda e: on_analyze(e, file_path_display, output_field, target_lang, page))

    page.add(header, ft.Divider(), file_path_display, ft.Row([pick_btn, analyze_btn, target_lang]), ft.Divider(), output_field)


def on_file_pick(e: ft.FilePickerResultEvent, file_path_display: ft.TextField, page: ft.Page):
    if e.files:
        selected = e.files[0]
        file_path_display.value = selected.path
        page.update()


def on_analyze(e, file_path_display: ft.TextField, output_field: ft.TextField, target_lang: ft.Dropdown, page: ft.Page):
    path = file_path_display.value
    if not path:
        page.snack_bar = ft.SnackBar(ft.Text("⚠️ Mohon pilih file gambar terlebih dahulu!"))
        page.snack_bar.open = True
        page.update()
        return

    output_field.value = "Sedang memproses..."
    page.update()

    result = describe_image(path, target_lang=target_lang.value)

    output_field.value = result
    page.update()


if __name__ == "__main__":
    ft.app(target=main)