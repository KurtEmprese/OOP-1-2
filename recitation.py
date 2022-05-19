import pyodbc

try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\MSI\Documents\Database01.accdb;')
    print("Database is Connected")

    database = connect.cursor()

    database.execute("INSERT INTO Table1 (ID, FullName, Age, Address, Birthdate, SemGrade) VALUES(?, ?, ?, ?, ?, ?)", (11, "Kurt Ashley S. Emprese", 18, "Cavite", "21/06/2003", 95))
    database.commit()

except pyodbc.Error:
    print("Error in Connection")