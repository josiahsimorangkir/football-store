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
  
Poin 2: Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html

  <img width="1082" height="306" alt="image" src="https://github.com/user-attachments/assets/1387a12e-ea1c-4b6b-bc5a-6efc46349fd0" />
  Alur:

  Ketika seorang pengguna (client) mengakses suatu halaman web melalui browser, misalnya dengan mengetikkan alamat URL atau mengklik sebuah tautan, browser akan mengirimkan sebuah HTTP request ke 
  server tempat aplikasi Django berjalan. Django pertama-tama akan menerima request tersebut dan mencocokkan URL yang diminta dengan pola-pola URL yang telah didefinisikan di dalam file urls.py. 
  Jika ditemukan kecocokan, Django akan meneruskan request itu ke fungsi atau class yang sesuai di dalam views.py.

Di dalam views.py, Django memproses logika aplikasi. Fungsi view dapat mengambil data dari database menggunakan model yang telah didefinisikan dalam file models.py. Django menggunakan ORM 
(Object-Relational Mapping) untuk mengakses database, sehingga kita tidak perlu menulis query SQL secara langsung. Setelah data diperoleh dan logika selesai dijalankan, fungsi view akan 
menyiapkan data untuk ditampilkan kepada user.

Selanjutnya, view akan merender tampilan menggunakan file template HTML yang biasanya disimpan di folder templates/. Data yang telah diambil dari database akan dimasukkan ke dalam template ini, 
lalu template dirender menjadi halaman HTML. Setelah proses render selesai, Django mengembalikan hasilnya dalam bentuk HTTP response ke browser. Akhirnya, browser menampilkan halaman web tersebut kepada user.

Poin 3: Jelaskan peran settings.py dalam proyek Django!

  File settings.py dalam proyek Django berfungsi sebagai pusat konfigurasi utama yang mengatur cara kerja seluruh aplikasi. Di dalamnya, terdapat pengaturan penting seperti koneksi database, 
  daftar aplikasi yang digunakan (INSTALLED_APPS), lokasi file template, serta konfigurasi keamanan seperti DEBUG, dan ALLOWED_HOSTS. Tanpa settings.py, Django tidak akan tahu bagaimana cara menjalankan 
  proyek dengan benar, karena semua komponen bergantung pada konfigurasi ini.

Poin 4: Bagaimana cara kerja migrasi database di Django?

  Migrasi database di Django adalah proses untuk menyamakan perubahan yang dilakukan pada model (file models.py) dengan struktur database yang sebenarnya. Saat developer membuat atau mengubah model, 
  Django tidak langsung mengubah database, melainkan mencatat perubahan tersebut melalui perintah python manage.py makemigrations. Perintah ini akan menghasilkan file migrasi yang berisi instruksi 
  tentang perubahan struktur data, seperti penambahan tabel atau kolom. Setelah itu, perintah python manage.py migrate digunakan untuk menerapkan perubahan tersebut ke database. Proses ini memungkinkan 
  pengelolaan struktur database secara otomatis, terkontrol, dan tanpa perlu menulis SQL secara manual.

Poin 5: Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?

  Django sering dijadikan permulaan pembelajaran karena framework ini meyediakan hampir smeua fitur yang dibutuhkan untuk membangun aplikasi web secara lengkap dan terstruktur.
  Dengan menggunakan Django, kami sebagai pemula tidak perlu memilih library tambahan, karena adanya fitur ORM, sistem routing, templating, dan lain lain. Django juga memiliki dokumentasi yang lengkap dan jelas.
   Django juga melatih kita untuk mengikuti struktur proyek yang rapi dan konsisten. Intinya, Django menyediakan lingkungan belajar yang terpadu untuk memahami bagaimana aplikasi dibangun.

Poin 6: Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?

  Menurut saya asdos tutorial 1 sudah sangat baik dan jelas dalam memberikan tutorial. Maka dari itu dari saya tidak ada saran ataupun kritik.
