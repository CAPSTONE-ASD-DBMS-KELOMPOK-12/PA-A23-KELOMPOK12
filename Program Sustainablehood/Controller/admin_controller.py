from Model.database import Database
from prettytable import PrettyTable
from Controller import linkedList_controller
from datetime import datetime
import random
import time

donasi_list = linkedList_controller.donasi_linkedlist()
barang_list = linkedList_controller.barang_linkedlist()
penerima_list = linkedList_controller.penerima_linkedlist()

class Admin:
    def __init__(self):
        self.inventory = linkedList_controller.LinkedList()
        self.db = Database()
        self.mycursor = self.db.mycursor
        self.mydb = self.db.mydb

    # Fungsi untuk menambahkan data ke linked list dan database
    def tambah_donasi(self, data):
        try:
            # Menambahkan data ke database
            query = "INSERT INTO donasi (ID_Donasi, Status_donasi, jumlah_barang, Tanggal_Donasi, id_barang, ID_Penerima, id_donatur, ID_Admin) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            self.mycursor.execute(query, (data['ID_Donasi'], data['Status_donasi'], data['jumlah_barang'], data['Tanggal_Donasi'], data['id_barang'], data['ID_Penerima'], data['id_donatur'], data['ID_Admin']))
            self.mydb.commit()

            # Update jumlah barang di database
            query_select_barang = "SELECT jumlah_barang FROM barang WHERE id_barang = %s"
            self.mycursor.execute(query_select_barang, (data['id_barang'],))
            jumlah_barang_sekarang = self.mycursor.fetchone()[0]
            jumlah_barang_terbaru = jumlah_barang_sekarang - data['jumlah_barang']

            query_update_barang = "UPDATE barang SET jumlah_barang = %s WHERE id_barang = %s"
            self.mycursor.execute(query_update_barang, (jumlah_barang_terbaru, data['id_barang']))
            self.mydb.commit()
            
            # Menambahkan data ke linked list
            donasi_list.append(data)
            linkedList_controller.donasi_list = donasi_list
            self.inventory.append(data)
            print("\n<< Data berhasil ditambahkan >>")

            time.sleep(2)
        except Exception as e:
            print('error', e)
            time.sleep(2.5)

    # Fungsi untuk membaca (read) data dari linked list
    def lihat_donasi(self):
        current = donasi_list.head
        print("\nData Donasi:")
        
        # Inisialisasi PrettyTable
        table = PrettyTable()
        table.field_names = ["ID Donasi", "Status Donasi", "Jumlah Barang", "Tanggal Donasi", "ID Barang", "ID Penerima", "ID Donatur", "ID Admin"]
        
        # Menambahkan baris-baris data ke PrettyTable
        while current:
            data = current.data
            table.add_row([data['ID_Donasi'], data['Status_donasi'], data['jumlah_barang'], data['Tanggal_Donasi'], data['id_barang'], data['ID_Penerima'], data['id_donatur'], data['ID_Admin']])
            current = current.next

        # Cetak PrettyTable
        print(table)

    # Fungsi untuk memperbarui (update) data dalam linked list dan database
    def update_donasi(self):
        try:
            id_donasi = input("\nMasukkan ID Donasi yang akan diupdate: ")

            # Cek apakah donasi dengan ID tersebut ada dalam database
            self.mycursor.execute("SELECT * FROM donasi WHERE ID_Donasi = %s", (id_donasi,))
            donasi = self.mycursor.fetchone()
            if not donasi:
                print("Donasi dengan ID tersebut tidak ditemukan.")
                return

            tabel = PrettyTable()
            tabel.field_names = ['Detail Donasi']
            tabel.align['Detail Donasi'] = 'l'
            tabel.add_row([f'[1] Status Donasi  : {donasi[1]}'])
            tabel.add_row([f'[2] Jumlah Barang  : {donasi[2]}'])
            tabel.add_row([f'[3] Tanggal Donasi : {donasi[3]}'])
            tabel.add_row([f'[4] ID Barang      : {donasi[4]}'])
            tabel.add_row([f'[5] ID Penerima    : {donasi[5]}'])
            tabel.add_row([f'[6] ID Donatur     : {donasi[6]}'])
            tabel.add_row([f'[7] ID Admin       : {donasi[7]}'])
            print()
            print(tabel)
            field_to_update = input("Pilih nomor field yang ingin diupdate (1-7): ")
            new_value = input("\nMasukkan nilai baru: ")

            # Update data donasi dalam database
            fields = ['Status_donasi', 'jumlah_barang', 'Tanggal_Donasi', 'id_barang', 'ID_Penerima', 'id_donatur', 'ID_Admin']
            field = fields[int(field_to_update) - 1]
            query = f"UPDATE donasi SET {field} = %s WHERE ID_Donasi = %s"
            self.mycursor.execute(query, (new_value, id_donasi))
            self.mydb.commit()

            # Perbarui juga data dalam linked list
            current = donasi_list.head
            while current:
                if current.data['ID_Donasi'] == id_donasi:
                    current.data[field] = new_value
                    break
                current = current.next
            linkedList_controller.donasi_list = donasi_list

            print("<< Data donasi berhasil diupdate >>")
            time.sleep(2)
        except Exception as e:
            print("Error", e)
            time.sleep(2)
        except KeyboardInterrupt:
            print("error")
            time.sleep(2)

    # Fungsi untuk menghapus data dari linked list dan database
    def hapus_penerima(self, target_id):
        current = penerima_list.head
        prev = None
        while current:
            if current.data['ID_Penerima'] == target_id:
                # Menghapus data dari database
                # mycursor = self.mycursor.mydb.mycursor()
                query = "DELETE FROM penerima WHERE ID_Penerima = %s"
                self.mycursor.execute(query, (target_id,))
                self.mydb.commit()
                # Menghapus data dari linked list
                if prev:
                    prev.next = current.next
                else:
                    donasi_list.head = current.next
                print("\n<< Data akun penerima berhasil dihapus >>")
                time.sleep(2)
                return
            prev = current
            current = current.next
        print("\n<< Data dengan ID Penerima tersebut tidak ditemukan >>")
        time.sleep(2)

    def update_kebutuhan(self, username, password):
        try:
            self.mycursor.execute('''SELECT * FROM penerima WHERE username = %s AND password = %s''', (username, password))
            if self.mycursor.fetchone() is None:
                print("Username tidak ditemukan di database.")
                return

            kebutuhan_baru = input("\nMasukkan kebutuhan baru: ")
            query = "UPDATE penerima SET Kebutuhan = %s WHERE username = %s"
            self.mycursor.execute(query, (kebutuhan_baru, username))
            self.mydb.commit()
            if self.mycursor.rowcount == 0:
                print("\n<< Pembaruan gagal >>")
            else:
                print("\n<< Kebutuhan penerima berhasil diperbarui >>")
        except Exception as e:
            print("Error saat update ke database:", e)

admin = Admin()

def input_data():
    id_donasi = 'D' + str(random.randint(000, 999))
    try:
        data_baru = {}
        data_baru['ID_Donasi'] = id_donasi
        while True:
            data_baru['Status_donasi'] = input("\nMasukkan status donasi (pending/berhasil/gagal): ").title()
            if data_baru['Status_donasi'].strip():
                break
            else: 
                print("\n<< Status donasi harus diisi >>")
        while True:
            data_baru['jumlah_barang'] = int(input("Masukkan jumlah barang: "))
            if data_baru['jumlah_barang'] > 0:
                break
            else:
                print("\n<< Jumlah barang harus lebih dari 0 >>")
        while True:
            data_baru['Tanggal_Donasi'] = input("Masukkan tanggal donasi (YYYY-MM-DD): ")
            if datetime.strptime(data_baru['Tanggal_Donasi'], '%Y-%m-%d'):
                break
            else:
                print("\n<< Format tanggal tidak sesuai >>")
        while True:
            data_baru['id_barang'] = input("Masukkan ID Barang: ")
            query = "SELECT * FROM barang WHERE id_barang = %s"
            admin.mycursor.execute(query, (data_baru['id_barang'],))
            result = admin.mycursor.fetchone()
            if result is None:
                print("\n<< ID Barang tidak valid >>")
            else:
                break
        while True:
            data_baru['ID_Penerima'] = input("Masukkan ID Penerima: ")
            query = "SELECT * FROM penerima WHERE ID_Penerima = %s"
            admin.mycursor.execute(query, (data_baru['ID_Penerima'],))
            result = admin.mycursor.fetchone()
            if result is None:
                print("\n<< ID Penerima tidak valid >>")
            else:
                break
        while True:
            data_baru['id_donatur'] = input("Masukkan ID Donatur: ")
            query = "SELECT * FROM barang WHERE id_donatur = %s"
            admin.mycursor.execute(query, (data_baru['id_donatur'],))
            result = admin.mycursor.fetchone()
            if result is None:
                print("\n<< ID Donatur tidak valid >>")
            else:
                break
        while True:
            data_baru['ID_Admin'] = input("Masukkan ID Admin: ")
            query = "SELECT * FROM admin WHERE ID_Admin = %s"
            admin.mycursor.execute(query, (data_baru['ID_Admin'],))
            result = admin.mycursor.fetchone()
            if result is None:
                print("\n<< ID Admin tidak valid >>")
            else:
                break
        return data_baru
    except KeyboardInterrupt:
        print('Terjadi kesalahan')
