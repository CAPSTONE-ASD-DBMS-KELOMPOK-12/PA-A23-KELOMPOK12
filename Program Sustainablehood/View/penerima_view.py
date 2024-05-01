from Controller import akun_controller
from Controller import admin_controller
from Controller import linkedList_controller
from Controller import donatur_controller
import os
import time

objek_akun = akun_controller.AkunController()
objek_admin = admin_controller.Admin()
objek_linkedlist = linkedList_controller.LinkedList()
objek_donatur = donatur_controller.Donatur()


def menu_penerima():
    while True:
        print("\n+--------------------------------------------------+")
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
                print("\n+--------------------------------------------------+")
                print("|                 LOGIN PENERIMA                   |")
                print("+--------------------------------------------------+")
                username = input("Masukkan username: ")
                password = input("Masukkan password: ")
                objek_akun.login_penerima(username, password)
                break
        elif pilih == "2":
            print("\n+--------------------------------------------------+")
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

def menu_utama_penerima(username, password):
    while True:
        print("""
+--------------------------------------------------+
|            PROGRAM SUSTAINABLEHOOD               |
|              MENU UTAMA PENERIMA                 |
+--------------------------------------------------+
| [1] Perbarui Permintaan Kebutuhan                |
| [2] Tampilkan Daftar Donasi dan Barang           |
| [3] Urutkan Daftar Donasi dan Barang             |
| [4] Cari Daftar Donasi dan Barang                |
| [0] Kembali                                      |
+--------------------------------------------------+""")
        pilih = input("Masukkan pilihan (1/2/3/4/0): ")
        if pilih == "1":
            objek_admin.update_kebutuhan(username, password)
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
            elif lihat == "0":
                break
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
