import pyodbc
import credentials  #the connection string values 

## NOTE: there is n better way to trap these errors than knowing what you are after.

#Establishing connection
#Stop SQL Server Service, manually to create a connection issue to test the error handling 
print('Establishing Connection...')
try:
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+credentials.SERVER+';DATABASE='+credentials.DATABASE+';ENCRYPT=no; APP=PyodbcPythonTraining; UID='+credentials.USERNAME+';PWD='+ credentials.PWD)
except pyodbc.OperationalError as pyodbcerror:  #trap the error here as an operational error    
        print('Error: ' + str(pyodbcerror))     #print the error message
        
input('Press Enter to continue...') #pause to check on the next error handling block

#Start SQL Server Service Manually 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+credentials.SERVER+';DATABASE='+credentials.DATABASE+';ENCRYPT=no; APP=PyodbcPythonTraining; UID='+credentials.USERNAME+';PWD='+ credentials.PWD)
cursor = cnxn.cursor()

#Disconnect
#Stop SQL Server while the WAITFOR is running for 30 seconds to test the error handling
print('Disconnect Example...')
tsql = "WAITFOR DELAY '00:00:30';"

try:
        cursor.execute(tsql)
        rows = cursor.fetchall()
except pyodbc.Error as pyodbcerror: #trap the error here as a generic error
        print('Error: ' + str(pyodbcerror)) #print the error message
        cnxn.close()

input('Press Enter to continue...')

#Start SQL Server service manually
connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+credentials.SERVER+';DATABASE='+credentials.DATABASE+';ENCRYPT=no; APP=PyodbcPythonTraining; UID='+credentials.USERNAME+';PWD='+ credentials.PWD)
cursor = connection.cursor()

#Integrity 
    #The following query will fail because the CountryID is a primary key and cannot be duplicated
print('Integrity Example...')
tsql = '''UPDATE [Application].[Countries]
        SET [CountryID] = (SELECT CountryID FROM [Application].[Countries]
        WHERE CountryName='Costa Rica')
        WHERE CountryName='Canada';'''  #Incorrect syntax near the keyword 'WHERE'

try:
        cursor.execute(tsql)
        rows = cursor.fetchall()
except pyodbc.IntegrityError as pyodbcerror:   #Incorrect syntax near the keyword 'WHERE'is expected to create a duplicate error in pyodbc
        print('Error: ' + str(pyodbcerror))    #print the error message

input('Press Enter to continue...')

#Data Error
print('Data Error Example...')
tsql = 'SELECT cast(100000000000000000000 AS int)'  #Arithmetic overflow error converting expression to data type int.

try:
        cursor.execute(tsql)
        rows = cursor.fetchall()
except pyodbc.DataError as pyodbcerror: #Arithmetic overflow error converting expression to data type int. is expected to create a data error in pyodbc
        print('Error: ' + str(pyodbcerror))

input('Press Enter to continue...')



connection.close()

