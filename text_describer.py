import google.generativeai as genai
import PySimpleGUI as sg
import textwrap # Library untuk memotong teks jika terlalu panjang

# --- KONFIGURASI PENTING ---
# GANTI TULISAN "YOUR_API_KEY_HERE" DENGAN KUNCI API YANG SUDAH ANDA SALIN.
# Pastikan Anda mendapatkan kunci API dari Google AI Studio.
API_KEY = "API_KEY_GEMINI_ANDA" 

# Batas maksimal karakter yang diizinkan
MAX_CHARS = 100000

# Konfigurasi model AI Google
try:
    genai.configure(api_key=API_KEY)
    # Menggunakan model 'gemini-2.5-flash' yang efisien untuk tugas teks
    model = genai.GenerativeModel('gemini-2.5-flash') 
except Exception as e:
    sg.popup_error(f"Error Konfigurasi API: {e}\n\nPastikan API Key Anda sudah benar dan koneksi internet aktif.")
    exit()

# --- FUNGSI UTAMA ---
def translate_text(text_to_translate):
    """Mengirim teks ke AI dan mendapatkan terjemahan ke Bahasa Indonesia."""
    if not text_to_translate.strip():
        return "Error: Tidak ada teks untuk diterjemahkan."
    
    # Memastikan teks tidak melebihi batas API (sebagai pengaman tambahan)
    if len(text_to_translate) > MAX_CHARS:
        return f"Error: Teks melebihi batas maksimal {MAX_CHARS} karakter."

    try:
        # Prompt yang jelas untuk AI agar fokus pada terjemahan
        prompt = f"""
        Translate the following text into clear and natural-sounding Indonesian.
        Provide only the translated text as the result, without any additional comments, explanations, or introductions.

        --- TEXT TO TRANSLATE ---
        {text_to_translate}
        --- END OF TEXT ---
        """
        
        # Kirim prompt ke model AI
        response = model.generate_content(prompt)
        
        return response.text
    except Exception as e:
        # Memberikan pesan error yang lebih informatif
        error_message = str(e)
        # Memotong pesan error jika terlalu panjang agar muat di popup
        wrapped_error = "\n".join(textwrap.wrap(error_message, 80))
        return f"Terjadi kesalahan saat menghubungi API:\n\n{wrapped_error}"

# --- TAMPILAN APLIKASI (GUI) ---
sg.theme('DarkBlue3')

# Ukuran diperkecil sekitar 20% (dari 80x15 menjadi 64x12)
layout = [
    [sg.Text("Text Translator", font=('Helvetica', 14))], # Font sedikit diperkecil
    [sg.Text("Masukkan teks yang ingin diterjemahkan ke Bahasa Indonesia:")],
    [sg.Multiline(size=(64, 12), key='-INPUT_TEXT-', enable_events=True)], # Ukuran diperkecil
    [sg.Text(f"0 / {MAX_CHARS}", key='-CHAR_COUNT-', size=(20, 1))],
    [sg.Button("Terjemahkan", key='-SUBMIT-'), sg.Button("Keluar")],
    [sg.HorizontalSeparator()],
    [sg.Text("Hasil Terjemahan:", font=('Helvetica', 11))], # Font sedikit diperkecil
    [sg.Multiline(size=(64, 12), key='-OUTPUT-', disabled=True)], # Ukuran diperkecil
    [sg.Text("Jumlah Karakter Hasil: 0", key='-OUTPUT_CHAR_COUNT-', size=(40, 1))] 
]

window = sg.Window('Text Translator AI', layout, resizable=True)

# --- LOOP UTAMA APLIKASI ---
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == "Keluar":
        break
    
    # Event untuk update penghitung karakter setiap kali ada ketikan
    if event == '-INPUT_TEXT-':
        char_count = len(values['-INPUT_TEXT-'])
        window['-CHAR_COUNT-'].update(f"{char_count} / {MAX_CHARS}")
        # Ubah warna teks menjadi merah jika melebihi batas
        if char_count > MAX_CHARS:
            window['-CHAR_COUNT-'].update(text_color='red')
        else:
            window['-CHAR_COUNT-'].update(text_color='white') # Ganti 'white' sesuai warna teks default tema Anda

    # Event saat tombol "Terjemahkan" ditekan
    if event == '-SUBMIT-':
        source_text = values['-INPUT_TEXT-']
        
        # Validasi input
        if not source_text.strip():
            sg.popup("Teks input tidak boleh kosong!", title="Peringatan")
            continue

        if len(source_text) > MAX_CHARS:
            sg.popup(f"Teks melebihi batas maksimal {MAX_CHARS} karakter!", title="Error")
            continue
            
        # Tampilkan status "memproses" dan reset penghitung output
        window['-OUTPUT-'].update("Sabar yaa anak ngentot...")
        window['-OUTPUT_CHAR_COUNT-'].update("Jumlah Karakter Hasil: 0") # Reset penghitung
        window.refresh() # Paksa jendela untuk update tampilan
        
        # Panggil fungsi terjemahan
        translation = translate_text(source_text)
        
        # Tampilkan hasil terjemahan
        window['-OUTPUT-'].update(translation)
        
        # Update penghitung karakter hasil terjemahan jika tidak ada error
        if not translation.startswith("Error:") and not translation.startswith("Terjadi kesalahan"):
             output_char_count = len(translation)
             window['-OUTPUT_CHAR_COUNT-'].update(f"Jumlah Karakter Hasil: {output_char_count}")

window.close()