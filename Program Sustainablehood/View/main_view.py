from View import admin_view
from View import donatur_view
from View import penerima_view
import os

def main_program():
    while True:
        try:
            print("\n+--------------------------------------------------+")
            print("|            PROGRAM SUSTAINABLEHOOD               |")
            print("+--------------------------------------------------+")
            print("| [1] Admin                                        |")
            print("| [2] Donatur                                      |")
            print("| [3] Penerima                                     |")
            print("| [0] Keluar dari Program                          |")
            print("+--------------------------------------------------+")
            pilih = input("Masukkan pilihan (1/2/3/0): ")
            if pilih == "1":
                os.system("cls")
                admin_view.login_admin()
            elif pilih == "2":
                os.system("cls")
                donatur_view.menu_donatur()
            elif pilih == "3":
                os.system("cls")
                penerima_view.menu_penerima()
            elif pilih == "0":
                print("\n+------------------ Terima Kasih ------------------+")
                break
            else:
                print("<< Input tidak valid >>")
        except KeyboardInterrupt:
            print("\n<< Terjadi kesalahan >>")
        except EOFError:
            print("T\n<< Terjadi kesalahan: Kembali ke awal program >>")