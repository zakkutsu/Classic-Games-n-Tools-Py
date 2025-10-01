import flet as ftimport google.generativeai as genai

import google.generativeai as genaifrom PIL import Image

from PIL import Imageimport PySimpleGUI as sg

import osimport os

import textwrap

# --- KONFIGURASI PENTING ---

# --- KONFIGURASI PENTING ---# Ganti tulisan "YOUR_API_KEY_HERE" dengan kunci API yang sudah Anda salin.

# GANTI DENGAN API KEY ANDA YANG VALIDAPI_KEY = "AIzaSyB4yOXYhsx43pAI0HCu5DKNt4VTZijLt7E" # GANTI DENGAN KUNCI API BARU ANDA

API_KEY = "API_KEY_GEMINI_ANDA"  # <-- PERHATIKAN! Ganti bagian ini.

# Konfigurasi model AI Google

# Konfigurasi model AI Googletry:

try:    genai.configure(api_key=API_KEY)

    genai.configure(api_key=API_KEY)    model = genai.GenerativeModel('gemini-2.5-flash')

    model = genai.GenerativeModel('gemini-2.5-flash')except Exception as e:

    API_CONFIGURED_SUCCESSFULLY = True    sg.popup_error(f"Error Konfigurasi API: {e}\n\nPastikan API Key Anda sudah benar dan koneksi internet aktif.")

except Exception as e:    exit()

    API_CONFIGURED_SUCCESSFULLY = False

    API_ERROR_MESSAGE = f"Error Konfigurasi API: {e}\n\nPastikan API Key Anda sudah benar dan koneksi internet aktif."# --- FUNGSI UTAMA ---

def describe_image(image_path):

# --- FUNGSI UTAMA (Backend) ---    """Mengirim gambar ke AI dan mendapatkan deskripsi."""

def describe_image(image_path):    if not os.path.exists(image_path):

    """Mengirim gambar ke AI dan mendapatkan deskripsi dalam Bahasa Indonesia."""        return "Error: File gambar tidak ditemukan."

    if not image_path or not os.path.exists(image_path):    

        return "Error: File gambar tidak ditemukan atau path kosong."    try:

            img = Image.open(image_path)

    try:        

        # Validasi format file        prompt = "Jelaskan apa yang ada di dalam gambar ini dalam Bahasa Indonesia yang singkat dan jelas."

        valid_extensions = ['.png', '.jpg', '.jpeg', '.gif', '.webp']        

        file_ext = os.path.splitext(image_path.lower())[1]        # Kirim gambar dan prompt ke model AI

        if file_ext not in valid_extensions:        response = model.generate_content([prompt, img])

            return f"Error: Format file tidak didukung. Gunakan: {', '.join(valid_extensions)}"        

                return response.text

        # Buka dan validasi gambar    except Exception as e:

        img = Image.open(image_path)        return f"Terjadi kesalahan saat memproses gambar: {e}"

        

        # Validasi ukuran file (maksimal 10MB)# --- TAMPILAN APLIKASI (GUI) ---

        file_size = os.path.getsize(image_path)# Perhatikan semua baris di bawah ini sekarang rata kiri (tanpa spasi di awal)

        if file_size > 10 * 1024 * 1024:  # 10MBsg.theme('DarkBlue3')

            return "Error: Ukuran file terlalu besar. Maksimal 10MB."

        layout = [

        prompt = """    [sg.Text("Pilih Gambar untuk Dideskripsikan", font=('Helvetica', 16))],

        Jelaskan apa yang ada di dalam gambar ini dalam Bahasa Indonesia yang detail dan informatif.    [sg.Input(key='-FILE_PATH-'), sg.FileBrowse("Cari Gambar", file_types=(("Image Files", "*.png *.jpg *.jpeg"),))],

        Berikan deskripsi yang mencakup:    [sg.Button("Mulai Deskripsikan", key='-SUBMIT-'), sg.Button("Keluar")],

        1. Objek utama yang terlihat    [sg.Text("Hasil Deskripsi:", font=('Helvetica', 12))],

        2. Warna dan komposisi    [sg.Multiline(size=(60, 10), key='-OUTPUT-', disabled=True, font=('Arial', 11))]

        3. Aktivitas atau situasi yang terjadi]

        4. Detail menarik lainnya

        window = sg.Window('Image Describer AI', layout)

        Berikan jawaban dalam format yang mudah dibaca dan informatif.

        """# --- LOOP UTAMA APLIKASI ---

        while True:

        # Kirim gambar dan prompt ke model AI    event, values = window.read()

        response = model.generate_content([prompt, img])    

        return response.text    if event == sg.WIN_CLOSED or event == "Keluar":

                break

    except Exception as e:    

        error_message = str(e)    if event == '-SUBMIT-':

        wrapped_error = "\n".join(textwrap.wrap(error_message, 80))        image_path = values['-FILE_PATH-']

        return f"Terjadi kesalahan saat memproses gambar:\n\n{wrapped_error}"        if image_path:

            # Tampilkan status "memproses"

# --- FUNGSI UTAMA APLIKASI FLET ---            window['-OUTPUT-'].update("Sedang memproses, mohon tunggu...")

def main(page: ft.Page):            window.refresh() # Paksa jendela untuk update tampilan

    # Konfigurasi halaman            

    page.title = "🖼️ Image Describer AI - Modern Edition"            # Panggil fungsi deskripsi dan tampilkan hasilnya

    page.vertical_alignment = ft.MainAxisAlignment.START            description = describe_image(image_path)

    page.theme_mode = ft.ThemeMode.DARK            window['-OUTPUT-'].update(description)

    page.window_width = 750        else:

    page.window_height = 900            sg.popup("Mohon pilih file gambar terlebih dahulu!")

    page.padding = ft.padding.all(20)

    page.scroll = ft.ScrollMode.AUTOwindow.close()

    # Fungsi untuk menampilkan dialog error jika API key salah di awal
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

    # --- KONTROL-KONTROL (WIDGETS) ---
    
    # Header dengan info
    header = ft.Container(
        content=ft.Column([
            ft.Text("🖼️ Image Describer AI", 
                   size=28, 
                   weight=ft.FontWeight.BOLD,
                   text_align=ft.TextAlign.CENTER),
            ft.Text("Powered by Google Gemini Vision AI", 
                   size=14, 
                   color=ft.colors.GREY_400,
                   text_align=ft.TextAlign.CENTER),
            ft.Divider(height=20)
        ]),
        margin=ft.margin.only(bottom=20)
    )

    # File path display
    file_path_display = ft.TextField(
        label="📂 Path file gambar",
        read_only=True,
        border_color=ft.colors.PURPLE_400,
        helper_text="Klik 'Pilih Gambar' untuk memilih file",
        value=""
    )

    # File info display
    file_info = ft.Container(
        content=ft.Text("Belum ada file dipilih", 
                       size=12, 
                       color=ft.colors.GREY_400),
        margin=ft.margin.only(top=5, bottom=10)
    )

    # File picker
    def pick_files_result(e: ft.FilePickerResultEvent):
        if e.files:
            selected_file = e.files[0]
            file_path_display.value = selected_file.path
            
            # Update file info
            try:
                file_size = os.path.getsize(selected_file.path)
                file_size_mb = file_size / (1024 * 1024)
                file_extension = os.path.splitext(selected_file.name)[1].upper()
                file_info.content.value = f"📄 {selected_file.name} | 📏 {file_size_mb:.2f} MB | 🔧 {file_extension}"
                file_info.content.color = ft.colors.GREEN_400
                
                # Enable analyze button
                analyze_button.content.disabled = False
            except Exception as ex:
                file_info.content.value = f"❌ Error reading file info: {str(ex)}"
                file_info.content.color = ft.colors.RED_400
                analyze_button.content.disabled = True
                
            page.update()

    file_picker = ft.FilePicker(on_result=pick_files_result)
    page.overlay.append(file_picker)

    # Pick files button
    pick_button = ft.Container(
        content=ft.ElevatedButton(
            text="📂 Pilih Gambar",
            icon=ft.icons.FOLDER_OPEN,
            width=200,
            height=45,
            style=ft.ButtonStyle(
                color=ft.colors.WHITE,
                bgcolor=ft.colors.PURPLE_600,
                overlay_color=ft.colors.PURPLE_700
            ),
            on_click=lambda _: file_picker.pick_files(
                dialog_title="Pilih gambar untuk dianalisis",
                file_type=ft.FilePickerFileType.IMAGE,
                allow_multiple=False
            )
        ),
        alignment=ft.alignment.center,
        margin=ft.margin.only(top=10, bottom=20)
    )

    # Progress indicator
    progress_ring = ft.Container(
        content=ft.Row([
            ft.ProgressRing(width=16, height=16, stroke_width=2),
            ft.Text("Sedang menganalisis gambar...", size=12, color=ft.colors.PURPLE_400)
        ]),
        visible=False
    )

    # Analyze button
    analyze_button = ft.Container(
        content=ft.ElevatedButton(
            text="🔍 Analisis Gambar",
            icon=ft.icons.ANALYTICS,
            width=200,
            height=45,
            disabled=True,
            style=ft.ButtonStyle(
                color=ft.colors.WHITE,
                bgcolor=ft.colors.GREEN_600,
                overlay_color=ft.colors.GREEN_700
            )
        ),
        alignment=ft.alignment.center,
        margin=ft.margin.only(top=10, bottom=20)
    )

    # Output field
    output_field = ft.TextField(
        label="📝 Hasil analisis gambar",
        multiline=True,
        min_lines=8,
        max_lines=12,
        read_only=True,
        border_color=ft.colors.GREEN_400,
        text_size=14,
        helper_text="Hasil deskripsi akan muncul di sini"
    )

    # Output info
    output_info = ft.Container(
        content=ft.Text("Belum ada hasil analisis", 
                       size=12, 
                       color=ft.colors.GREY_400,
                       text_align=ft.TextAlign.RIGHT),
        alignment=ft.alignment.center_right,
        margin=ft.margin.only(top=5)
    )

    # Statistics container
    stats_container = ft.Container(
        content=ft.Row([
            ft.Container(
                content=ft.Column([
                    ft.Text("📊 Info File", weight=ft.FontWeight.BOLD, size=12),
                    ft.Text("Belum dipilih", size=10, color=ft.colors.GREY_400, ref=ft.Ref[ft.Text]()),
                    ft.Text("Format: -", size=10, color=ft.colors.GREY_400, ref=ft.Ref[ft.Text]())
                ]),
                bgcolor=ft.colors.GREY_900,
                border_radius=8,
                padding=10,
                expand=True
            ),
            ft.Container(width=10),
            ft.Container(
                content=ft.Column([
                    ft.Text("⚡ Status", weight=ft.FontWeight.BOLD, size=12),
                    ft.Text("Siap", size=10, color=ft.colors.GREEN_400, ref=ft.Ref[ft.Text]())
                ]),
                bgcolor=ft.colors.GREY_900,
                border_radius=8,
                padding=10,
                expand=True
            )
        ]),
        margin=ft.margin.only(top=20)
    )

    # --- FUNGSI EVENT HANDLER ---
    def start_analysis(e):
        """Dipanggil saat tombol 'Analisis Gambar' diklik."""
        image_path = file_path_display.value
        
        # Validasi
        if not image_path or not image_path.strip():
            show_snackbar("⚠️ Mohon pilih file gambar terlebih dahulu!", ft.colors.ORANGE_600)
            return

        # Tampilkan status loading & nonaktifkan tombol
        progress_ring.visible = True
        analyze_button.content.disabled = True
        pick_button.content.disabled = True
        output_field.value = ""
        output_info.content.value = "Sedang menganalisis..."
        stats_container.content.controls[1].content.controls[1].value = "Memproses..."
        stats_container.content.controls[1].content.controls[1].color = ft.colors.ORANGE_400
        page.update()
        
        # Panggil fungsi analisis gambar (proses backend)
        analysis_result = describe_image(image_path)
        
        # Sembunyikan status loading & aktifkan kembali tombol
        progress_ring.visible = False
        analyze_button.content.disabled = False
        pick_button.content.disabled = False
        
        # Tampilkan hasil
        output_field.value = analysis_result
        result_length = len(analysis_result)
        
        if analysis_result.startswith("Error:") or analysis_result.startswith("Terjadi"):
            output_info.content.color = ft.colors.RED_400
            output_info.content.value = "❌ Terjadi kesalahan"
            stats_container.content.controls[1].content.controls[1].value = "Error"
            stats_container.content.controls[1].content.controls[1].color = ft.colors.RED_400
            show_snackbar("❌ Terjadi kesalahan saat menganalisis", ft.colors.RED_600)
        else:
            output_info.content.color = ft.colors.GREEN_400
            output_info.content.value = f"✅ Analisis selesai | {result_length:,} karakter"
            stats_container.content.controls[1].content.controls[1].value = "✅ Berhasil"
            stats_container.content.controls[1].content.controls[1].color = ft.colors.GREEN_400
            show_snackbar("✅ Analisis gambar berhasil!", ft.colors.GREEN_600)
            
        page.update()

    def clear_all(e):
        """Membersihkan semua field."""
        file_path_display.value = ""
        output_field.value = ""
        file_info.content.value = "Belum ada file dipilih"
        file_info.content.color = ft.colors.GREY_400
        output_info.content.value = "Belum ada hasil analisis"
        output_info.content.color = ft.colors.GREY_400
        analyze_button.content.disabled = True
        stats_container.content.controls[0].content.controls[1].value = "Belum dipilih"
        stats_container.content.controls[0].content.controls[2].value = "Format: -"
        stats_container.content.controls[1].content.controls[1].value = "Siap"
        stats_container.content.controls[1].content.controls[1].color = ft.colors.GREEN_400
        page.update()

    def show_snackbar(message, color):
        """Menampilkan snackbar dengan pesan dan warna tertentu."""
        page.snack_bar = ft.SnackBar(
            content=ft.Text(message, color=ft.colors.WHITE),
            bgcolor=color,
            action="OK",
            action_color=ft.colors.WHITE
        )
        page.snack_bar.open = True
        page.update()

    # Clear button
    clear_button = ft.Container(
        content=ft.OutlinedButton(
            text="🗑️ Bersihkan",
            icon=ft.icons.CLEAR_ALL,
            on_click=clear_all,
            width=150,
            height=35
        ),
        alignment=ft.alignment.center,
        margin=ft.margin.only(top=10)
    )
        
    # Menghubungkan event ke fungsi
    analyze_button.content.on_click = start_analysis

    # Update statistics saat file dipilih
    def update_file_stats(file_path):
        if file_path and os.path.exists(file_path):
            try:
                file_size = os.path.getsize(file_path)
                file_size_mb = file_size / (1024 * 1024)
                file_name = os.path.basename(file_path)
                file_ext = os.path.splitext(file_path)[1].upper()
                
                stats_container.content.controls[0].content.controls[1].value = f"{file_name[:20]}..."
                stats_container.content.controls[0].content.controls[2].value = f"Format: {file_ext} | {file_size_mb:.1f}MB"
            except:
                stats_container.content.controls[0].content.controls[1].value = "Error reading file"
                stats_container.content.controls[0].content.controls[2].value = "Format: Unknown"

    # --- MENYUSUN TAMPILAN ---
    page.add(
        header,
        file_path_display,
        file_info,
        pick_button,
        ft.Row([
            analyze_button,
            progress_ring
        ], alignment=ft.MainAxisAlignment.CENTER),
        ft.Divider(height=30),
        output_field,
        output_info,
        clear_button,
        stats_container,
        ft.Container(height=20)  # Spacer di bawah
    )

# Menjalankan aplikasi
if __name__ == "__main__":
    ft.app(target=main)