import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}' 
                                r'DBQ=C:\Users\LENOVO 305\Database1.accdb;')

    print("Database is Connected")

except pyodbc.Error:
    print("Database is NOT connected")
