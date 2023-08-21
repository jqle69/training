import pyodbc
from tkinter import messagebox

#Define server and database name
server = 'MSI'
database = 'MyDb'

class DAL:

    def __init__(self):
        #define connection string
        self.conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
                      SERVER=' + server + ';\
                      DATABASE=' + database + ';\
                      Trusted_Connection=yes;')
        #create cursor
        self.cursor = self.conn.cursor()

    def save_dictation(self, dicttext):
        try:
            self.cursor.execute("INSERT INTO dbo.dictations (dicttext) values (?)", (dicttext))
            self.conn.commit()

        except pyodbc.Error as e:
            messagebox.showerror(title="Error", message=f"Database Error: {e}")

    def update_dictation(self, dictid, dicttext):
        try:
            self.cursor.execute("UPDATE dbo.dictations SET dicttext=? WHERE dictid=?", (dicttext, dictid))
            self.conn.commit()

        except pyodbc.Error as e:
            messagebox.showerror(title="Error", message=f"Database Error: {e}")

    def delete_dictation(self,  dictid):
        try:
            self.cursor.execute("DELETE FROM dictations WHERE ", (dictid))
            self.conn.commit()

        except pyodbc.Error as e:
            messagebox.showerror(title="Error", message=f"Database Error: {e}")

    def __del__(self):
        self.cursor.close()
        self.conn.close()