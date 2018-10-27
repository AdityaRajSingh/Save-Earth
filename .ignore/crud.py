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
# sqlcmd -S tcp:tweets12.database.windows.net -U adnan-azmat -P DreamDare321 -Q "CREATE DATABASE KeepTweets;"
# sqlcmd -S tweets12.database.windows.net -U adnan-azmat -P DreamDare321 -Q "SELECT @@VERSION"
# sqlcmd -S tcp:tweets12.database.windows.net -U adnan-azmat -P DreamDare321 -Q "USE tweets; CREATE TABLE Tweets (Text NVARCHAR(280), Location NVARCHAR(100), Time NVARCHAR(50));"
# sqlcmd -S tweets123.database.windows.net -U adnan-azmat -P DreamDare321 -Q "CREATE TABLE Tweets (Text NVARCHAR(280), Location NVARCHAR(100), Time NVARCHAR(50));"
# sqlcmd -S localhost -U sa -P DreamDare321 -Q "SELECT @@VERSION"
# sqlcmd -S localhost -U sa -P DreamDare321 -Q "USE SampleDB; ALTER TABLE Tweets ALTER COLUMN Text NVARCHAR (500);"
# sqlcmd -S . -d SampleDB -E -s',' -W -Q "SELECT * FROM TableName" > /Users/adnanazmat/Desktop/Tweets.csv

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