from Controller import akun_controller

objek_akun = akun_controller.AkunController()

def menu_penerima():
    while True:
        print("+--------------------------------------------------+")
        print("|            PROGRAM SUSTAINABLEHOOD               |")
        print("|                 MENU PENERIMA                    |")
        print("+--------------------------------------------------+")
        print("| [1] Login                                        |")
        print("| [2] Registrasi                                   |")
        print("| [0] Kembali                                      |")
        print("+--------------------------------------------------+")
        pilih = input("Masukkan pilihan (1/2/3/0): ")
        if pilih == "1":
            while True:
                print("+--------------------------------------------------+")
                print("|                 LOGIN PENERIMA                   |")
                print("+--------------------------------------------------+")
                username = input("Masukkan username: ")
                password = input("Masukkan password: ")
                objek_akun.login_penerima(username, password)
                break
        elif pilih == "2":
            print("+--------------------------------------------------+")
            print("|               REGISTRASI PENERIMA                |")
            print("+--------------------------------------------------+")
            while True:
                try:
                    nama = input("Masukkan nama lengkap: ").title()
                    if nama.strip():
                        break
                    else:
                        print("\n<< Nama tidak boleh kosong >>")
                except ValueError:
                    print('\n<< Input nama tidak sesuai >>')
            while True:
                try:
                    email = input("Masukkan alamat email: ")
                    if "@" in email and "." in email:
                        break
                    else:
                        print("\n<< Alamat email tidak valid >>")
                except ValueError:
                    print('\n<< Input alamat email tidak sesuai >>')
            while True:
                try:
                    no_hp = input("Masukkan nomor telepon lengkap: ")
                    if no_hp.isdigit() and len(no_hp) >= 10:  
                        break
                    else:
                        print('\n<< Nomor telepon tidak valid >>')            
                except ValueError:
                    print('\n<< Input nomor telepon tidak sesuai >>')
            while True:
                try:
                    alamat = input("Masukkan alamat lengkap: ").title()
                    if alamat.strip():
                        break
                    else:
                        print("\n<< Alamat tidak boleh kosong >>")               
                except ValueError:
                    print('\n<< Input alamat tidak sesuai >>')
            while True:
                try:
                    pekerjaan = input("Masukkan pekerjaan: ").title()
                    if pekerjaan.strip():
                        break
                    else:
                        print("\n<< Pekerjaan tidak boleh kosong >>")               
                except ValueError:
                    print('\n<< Input pekerjaan tidak sesuai >>')
            while True:
                try:
                    gaji = int(input("Masukkan jumlah gaji: "))
                    if gaji >= 0:
                        break
                    else:
                        print("\n<< Gaji harus lebih besar dari 0 atau 0 >>")            
                except ValueError:
                    print('\n<< Input gaji harus bilangan bulat >>')
            while True:
                try:
                    username = input("Masukkan username yang ingin dibuat: ")
                    if username.strip():
                        break
                    else:
                        print("\n<< Username tidak boleh kosong >>")            
                except ValueError:
                    print('\n<< Input username tidak sesuai >>')   
            while True:
                try:
                    password = input("Masukkan password yang ingin dibuat: ")
                    if password.strip():
                        break
                    else:
                        print("\n<< Password tidak boleh kosong >>")
                except ValueError:
                    print('\n<< Input password tidak sesuai >>')
            while True:
                try:
                    kebutuhan = input("Masukkan kebutuhan yang diperlukan: ").title()
                    if kebutuhan.strip():
                        break
                    else:
                        print("\n<< Pekerjaan tidak boleh kosong >>")               
                except ValueError:
                    print('\n<< Input pekerjaan tidak sesuai >>')
            id_penerima = 0
            objek_akun.registrasi_penerima(id_penerima, nama, email, no_hp, alamat, pekerjaan, gaji, kebutuhan, username, password)
        elif pilih == "0":
            print("<< Kembali ke menu utama >>")
            break
        else:
            print("<< Input tidak valid >>")

def menu_utama_penerima():
    while True:
        print("""
+--------------------------------------------------+
|            PROGRAM SUSTAINABLEHOOD               |
|              MENU UTAMA PENERIMA                 |
+--------------------------------------------------+
| [1] Buat Permintaan Kebutuhan                    |
| [2] Tampilkan Daftar Donasi dan Barang           |
| [3] Urutkan Daftar Donasi dan Barang             |
| [4] Cari Daftar Donasi dan Barang                |
| [0] Kembali                                      |
+--------------------------------------------------+""")
        pilih = input("Masukkan pilihan (1/2/3/0): ")
        if pilih == "1":
            pass
        elif pilih == "2":
            pass
        elif pilih == "3":
            pass
        elif pilih == "4":
            pass
        elif pilih == "0":
            print("<< Kembali ke menu utama >>")
            break
        else:
            print("<< Input tidak valid >>")
