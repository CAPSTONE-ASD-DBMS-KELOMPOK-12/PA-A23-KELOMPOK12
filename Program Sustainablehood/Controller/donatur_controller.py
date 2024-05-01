from Model.database import Database
from Controller import akun_controller
from Controller import linkedList_controller
import random
import time
from prettytable import PrettyTable

donasi_list = linkedList_controller.donasi_linkedlist()
barang_list = linkedList_controller.barang_linkedlist()
objek_akun = akun_controller.AkunController()

class Donatur:
    def __init__(self):
        self.inventory = linkedList_controller.LinkedList()
        self.db = Database()
        self.mycursor = self.db.mycursor
        self.mydb = self.db.mydb

    def tambah_barang(self, data):
        try:
            query = "INSERT INTO barang (id_barang, nama_barang, jumlah_barang, kondisi_barang, jenis_barang, id_donatur) VALUES (%s, %s, %s, %s, %s, %s)"
            self.mycursor.execute(query, (data['id_barang'], data['nama_barang'], data['jumlah_barang'], data['kondisi_barang'], data['jenis_barang'], data['id_donatur']))
            self.mydb.commit()
            
            barang_list.append(data) 
            linkedList_controller.barang_list = barang_list
            self.inventory.append(data)
            print("\n<< Data barang berhasil ditambahkan >>")
            time.sleep(2)

        except Exception as e:
            print('error', e)
            time.sleep(2)

    def lihat_barang(self):
        query_select_barang = "SELECT * FROM barang"
        self.mycursor.execute(query_select_barang)
        barang_list.clear()
        for barang_data in self.mycursor.fetchall():
            barang = {
                'id_barang': barang_data[0],
                'nama_barang': barang_data[1],
                'jumlah_barang': barang_data[2],
                'kondisi_barang': barang_data[3],
                'jenis_barang': barang_data[4],
                'id_donatur': barang_data[5],
            }
            barang_list.append(barang)

        current = barang_list.head
        print("\nData Barang:")
        
        table = PrettyTable()
        table.field_names = ["ID Barang", "Nama Barang", "Jumlah Barang", "Kondisi Barang", "Jenis Barang", "ID Donatur"]
        
        while current:
            data = current.data
            table.add_row([data['id_barang'], data['nama_barang'], data['jumlah_barang'], data['kondisi_barang'], data['jenis_barang'], data['id_donatur']])
            current = current.next
        print(table)

donatur = Donatur()

def input_data_barang():
    try:
        id_barang = 'B' + str(random.randint(000, 999))
        data_baru = {}
        data_baru['id_barang'] = id_barang
        while True:
            data_baru['nama_barang'] = input("Masukkan nama barang: ").title()
            if data_baru['nama_barang'].strip():
                break
            else: 
                print("\n<< Nama barang harus diisi >>")
        while True:
            data_baru['jumlah_barang'] = int(input("Masukkan jumlah barang: "))
            if data_baru['jumlah_barang'] > 0:
                break
            else:
                print("\n<< Jumlah barang harus lebih dari 0 >>")
        while True:
            data_baru['kondisi_barang'] = input("Masukkan kondisi barang (baik/rusak): ").title()
            if data_baru['kondisi_barang'].strip():
                break
            else: 
                print("\n<< Kondisi barang harus diisi >>")
        while True:
            data_baru['jenis_barang'] = input("Masukkan jenis barang: ").title()
            if data_baru['jenis_barang'].strip():
                break
            else: 
                print("\n<< Jenis barang harus diisi >>")
        while True:
            data_baru['id_donatur'] = input("Masukkan ID Donatur: ")
            query = "SELECT * FROM barang WHERE id_donatur = %s"
            donatur.mycursor.execute(query, (data_baru['id_donatur'],))
            result = donatur.mycursor.fetchone()
            if not result:
                print("\n<< ID Donatur tidak valid >>")
            else:
                break
        return data_baru
    except Exception as e:
        print("Terjadi kesalahan:", e)
        return None
    except KeyboardInterrupt:
        print("Salah input")



    


    