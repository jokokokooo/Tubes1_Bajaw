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
<pre></pre>
├── game
│   ├── logic
│   │   ├── __init__.py              
│   │   ├── bajaw.py                 
│   │   ├── base.py                  
│   │   ├── random.py                
│   ├── __init__.py                  
│   ├── api.py                       
│   ├── board_handler.py            
│   ├── bot_handler.py              
│   ├── models.py                   
│   ├── util.py                     
├── .gitignore                      
├── decode.py                       
├── main.py                         
├── README.md                       
├── requirements.txt                
├── run-bots.bat                    
├── run-bots.sh                     
<pre></pre>

Kelebihan
-Lebih efektif dalam mengumpulkan poin.
-Tidak mengejar diamond sembarangan.
-Fleksibel dan aman saat menghadapi ancaman dari bot lain.

Catatan
Pastikan backend game engine sudah berjalan di localhost:3000/api, dan token bot tersedia jika menggunakan akun lama. Performa bot dapat bervariasi tergantung konfigurasi papan permainan (board state) dan kecepatan musuh.
