import google.generativeai as genai
from PIL import Image
import PySimpleGUI as sg
import os

# --- KONFIGURASI PENTING ---
# Ganti tulisan "YOUR_API_KEY_HERE" dengan kunci API yang sudah Anda salin.
API_KEY = "" # GANTI DENGAN KUNCI API BARU ANDA

# Konfigurasi model AI Google
try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-2.5-flash')
except Exception as e:
    sg.popup_error(f"Error Konfigurasi API: {e}\n\nPastikan API Key Anda sudah benar dan koneksi internet aktif.")
    exit()

# --- FUNGSI UTAMA ---
def describe_image(image_path):
    """Mengirim gambar ke AI dan mendapatkan deskripsi."""
    if not os.path.exists(image_path):
        return "Error: File gambar tidak ditemukan."
    
    try:
        img = Image.open(image_path)
        
        prompt = "Jelaskan apa yang ada di dalam gambar ini dalam Bahasa Indonesia yang singkat dan jelas."
        
        # Kirim gambar dan prompt ke model AI
        response = model.generate_content([prompt, img])
        
        return response.text
    except Exception as e:
        return f"Terjadi kesalahan saat memproses gambar: {e}"

# --- TAMPILAN APLIKASI (GUI) ---
# Perhatikan semua baris di bawah ini sekarang rata kiri (tanpa spasi di awal)
sg.theme('DarkBlue3')

layout = [
    [sg.Text("Pilih Gambar untuk Dideskripsikan", font=('Helvetica', 16))],
    [sg.Input(key='-FILE_PATH-'), sg.FileBrowse("Cari Gambar", file_types=(("Image Files", "*.png *.jpg *.jpeg"),))],
    [sg.Button("Mulai Deskripsikan", key='-SUBMIT-'), sg.Button("Keluar")],
    [sg.Text("Hasil Deskripsi:", font=('Helvetica', 12))],
    [sg.Multiline(size=(60, 10), key='-OUTPUT-', disabled=True, font=('Arial', 11))]
]

window = sg.Window('Image Describer AI', layout)

# --- LOOP UTAMA APLIKASI ---
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == "Keluar":
        break
    
    if event == '-SUBMIT-':
        image_path = values['-FILE_PATH-']
        if image_path:
            # Tampilkan status "memproses"
            window['-OUTPUT-'].update("Sedang memproses, mohon tunggu...")
            window.refresh() # Paksa jendela untuk update tampilan
            
            # Panggil fungsi deskripsi dan tampilkan hasilnya
            description = describe_image(image_path)
            window['-OUTPUT-'].update(description)
        else:
            sg.popup("Mohon pilih file gambar terlebih dahulu!")

window.close()