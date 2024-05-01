from Model.database import Database
import random
import time

class AkunController():
    def __init__(self):
        self.db = Database()
        self.mycursor = self.db.mycursor
        self.mydb = self.db.mydb

    def registrasi_donatur(self, id_donatur, nama, email, no_hp, alamat, username, password):
        id_donatur = 'D' + str(random.randint(1000, 9999))
        try:
            self.mycursor.execute('''INSERT INTO donatur (ID_Donatur, Nama_Donatur, Email, NO_Telpon, Alamat, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s)''', (id_donatur, nama, email, no_hp, alamat, username, password))
            self.mydb.commit()
            print(f"\n<< {nama} berhasil registrasi >>")
            return True
        except Exception as e:
            print(f"\n<< Registrasi gagal: {e}>>")
            return False

    def login_donatur(self, username, password):
        self.mycursor.execute('SELECT * FROM donatur WHERE username = %s AND password = %s', (username, password))
        result = self.mycursor.fetchone()
        if result:
            print(f"\n<< {username} berhasil login sebagai donatur >>")
            time.sleep(2)
            from View import donatur_view
            donatur_view.menu_utama_donatur()
        else:
            print("\n<< Password salah >>")

    def registrasi_penerima(self, id_penerima, nama, email, no_hp, alamat, pekerjaan, gaji, kebutuhan, username, password):
        id_penerima = 'P' + str(random.randint(1000, 9999))
        try:
            self.mycursor.execute('''INSERT INTO penerima (ID_Penerima, Nama_Penerima, Email, Nomor_Telpon, Alamat, Pekerjaan, Gaji, username, password, Kebutuhan) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''', (id_penerima, nama, email, no_hp, alamat, pekerjaan, gaji, username, password, kebutuhan))
            self.mydb.commit()
            print(f"\n<< {nama} berhasil registrasi >>")
            return True
        except Exception as e:
            print(f"\n<< Registrasi gagal: {e}>>")
            return False

    def login_penerima(self, username, password):
        self.mycursor.execute('''SELECT * FROM penerima WHERE username = %s AND password = %s''', (username, password))
        result = self.mycursor.fetchone()
        if result:
            print(f"\n<< {username} berhasil login sebagai donatur >>")
            time.sleep(2)
            from View import penerima_view
            penerima_view.menu_utama_penerima()
        else:
            print("\n<< Password salah >>")

    def login_admin(self, username, password):
        try:
            self.mycursor.execute('SELECT * FROM admin WHERE username = %s AND password = %s', (username, password))
            result = self.mycursor.fetchone()
            if result:
                print(f"\n<< {username} berhasil login sebagai admin >>")
                time.sleep(2)
                from View import admin_view
                admin_view.menu_admin()
            else:
                print("\n<< Username atau password admin salah >>")
        except Exception as e:
            print(f"\n<< Login admin gagal: {e} >>")


