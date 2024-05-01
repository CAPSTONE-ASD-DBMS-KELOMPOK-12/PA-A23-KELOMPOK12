from Model.database import Database
from datetime import datetime
from prettytable import PrettyTable

mydb = Database()
mydb = Database().mydb

# Node class untuk linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked list class
class LinkedList:
    def __init__(self):
        self.head = None

    # Menambahkan node baru ke linked list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def clear(self):
        self.head = None

    # Cetak isi linked list
    def display(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

# Mengambil data dari tabel donasi dan menyimpannya dalam linked list
def donasi_linkedlist():
    linked_list = LinkedList()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM donasi")
    result = cursor.fetchall()
    linked_list.clear()
    for row in result:
        data = {
            'ID_Donasi': row[0],
            'Status_donasi': row[1],
            'jumlah_barang': row[2],
            'Tanggal_Donasi': row[3],
            'id_barang': row[4],
            'ID_Penerima': row[5],
            'id_donatur': row[6],
            'ID_Admin': row[7]
        }
        linked_list.append(data)
    return linked_list

# Mengambil data dari tabel barang dan menyimpannya dalam linked list
def barang_linkedlist():
    linked_list = LinkedList()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM barang")
    result = cursor.fetchall()
    linked_list.clear()
    for row in result:
        data = {
            'id_barang': row[0],
            'nama_barang': row[1],
            'jumlah_barang': row[2],
            'kondisi_barang': row[3],
            'jenis_barang': row[4],
            'id_donatur': row[5]
        }
        linked_list.append(data)
    return linked_list

def penerima_linkedlist():
    linked_list = LinkedList()  # Membuat objek linked list baru
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM penerima")
    result = cursor.fetchall()
    
    for row in result:
        data = {
            'Nama_Penerima': row[0],
            'ID_Penerima': row[1],
            'Nomor_Telpon': row[2],
            'Email': row[3],
            'Pekerjaan': row[4],
            'Gaji': row[5],
            'Alamat': row[6],
            'username': row[7],
            'password': row[8],
            'Kebutuhan': row[9]
        }
        linked_list.append(data)
    
    return linked_list

donasi_list = donasi_linkedlist()

# Fungsi untuk melakukan jump search pada linked list donasi berdasarkan ID Donasi
def jump_search_donasi(head, target_id):
    current = head
    while current:
        if current.data['ID_Donasi'] == target_id:
            return current.data  # Mengembalikan data jika ditemukan
        current = current.next
    return None  # Mengembalikan None jika data tidak ditemukan

# jump search donasi berdasarkan ID Donasi
def jump_search_id_donasi():
    # Mencari data dengan ID_Donasi menggunakan jump search
    target_id = input("\nMasukkan ID Donasi yang ingin dicari: ")
    result = jump_search_donasi(donasi_list.head, target_id)
    if result:
        print("Data ditemukan:")
        # Output dalam bentuk pretty table
        table = PrettyTable()
        table.field_names = ["ID_Donasi", "Status_donasi", "jumlah_barang", "Tanggal_Donasi", "id_barang", "ID_Penerima", "id_donatur", "ID_Admin"]
        table.add_row([result['ID_Donasi'], result['Status_donasi'], result['jumlah_barang'], result['Tanggal_Donasi'], result['id_barang'], result['ID_Penerima'], result['id_donatur'], result['ID_Admin']])
        print(table)
    else:
        print("Data tidak ditemukan.")

barang_list = barang_linkedlist()

# jump search tabel barang berdasarkan ID Barang
def jumpSearchBarangID(head, target_id):
    current = head
    while current:
        if current.data['id_barang'] == target_id:
            return current.data  # Mengembalikan data jika ditemukan
        current = current.next
    return None  # Mengembalikan None jika data tidak ditemukan

def jump_search_barang_id():
    # Pencarian dengan menggunakan Jump Search
    target_id = input("Masukkan ID Barang yang ingin dicari: ")
    result = jumpSearchBarangID(barang_list.head, target_id)
    if result:
        print("Barang ditemukan:")
        table = PrettyTable()
        table.field_names = ["id_barang", "nama_barang", "jumlah_barang", "kondisi_barang", "jenis_barang", "id_donatur"]
        table.add_row([result['id_barang'], result['nama_barang'], result['jumlah_barang'], result['kondisi_barang'], result['jenis_barang'], result['id_donatur']])
        print(table)
    else:
        print("Barang dengan ID", target_id, "tidak ditemukan.")

def quickSortDonasiAscending(data):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]

        # Konversi tanggal dari string ke objek datetime.date
        pivot_date = datetime.strptime(str(pivot['Tanggal_Donasi']), '%Y-%m-%d').date()

        less_than_pivot = [x for x in data[1:] if datetime.strptime(str(x['Tanggal_Donasi']), '%Y-%m-%d').date() <= pivot_date]
        greater_than_pivot = [x for x in data[1:] if datetime.strptime(str(x['Tanggal_Donasi']), '%Y-%m-%d').date() > pivot_date]

        return quickSortDonasiAscending(less_than_pivot) + [pivot] + quickSortDonasiAscending(greater_than_pivot)


donasi_list = donasi_linkedlist()

# Fungsi untuk melakukan pengurutan data donasi berdasarkan Tanggal Donasi
def quick_sort_donasi_ascending():
    # Ubah LinkedList menjadi list
    list_data = []
    current = donasi_list.head
    while current:
        list_data.append(current.data)
        current = current.next
    
    sorted_donasi_list = quickSortDonasiAscending(list_data)
    print("\nData donasi setelah diurutkan berdasarkan tanggal donasi terlama:")
    table = PrettyTable()
    table.title = "Daftar Donasi Berdasarkan Tanggal Terlama"
    table.field_names = ["ID Donasi", "Status Donasi", "Jumlah Barang", "Tanggal Donasi", "ID Barang", "ID Penerima", "ID Donatur", "ID Admin"]
    for donasi in sorted_donasi_list:
        table.add_row([donasi['ID_Donasi'], donasi['Status_donasi'], donasi['jumlah_barang'], donasi['Tanggal_Donasi'], donasi['id_barang'], donasi['ID_Penerima'], donasi['id_donatur'], donasi['ID_Admin']])
    print(table)

def quickSortDonasiDescending(data):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]

        # Konversi tanggal dari string ke objek datetime.date
        pivot_date = datetime.strptime(str(pivot['Tanggal_Donasi']), '%Y-%m-%d').date()

        less_than_pivot = [x for x in data[1:] if datetime.strptime(str(x['Tanggal_Donasi']), '%Y-%m-%d').date() >= pivot_date]
        greater_than_pivot = [x for x in data[1:] if datetime.strptime(str(x['Tanggal_Donasi']), '%Y-%m-%d').date() < pivot_date]

        return quickSortDonasiDescending(less_than_pivot) + [pivot] + quickSortDonasiDescending(greater_than_pivot)

def quick_sort_donasi_descending():
    # Ubah LinkedList menjadi list
    list_data = []
    current = donasi_list.head
    while current:
        list_data.append(current.data)
        current = current.next
    
    sorted_donasi_list = quickSortDonasiDescending(list_data)
    print("\nData donasi setelah diurutkan berdasarkan tanggal donasi terbaru:")
    table = PrettyTable()
    table.title = "Daftar Donasi Berdasarkan Tanggal Terbaru"
    table.field_names = ["ID Donasi", "Status Donasi", "Jumlah Barang", "Tanggal Donasi", "ID Barang", "ID Penerima", "ID Donatur", "ID Admin"]
    for donasi in sorted_donasi_list:
        table.add_row([donasi['ID_Donasi'], donasi['Status_donasi'], donasi['jumlah_barang'], donasi['Tanggal_Donasi'], donasi['id_barang'], donasi['ID_Penerima'], donasi['id_donatur'], donasi['ID_Admin']])
    print(table)

def quickSortBarangAscending(data):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]

        # Ambil nama barang dari pivot
        pivot_name = pivot['nama_barang']

        # Pisahkan data menjadi dua bagian: yang kurang dari pivot dan yang lebih besar dari pivot
        less_than_pivot = []
        greater_than_pivot = []
        for x in data[1:]:
            if x['nama_barang'] <= pivot_name:
                less_than_pivot.append(x)
            else:
                greater_than_pivot.append(x)

        # Rekursi untuk kedua bagian dan gabungkan dengan pivot
        return quickSortBarangAscending(less_than_pivot) + [pivot] + quickSortBarangAscending(greater_than_pivot)

# Fungsi untuk melakukan pengurutan data barang berdasarkan Nama Barang
def quick_sort_barang_ascending():
    # Ubah LinkedList menjadi list
    list_data = []
    current = barang_list.head
    while current:
        list_data.append(current.data)
        current = current.next
    
    sorted_barang_list = quickSortBarangAscending(list_data)
    print("\nData barang setelah diurutkan berdasarkan nama barang A-Z:")
    table = PrettyTable()
    table.title = "Daftar Barang Berdasarkan Huruf A-Z"
    table.field_names = ["ID Barang", "Nama Barang", "Jumlah Barang", "Kondisi Barang", "Jenis Barang", "ID Donatur"]
    for barang in sorted_barang_list:
        table.add_row([barang['id_barang'], barang['nama_barang'], barang['jumlah_barang'], barang['kondisi_barang'], barang['jenis_barang'], barang['id_donatur']])
    print(table)

def quickSortBarangDescending(data):
    if len(data) <= 1:
        return data
    else:
        pivot = data[0]

        # Ambil nama barang dari pivot
        pivot_name = pivot['nama_barang']

        # Pisahkan data menjadi dua bagian: yang kurang dari pivot dan yang lebih besar dari pivot
        less_than_pivot = []
        greater_than_pivot = []
        for x in data[1:]:
            if x['nama_barang'] >= pivot_name:  # Perubahan disini, dari <= menjadi >=
                less_than_pivot.append(x)
            else:
                greater_than_pivot.append(x)

        # Rekursi untuk kedua bagian dan gabungkan dengan pivot
        return quickSortBarangDescending(less_than_pivot) + [pivot] + quickSortBarangDescending(greater_than_pivot)

# Fungsi untuk melakukan pengurutan data barang berdasarkan Nama Barang secara descending
def quick_sort_barang_descending():
    # Ubah LinkedList menjadi list
    list_data = []
    current = barang_list.head
    while current:
        list_data.append(current.data)
        current = current.next
    
    sorted_barang_list = quickSortBarangDescending(list_data)
    print("\nData barang setelah diurutkan berdasarkan nama barang Z-A:")
    table = PrettyTable()
    table.title = "Daftar Barang Berdasarkan Huruf Z-A"
    table.field_names = ["ID Barang", "Nama Barang", "Jumlah Barang", "Kondisi Barang", "Jenis Barang", "ID Donatur"]
    for barang in sorted_barang_list:
        table.add_row([barang['id_barang'], barang['nama_barang'], barang['jumlah_barang'], barang['kondisi_barang'], barang['jenis_barang'], barang['id_donatur']])
    print(table)