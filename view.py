import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}'
                                r'DBQ=C:\Users\LENOVO 305\Database1.accdb;')

    database = connection.cursor()
    database.execute('select * from Table1')
    for x in database.fetchall():
        print(x)
    print('Database is viewed.')
except pyodbc.Error:
    print("Database is NOT connected")
