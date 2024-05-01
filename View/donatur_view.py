from Controller import akun_controller
from Controller import admin_controller
from Controller import linkedList_controller
from Controller import donatur_controller
import time
import os

objek_akun = akun_controller.AkunController()
objek_admin = admin_controller.Admin()
objek_linkedlist = linkedList_controller.LinkedList()
objek_donatur = donatur_controller.Donatur()

def menu_donatur():
    while True:
        print("\n+--------------------------------------------------+")
        print("|            PROGRAM SUSTAINABLEHOOD               |")
        print("|                  MENU DONATUR                    |")
        print("+--------------------------------------------------+")
        print("| [1] Login                                        |")
        print("| [2] Registrasi                                   |")
        print("| [0] Kembali                                      |")
        print("+--------------------------------------------------+")
        pilih = input("Masukkan pilihan (1/2/3/0): ")
        if pilih == "1":
            while True:
                print("\n+--------------------------------------------------+")
                print("|                  LOGIN DONATUR                   |")
                print("+--------------------------------------------------+")
                username = input("Masukkan username: ")
                password = input("Masukkan password: ")
                objek_akun.login_donatur(username, password)
                break
        elif pilih == "2":
            print("\n+--------------------------------------------------+")
            print("|               REGISTRASI DONATUR                 |")
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
            id_donatur = 0
            cek = objek_akun.registrasi_donatur(id_donatur, nama, email, no_hp, alamat, username, password)
            if cek:
                print("\n<< Registrasi berhasil >>")
                return menu_donatur()
            else:
                print("\n<< Registrasi gagal >>")
        elif pilih == "0":
            print("\n<< Kembali ke menu awal program >>")
            break
        else:
            print("\n<< Input tidak valid >>")

def menu_utama_donatur():
    while True:
        print("\n+--------------------------------------------------+")
        print("|            PROGRAM SUSTAINABLEHOOD               |")
        print("|               MENU UTAMA DONATUR                 |")
        print("+--------------------------------------------------+")
        print("| [1] Sumbang Barang                               |")
        print("| [2] Tampilkan Daftar Donasi dan Barang           |")
        print("| [3] Urutkan Daftar Donasi dan Barang             |")
        print("| [4] Cari Daftar Donasi dan Barang                |")
        print("| [0] Kembali                                      |")
        print("+--------------------------------------------------+")
        pilih = input("Masukkan pilihan (1/2/3/4/0): ")
        if pilih == "1":
            os.system("cls")
            data_baru = donatur_controller.input_data_barang()
            objek_donatur.tambah_barang(data_baru)            
        elif pilih == "2":
            os.system("cls")
            print("\n+--------------------------------------------------+")
            print("|         Tampilkan Daftar Donasi & Barang         |")
            print("+--------------------------------------------------+")
            print("| [1] Lihat Daftar Donasi                          |")
            print("| [2] Lihat Daftar Barang                          |")
            print("| [0] Keluar                                       |")
            print("+--------------------------------------------------+")
            lihat = input("Masukkan pilihan (1/2/0): ")
            if lihat == "1":
                objek_admin.lihat_donasi()
                skip = input("Tekan Enter untuk kembali ke menu utama")
            elif lihat == '2':
                objek_donatur.lihat_barang()
                skip = input("Tekan Enter untuk kembali ke menu utama")
            else:
                print("\n<< Input tidak valid >>")
                time.sleep(2)
        elif pilih == "3":
            print("\n+--------------------------------------------------+")
            print("|            Sort Daftar Donasi & Barang           |")
            print("+--------------------------------------------------+")
            print("| [1] Sort Daftar Donasi                           |")
            print("| [2] Sort Daftar Barang                           |")
            print("| [0] Keluar                                       |")
            print("+--------------------------------------------------+")
            pil_sort = input("Masukkan pilihan (1/2/0): ")
            if pil_sort == "1":
                print("\n+--------------------------------------------------+")
                print("|                Sort Daftar Donasi                |")
                print("+--------------------------------------------------+")
                print("| [1] Sort Donasi Tanggal Terlama (Ascending)      |")
                print("| [2] Sort Donasi Tanggal Terbaru (Descending)     |")
                print("| [0] Keluar                                       |")
                print("+--------------------------------------------------+")
                pilSort = input("Masukkan pilihan (1/2/0): ")
                if pilSort == "1":
                    linkedList_controller.quick_sort_donasi_ascending()
                    skip = input("Tekan Enter untuk kembali ke menu utama")
                elif pilSort == "2":
                    linkedList_controller.quick_sort_donasi_descending()
                    skip = input("Tekan Enter untuk kembali ke menu utama")
                elif pilSort == "0":
                    break
                else:
                    print("\n<< Input tidak valid >>")
            elif pil_sort == "2":
                print("\n+--------------------------------------------------+")
                print("|                Sort Daftar Barang                |")
                print("+--------------------------------------------------+")
                print("| [1] Sort Nama Barang A-Z (Ascending)             |")
                print("| [2] Sort Nama Barang A-Z (Descending)            |")
                print("| [0] Keluar                                       |")
                print("+--------------------------------------------------+")
                pilSort = input("Masukkan pilihan (1/2/0): ")
                if pilSort == "1":
                    linkedList_controller.quick_sort_barang_ascending()
                    skip = input("Tekan Enter untuk kembali ke menu utama")
                elif pilSort == "2":
                    linkedList_controller.quick_sort_barang_descending()
                    skip = input("Tekan Enter untuk kembali ke menu utama")
                elif pilSort == "0":
                    break
                else:
                    print("\n<< Input tidak valid >>")
            elif pil_sort == "0":
                break
            else:
                print("\n<< Input tidak valid >>")
                time.sleep(2)        
        elif pilih == "4":
            os.system("cls")
            print("\n+--------------------------------------------------+")
            print("|              Sarch Donasi & Barang               |")
            print("+--------------------------------------------------+")
            print("| [1] Search Donasi                                |")
            print("| [2] Search Barang                                |")
            print("| [0] Keluar                                       |")
            print("+--------------------------------------------------+")    
            cari = input("Masukkan pilihan (1/2/0): ")  
            if cari == "1":
                linkedList_controller.jump_search_id_donasi()
                skip = input("Tekan Enter untuk kembali ke menu utama")
            elif cari == '2':
                linkedList_controller.jump_search_barang_id()
                skip = input("Tekan Enter untuk kembali ke menu utama")
            elif cari == "0":
                break
            else:
                print("\n<< Input tidak valid >>")
                time.sleep(2)
        elif pilih == "0":
            print("\n<< Kembali ke menu awal donatur >>")
            break
        else:
            print("<< Input tidak valid >>")
