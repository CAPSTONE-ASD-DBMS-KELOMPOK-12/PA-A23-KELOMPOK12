from Controller import admin_controller
from Controller import linkedList_controller
from Controller import donatur_controller
from Controller import akun_controller

import time
import os

objek_akun = akun_controller.AkunController()
objek_admin = admin_controller.Admin()
objek_linkedlist = linkedList_controller.LinkedList()
objek_donatur = donatur_controller.Donatur()

def login_admin():
    while True:
        print("\n+--------------------------------------------------+")
        print("|                  LOGIN ADMIN                     |")
        print("+--------------------------------------------------+")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        objek_akun.login_admin(username, password)
        break

def menu_admin():
    while True:
        print("\n+--------------------------------------------------+")
        print("|            PROGRAM SUSTAINABLEHOOD               |")
        print("|                MENU UTAMA ADMIN                  |")
        print("+--------------------------------------------------+")
        print("| [1] Buat Donasi                                  |")
        print("| [2] Tampilkan Daftar Donasi dan Barang           |")
        print("| [3] Perbarui Donasi                              |")
        print("| [4] Hapus Akun Penerima                          |")
        print("| [5] Sort Daftar Donasi dan Barang                |")
        print("| [6] Search Daftar Donasi dan Barang              |")
        print("| [0] Kembali                                      |")
        print("+--------------------------------------------------+")
        pilih = input("Masukkan pilihan (1/2/3/4/5/6/0): ")
        if pilih == "1":
            data_baru = admin_controller.input_data()
            objek_admin.tambah_donasi(data_baru)            
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
            objek_admin.update_donasi() 
        elif pilih == "4":
            os.system("cls")
            target_id = input("Masukkan ID_Penerima yang ingin dihapus: ")
            objek_admin.hapus_penerima(target_id)            
        elif pilih == "5":
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
        elif pilih == "6":
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
            print("\n<< Kembali ke menu awal program >>")
            break
        else:
            print("<< Input tidak valid >>")
