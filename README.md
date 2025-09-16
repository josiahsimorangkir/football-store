Nama: Josiah Naphta Simorangkir
NPM: 2406414593
Kelas: PBP F
Tautan PWS: https://josiah-naphta-footballstore.pbp.cs.ui.ac.id/

Poin 1: Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
    Step 1: Buat proyek django
        - Buat direktori baru dengan nama Football-Store
        - Buat virtual environment (Windows)
        - Mengaktifkan virtual environment
        - Buat requirements.txt serta tambahkan beberapa dependencies seperti di Tutorial 0
        - Instalasi terhadap dependencies
        - Buat proyek dengan django-admin startproject football_news .
    
    Step 2: Konfigurasi environment
        - Buat file .env dan isi dengan PRODUCTION = false
        - Buat file .env.prod yang akan digunakan untuk production deployment dan isi berkas dengan kredensial yang diperoleh dari email ITF Fasilkom UI
        - Modifikasi file settings.py dengan menambahkan kode seperti di Tutorial 0
        - Tambahkan local host di list ALLOWED_HOSTS
        - Tambahkan konfigurasi PRODUCTION di settings.py
        - Ubah konfigurasi database di settings.py seperti di Tutorial 0
    
    Step 3: Jalankan Server
        - Jalankan migrasi database
        - Jalankan server django

    Step 4: Buat aplikasi main
        - Membentuk direktori baru dengan nama main dengan menjalankan perintah python manage.py startapp main
        - Tambahkan 'main' ke dalam INSTALLED_APPS yang ada di settings.py
    
    Step 5: Membuat template yang berada di main
        - Buat direktori baru bernama templates di dalam main
        - Buat berkas baru bernama main.html di dalam templates
        - Isi berkas dengan informasi nama toko, nama, dan kelas
    
    Step 6: Mendefinisikan berkas models.py
        - Isi berkas models.py dengan class Products dengan atribut wajib, seperti name, price, description, thumbnail, category, is_featured
        
    Step 7: Migrasi model
        - Menjalankan perintah python manage.py makemigrations untuk membuat migrasi model
        - Menjalankan perintah python manage.py migrate untuk menerapkan migrasi ke lokal
    
    Step 8: Mengintegrasikan Komponen MVT
        - Tambahkan baris kode import-import yang dibutuhkan pada views.py
        - Tambahkan fungsi show_main seperti di Tutorial 1

    Step 9: Modifikasi template
        - Ubah informasi nama, nama toko, dan kelas menjadi struktur kode django(template variables)

    Step 10: Mengkonfigurasi Routing URL
        - Buat berkas urls.py di dalam main
        - Isi berkas dengan kode seperti di Tutorial 1

    Step 11: Mengkonfigurasi Routing URL Proyek
        - Import fungsi include dari django.urls ke dalam berkas urls.py yang didalam direktori proyek
        - Tambah rute URL path('', include('main.urls')) ke dalam urlpatterns
    
    Step 12: Push ke repo
        - git add .
        - git commit -m "(sesuai dengan tugasnya)"
        - git push origin master
        - git push pws master

