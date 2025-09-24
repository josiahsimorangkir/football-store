Nama: Josiah Naphta Simorangkir

NPM: 2406414593

Kelas: PBP F

Tautan PWS: https://josiah-naphta-footballstore.pbp.cs.ui.ac.id/

# Tugas 2

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

# Tugas 3

Pertanyaan 1:  Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Dalam pengembangan sebuah platform, data delivery berguna karena untuk komunikasi antar stack dengan menggunakan format standar seperti HTML, XML, dan JSON. HTML biasanya digunakan untuk menyampaikan data dalam bentuk tampilan, sementara XML dan JSON lebih sering dipakai untuk pertukaran data antar sistem karena bersifat terstruktur, mudah dibaca. Dengan adanya mekanisme data delivery, platform dapat mengirim dan menerima data.

Pertanyaan 2: Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?

JSON lebih populer dibandingkan XML karena strukturnya yang lebih ringkas, sederhana, dan mudah dipahami. JSON menggunakan format key–value yang langsung cocok dengan struktur data pada bahasa pemrograman modern, sehingga proses parsing dan manipulasi data menjadi lebih cepat, terutama untuk aplikasi web dan mobile. Selain itu, JSON memiliki ukuran yang lebih kecil yang membuat transfer data melalui jaringan lebih ringan dibandingkan XML yang banyak menggunakan tag pembuka dan penutup.Jadi menurut saya JSON lebih baik.

Pertanyaan 3: Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?

Method is_valid() pada form Django berfungsi untuk memvalidasi data yang dikirimkan melalui form. Saat form menerima input dari user, Django memeriksa apakah semua field sudah diisi sesuai aturan yang didefinisikan di dalam form. Jika semua data lolos validasi, is_valid() akan mengembalikan True dan kita bisa mengakses data yang sudah dibersihka. Sebaliknya, jika ada kesalahan, is_valid() akan mengembalikan False dan semua pesan error akan disimpan di dalam atribut errors.

Pertanyaan 4: Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

csrf_token pada Django diperlukan untuk melindungi aplikasi dari serangan Cross-Site Request Forgery (CSRF), yaitu serangan di mana penyerang memanfaatkan browser korban yang sudah login untuk mengirimkan permintaan berbahaya. Token ini memastikan setiap request yang dapat mengubah data (seperti POST, PUT, DELETE) benar-benar berasal dari halaman aplikasi kita, bukan dari situs lain. Jika csrf_token tidak digunakan, penyerang dapat membuat halaman berisi form tersembunyi atau script yang otomatis mengirim permintaan ke server menggunakan cookie sesi korban, sehingga aksi penting seperti mengubah password, melakukan transfer, atau menghapus data bisa dieksekusi secara ilegal.

Pertanyaan 5: Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

1. Buat folder templates pada direktori utama dan buat sebuah berkas HTML baru bernama base.html.
2. Menambahkan BASE_DIR / 'templates' ke dalam INSTALLED APPS yang ada di settings.py
3. Buat berkas baru pada direktori main dengan nama forms.py untuk membuat struktur form yang dapat menerima data Product baru. Isi field dengan atribut-atribut yang dibutuhkan.
4. Ubah main.html sesuai dengan keinginan dan kebutuhan yang diperlukan sebuah website toko olahraga. Buat juga create_product.html dan product_detail.html untuk menampilkan halaman form input dan detail produk.
5. Tambahkan entri url proyek pws pada CSRF_TRUSTED_ORIGINS di settings.py
6. Tambahkan beberapa import pada views.py lalu tambahkan fungsi create_product(), show_product(), show_xml(), show_json(), show_xml_by_id(), dan show_json_by_id().
7. Import fungsi yang sudah dibuat ke dalam urls.py pada direktori main
8. Terakhir, tambahkan path URL ke dalam urlpatterns

Pertanyaan 6: Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?

Tidak ada

Screenshot Postman
<img width="1817" height="884" alt="image" src="https://github.com/user-attachments/assets/238f7dba-ee96-4874-b4bc-01bbcc1b54cb" />

<img width="1818" height="891" alt="image" src="https://github.com/user-attachments/assets/1acbef3d-8ca8-4c30-910b-44aac76f21a7" />


<img width="1804" height="799" alt="image" src="https://github.com/user-attachments/assets/c21913dc-5fd7-460e-9474-f112fdf5bcca" />

<img width="1819" height="872" alt="image" src="https://github.com/user-attachments/assets/beb28a39-6078-45f5-9c53-d13767f67654" />


# Tugas 4
 
## Soal 1: Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.


AuthenticationForm adalah form bawaan Django (django.contrib.auth.forms.AuthenticationForm) yang memudahkan validasi username + password. Fungsinya memanggil authenticate() dan mengecek kredensial.

Kelebihan: 
  1. Mudah dipasang pada custom login view atau LoginView.
  2. Adanya handling error yang baik.

Kekurangan: 
  1. Tidak menyediakan rate-limiting / throttle / brute-force protection
  2. Hanya menangani username + password standar

## Soal 2: Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?


Singkatnya, perbedaan antara autentikasi dan otorisasi adalah autentikasi proses untuk mengecek identitas, sedangkan otorisasi adalah proses mengecek hak/izin setelah identitas terverifikasi. Implementasi untuk autentikasi pada Django: django.contrib.auth menyediakan User model, backends (authenticate()), views/helpers (login(), logout()), dan forms (AuthenticationForm, UserCreationForm). Implementasi untuk otorisasi pada Django: permissions & groups (user.has_perm('app.change_model'), @permission_required), is_staff, is_superuser, serta decorators seperti @login_required (ini autentikasi) dan middleware/utility untuk permission checks.

## Soal 3:  Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?


### Cookies

Kelebihan: mudah, persisten across requests, cocok untuk data kecil.

Kekurangan: ukuran teApakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?rbatas, mudah diubah oleh client → risiko integritas, raw cookies dapat dilihat/diubah kecuali disigned/encrypted, rentan XSS (jika tidak HttpOnly).

### Sessions

Kelebihan: data disimpan server → lebih aman, menyimpan lebih banyak data, mudah dicabut/expire dari server, cocok untuk data sensitif.

Kekurangan: butuh storage, perlu skala jika ada banyak user (session store → redis/memcached), masih bergantung pada cookie session id (jadi harus amankan cookie).

## Soal 4: Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

Tidak otomatis aman. Risiko utama: XSS (cookie dicuri via JS), man-in-the-middle (intersepsi) jika tidak HTTPS, CSRF (cross-site request forgery) jika cookie dikirim secara tidak aman.

Django menangani hal tersebut dengan:
  1. CSRF protection: middleware + template tag {% csrf_token %}; Django mengeluarkan CSRF cookie dan mengecek token pada POST/unsafe requests.
  2. CSRF_COOKIE_SECURE, CSRF_COOKIE_HTTPONLY (CSRF cookie biasanya bukan HttpOnly karena JS harus membaca token; oleh karena itu CSRF cookie sering tidak HttpOnly).
  3. Signed cookies: HttpResponse.set_signed_cookie().Django meng-sign cookie sehingga server bisa mendeteksi perubahan/tampering.


## Soal 5: Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

  1. Tambahkan import UserCreationForm dan messages pada views.py
  2. Tambahkan fungsi register di bawah ini ke dalam views.py
  3. Membuat berkas baru bernama register.html di main/templates dengan kode seperti di tutorial
  4. Import fungsi register di urls.py dan tambahkan path url ke urlpatterns
  5. Tambahkan import authenticate, login, dan AuthenticationForm pada views.py
  6. Tambahkan fungsi login_user di bawah ini ke dalam views.py. Kode dari login_user seperti di tutorial
  7. Membuat berkas baru bernama login.html dan isi berkas dengan kode seperti di tutorial
  8. Import fungsi login_user di urls.py dan tambahkan path url ke urlpatterns
  9. Tambahkan import logout pada views.py
  10. Tambahkan fungsi logout_user ke dalam fungsi views.py. Kodenya seperti di tutorial
  11. Tambahkan button logout pada main.html
  12. Import fungsi logout_user di urls.py dan tambahkan path url ke urlpatterns
  13. Tambahkan import login_required pada views.py
  14. Tambahkan potongan kode @login_required(login_url='/login') di atas fungsi show_main dan show_product
  15. Tambahkan import HttpResponseRedirect, reverse, dan datetime pada views.py
  16. Ubah fungsi login_user untuk menyimpan cookie baru bernama last_login
  17. Tambahkan 'last_login': request.COOKIES['last_login'] ke dalam variable context
  18. Ubah fungsi logout_user untuk menghapus cookie last_login setelah melakukan logout.
  19. Tambahkan last_login pada main.html
  20. Import user pada models.py
  21. Tambahkan relationship di models.py untuk menghubungkan satu product ke satu user dengan potongan kode user = models.ForeignKey(User, on_delete=models.CASCADE, null=True). Jangan lupa migrasi
  22. Ubah fungsi create_product agar setiap objek yang dibuat akan secara otomatis terhubung dengan pengguna yang membuatnya.
  23. Modifikasi fungsi show_main agar dilengkapi dengan filter artikel berdasarkan penulis
  24. Tambahkan tombol filter My dan All pada halaman main.html dan juga tampilkan nama author di product_detail.html
