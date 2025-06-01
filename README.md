Bot Bajaw - IF2211 Bot Strategy Pack

1. Penjelasan Singkat Algoritma Greedy

Bot **Bajaw** menggunakan algoritma **Greedy by Value-to-Distance Ratio**, yaitu strategi yang memprioritaskan pengambilan diamond berdasarkan perbandingan antara nilai (points) dan jaraknya dari posisi bot saat ini (distance). Bot ini selalu berusaha mendapatkan keuntungan maksimum dalam langkah tercepat dengan memilih diamond yang paling efisien terlebih dahulu. Jika tas penuh atau musuh terdekat membawa diamond dan berada dalam radius ancaman, bot akan segera kembali ke base untuk menyimpan diamond atau melakukan intersepsi terhadap musuh. Strategi ini membuat Bajaw cerdas dalam memilih langkah optimal tanpa menggunakan pencarian jalur berat seperti BFS.

2. Requirements & Instalasi
- Python ≥ 3.7
- Library Python tambahan:
  - `colorama`
  - `requests`
  - `dacite`

Untuk menginstal semua dependency, jalankan:

```bash
pip install -r requirements.txt

3. Cara Menjalankan Bot
Langkah-langkah menjalankan bot:
a. Mendaftarkan bot pertama kali
python main.py --logic Bajaw --name bajaw --email bajaw@bot.com --password 123456 --team bajaw
Bot akan terdaftar dan otomatis login jika belum pernah dibuat.
b. Menjalankan bot menggunakan token
Jika sudah punya token bot:
python main.py --logic Bajaw --token <TOKEN>
c. Mode Windows (opsional)
Jika tersedia file run-bots.bat, Anda dapat menjalankan dengan:
./run-bots.bat
4. Struktur File
tubes1-IF2211-bot-starter-pack-1.0.1/
├── game/
│   ├── logic/
│   │   ├── bajaw.py       
│   │   ├── base.py        
│   │   └── random.py      
│   ├── api.py
│   ├── board_handler.py
│   ├── bot_handler.py
│   ├── models.py
│   └── util.py
├── main.py                
├── requirements.txt       
├── README.md              
5. Author
Nama/NIM : Nikson Gabriel Sihombing/12314005
           Joko Prayogo/123140055
           Gohan Tua Jeremia Ambarita/123140160
Kelas : IF2211 - Strategi Algoritma
Bot : Bajaw

Deskripsi : Bot greedy berbasis efisiensi jarak terhadap nilai, mampu beradaptasi terhadap ancaman dan memprioritaskan keuntungan maksimal.
