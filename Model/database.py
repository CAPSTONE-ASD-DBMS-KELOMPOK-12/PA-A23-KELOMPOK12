import mysql.connector

class Database:
    def __init__(self):
            self.mydb = mysql.connector.connect(
                host = "localhost",
                user ="root",
                password = "",
                database = "donasi"
            )

            self.mycursor = self.mydb.cursor()
        
    
    







