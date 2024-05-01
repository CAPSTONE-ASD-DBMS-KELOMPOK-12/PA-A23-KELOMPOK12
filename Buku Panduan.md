# Program-Sustainablehood
# Anggota Kelompok
1. Diva Tri Andini (2309116011)
2. David Sebastian (2309116041)
3. Rifqi Hadi Wijaya (2309116042)
4. Tri Rahayu Septiyani (2309116004)
# Deskripsi Program
Program Sustainablehood adalah program dimana sebuah komunitas mewadahi penggunanya untuk berbagi dan mendonasikan produk yang tidak terpakai namun masih layak pakai secara berkelanjutan dan membagikannya kepada yang membutuhkan. Program ini memungkinkan pengguna, yaitu donatur untuk mendonasikan barangnya dan penerima untuk menerima barang donasi yang kemudian pada proses pendonasiannya dikelola oleh admin komunitas tersebut.

Program ini dibuat menggunakan bahasa pemrograman Python dan mengimplementasikan struktur data Linked List. Program Sustainablehood menggunakan database MySQL untuk menyimpan data pengguna, seperti Admin, Donatur, dan Penerima serta menyimpan data donasi dan barang. 
# Struktur Project
1. Folder Controller, berisi file-file controller yang bertindak sebagai perantara antara model dan view. Selain itu, folder controller berisi alur yang mengatur jalannya program.
  - File admin_controller berisi logika yang mengimplementasikan kelas Admin untuk mengelola data donasi, barang serta akun penerima.
  - File donatur_controller berisi kode yang mengimplementasikan kelas Donatur yang digunakan untuk mengelola data barang milik donatur di aplikasi.
  - File akun_controller berisi kode yang mengimplementasikan kelas AkunController untuk mengelola akun pengguna dalam aplikasi donasi. Kelas ini memiliki fungsi-fungsi terkait registrasi dan login untuk tiga jenis pengguna: donatur, penerima, dan admin.
  - File linkedList_controller berisi kode yang mengimplementasikan berbagai fungsi untuk mengelola dan memproses data dalam linked list. Fungsi tersebut seperti pencarian data, pengurutan data, serta pengambilan data dari tabel.
2. Folder Model, berisi file model yang berfungsi untuk mengakses database, seperti file database yang berisi kelas untuk menghubungkan python dengan database.
3. Folder View, berisi file-file view yang bertanggung jawab untuk menampilkan antarmuka program kepada user.
  - File admin_view merupakan file yang menampilkan fitur yang dimiliki oleh admin untuk mengelola donasi dan barang.
  - File donatur_view merupakan file yang menampilkan fitur yang dimiliki oleh donatur untuk menyumbangkan barang serta melihat data donasi dan barang.
  - File penerima_view merupakan file yang menampilkan fitur yang dimiliki oleh penerima untuk melihat data donasi dan barang.
4. File main, merupakan file utama untuk menjalankan program.
# Fitur
Berikut merupakan fitur yang terdapat pada program Sustainablehood, yaitu:
1. Admin
  - Membuat donasi: admin bertanggung jawab untuk mengelola barang yang disumbangkan oleh donatur dan mendonasikan barang tersebut kepada penerima.
  - Menampilkan daftar donasi dan barang: admin dapat melihat seluruh daftar donasi dan daftar barang.
  - Memperbarui donasi: admin dapat memperbarui informasi yang terdapat pada daftar donasi.
  - Menghapus akun penerima: admin dapat menghapus akun penerima yang bersangkutan.
  - Mengurutkan daftar donasi dan barang: admin dapat mengurutkan daftar donasi berdasarkan tanggal terlama dan tanggal terbaru, serta mengurutkan donasi berdasarkan nama A-Z dan Z-A.
  - Mencari daftar donasi dan barang: admin dapat mencari daftar donasi dan barang berdasarkan ID.
2. Donatur
  - Menyumbangkan barang: donatur dapat menyumbangkan barang lalu selanjutnya dikelola oleh admin untuk proses pendonasian.
  - Menampilkan daftar donasi dan barang: donatur dapat melihat seluruh daftar donasi dan daftar barang.
  - Mengurutkan daftar donasi dan barang: donatur dapat mengurutkan daftar donasi berdasarkan tanggal terlama dan tanggal terbaru, serta mengurutkan donasi berdasarkan nama A-Z dan Z-A.
  - Mencari daftar donasi dan barang: donatur dapat mencari daftar donasi dan barang berdasarkan ID.
3. Penerima
  - Menampilkan daftar donasi dan barang: penerima dapat melihat seluruh daftar donasi dan daftar barang.
  - Mengurutkan daftar donasi dan barang: penerima dapat mengurutkan daftar donasi berdasarkan tanggal terlama dan tanggal terbaru, serta mengurutkan donasi berdasarkan nama A-Z dan Z-A.
  - Mencari daftar donasi dan barang: penerima dapat mencari daftar donasi dan barang berdasarkan ID.

Pada program ini juga terdapat beberapa modul yang digunakan, yaitu:
1. PrettyTable merupakan modul dalam python yang digunakan untuk membuat / mengeluarkan data dalam bentuk tabel.
2. Datetime merupakan modul yang digunakan jika suatu program membutuhkan segala operasi yang berhubungan dengan waktu, salah satu contonya pada program yaitu mengurutkan data donasi berdasarkan tanggal.
3. OS merupakan modul yang digunakan untuk berinteraksi dengan sistem operasi yang mendasarinya. Pada prorgram, modul OS berfungsi untuk membersihkan layar terminal.
4. Random merupakan modul yang menyediakan berbagai fungsi untuk menghasilkan bilangan acak. 
5. Time merupakan modul yang menyediakan berbagai fungsi untuk bekerja dengan waktu dan pengukuran waktu. Pada program, modul time digunakan untuk menjeda eksekusi program.
# Fungsionalitas
1. Registrasi: donatur dan penerima dapat melakukan registrasi sebelum masuk ke dalam Program Sustainablehood dengan mengisi beberapa informasi yang diperlukan.
2. Login dan Exit: admin, donatur, dan penerima dapat melakukan login ke dalam program dengan menggunakan username dan password yang telah dibuat, serta dapat keluar dari program dengan pilihan keluar (exit).
3. Penyumbangan Barang: donatur dapat melakukan penyumbangan barang serta melihat tata kelola barang dan donasi yang dilakukan oleh admin.
4. Pendonasian: admin bertanggung jawab mengelola seluruh pendonasian dan barang terhadap donatur dan penerima.
