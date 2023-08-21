import pyodbc as odbc 
import pandas as pd
from datetime import datetime

SERVER_NAME = "MSI"
DATABASE_NAME = "AdventureWorksDW2019"

#ODBC Drive 17 for SQL Server
conn_ODBC = f"Driver=ODBC Driver 17 for SQL Server;Server={SERVER_NAME};Database={DATABASE_NAME};Trusted_Connection=yes;"
#OleDB connection to SQL Server
conn_OLE = f"Provider=SQLNCLI11;Server={SERVER_NAME};Database={DATABASE_NAME};Trusted_Connection=yes;"

conn = odbc.connect(conn_ODBC)

query = pd.read_sql_query("SELECT * FROM dbo.DimDate", conn)

df = pd.DataFrame()

df.to_csv("C:\\Users\\17147\\Desktop\\CMPR114\\sqlserver\\sql"+datetime.now().strftime('%Y%m%d')+".csv", index=False)
