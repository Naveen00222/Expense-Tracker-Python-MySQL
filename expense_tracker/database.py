import mysql.connector
from config import DB_HOST, DB_USER,DB_PASSWORD,DB_NAME

class DatabaseManager:
       def __init__(self):
             #  to establish the connection to sql
             self.conn = mysql.connector.connect(
                    host = DB_HOST,
                    user = DB_USER,
                    password = DB_PASSWORD,
                    database = DB_NAME
             )
             self.cursor = self.conn.cursor()
        
       def insert_expense(self,amount,category,date,note):
              query = "INSERT INTO expenses (amount, category, date,note)VALUES (%s, %s ,%s ,%s)"
              values = (amount, category, date, note)
              self.cursor.execute(query,values)
              self.conn.commit()

       def fetch_all_expenses(self):
              self.cursor.execute("SELECT * FROM expenses")     
              return self.cursor.fetchall()

       def close(self):
              self.cursor.close()
              self.conn.close()         

