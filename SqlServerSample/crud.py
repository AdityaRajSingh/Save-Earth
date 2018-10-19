import pyodbc
server = 'localhost'
database = 'SampleDB'
username = 'sa'
password = 'DreamDare321'
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

print ('Inserting a new row into table')
#Insert Query
tsql = "INSERT INTO Tweets (Id, Text, Location, Time) VALUES (?,?,?,?);"
with cursor.execute(tsql, 1, 'Jake','United States', '9 PM'):
    print ('Successfuly Inserted!')

# sqlcmd -S localhost -U sa -P DreamDare321 -Q "USE SampleDB; CREATE TABLE Tweets (SerialNo INT IDENTITY(1,1) NOT NULL PRIMARY KEY, Id INT, Text NVARCHAR(50), Location NVARCHAR(100), Time NVARCHAR(50));"

#Update Query
print ('Updating Location for Jake')
tsql = "UPDATE Tweets SET Location = ? WHERE Text = ?"
with cursor.execute(tsql,'Sweden','Jake'):
    print ('Successfuly Updated!')

#Select Query
print ('Reading data from table')
tsql = "SELECT Text, Location FROM Tweets;"
with cursor.execute(tsql):
    row = cursor.fetchone()
    while row:
        print (str(row[0]) + " " + str(row[1]))
        row = cursor.fetchone()

#Delete Query
print ('Deleting user Jake')
tsql = "DELETE FROM Tweets WHERE Text = ?"
with cursor.execute(tsql,'Jake'):
    print ('Successfuly Deleted!')



