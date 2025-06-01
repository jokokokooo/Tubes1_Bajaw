Bajaw Bot
Bajaw adalah bot permainan berbasis strategi greedy untuk kompetisi pengumpulan diamond dalam game engine STIMA. Bot ini didesain untuk bermain secara efisien dengan mengutamakan pengambilan diamond bernilai tinggi dalam jarak yang optimal, menggunakan pendekatan Greedy by Value-to-Distance Ratio.

Strategi Bot
Bajaw menggunakan strategi greedy yang cerdas:
-Memilih diamond berdasarkan rasio nilai/jarak tertinggi.
-Menghindari musuh saat membawa banyak diamond.
-Pulang ke base secara aman ketika kantong penuh.
-Menghindari dinding dan bergerak secara valid dalam peta permainan.
-Secara adaptif mengubah arah saat tidak memiliki target pasti.

Cara Menjalankan
Pastikan semua dependensi telah terinstall sesuai requirements.txt.

Jalankan dengan command berikut:

python main.py --logic Bajaw --email=test@email.com --name=Bajaw --password=123456 --team etimo
Atau melalui file batch:
./run-bots.bat
Ganti parameter sesuai dengan akun dan nama bot kamu.

Struktur Folder
tubes1-IF2211-bot-starter-pack-1.0.1/
├── game/
│   ├── logic/
│   │   ├── __init__.py              # Inisialisasi modul logic
│   │   ├── bajaw.py                 # Logika utama bot Bajaw (bot milikmu)
│   │   ├── base.py                  # Base class untuk bot logic
│   │   ├── random.py                # Bot logika dasar acak (random)
│   ├── __init__.py                  # Inisialisasi modul game
│   ├── api.py                       # Koneksi API ke game engine (POST/GET)
│   ├── board_handler.py            # Handler untuk manipulasi papan/board
│   ├── bot_handler.py              # Handler bot (register, move, recover)
│   ├── models.py                   # Definisi model data seperti Bot, Board
│   ├── util.py                     # Fungsi utilitas seperti get_direction()
├── .gitignore                      # Mengabaikan file tertentu di Git
├── decode.py                       # Dekoder response dari backend API
├── main.py                         # Entry point untuk menjalankan bot
├── README.md                       # Dokumentasi utama proyek
├── requirements.txt                # Daftar dependensi Python
├── run-bots.bat                    # File batch Windows untuk jalankan bot
├── run-bots.sh                     # File shell Linux/Mac untuk jalankan bot

Kelebihan
-Lebih efektif dalam mengumpulkan poin.
-Tidak mengejar diamond sembarangan.
-Fleksibel dan aman saat menghadapi ancaman dari bot lain.

Catatan
Pastikan backend game engine sudah berjalan di localhost:3000/api, dan token bot tersedia jika menggunakan akun lama. Performa bot dapat bervariasi tergantung konfigurasi papan permainan (board state) dan kecepatan musuh.
