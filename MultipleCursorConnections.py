import pyodbc
import credentials  #the connection string values 


#Establishing connection
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+credentials.SERVER+';DATABASE='+credentials.DATABASE+';ENCRYPT=no;UID='+credentials.USERNAME+';PWD='+ credentials.PWD)

#
with cnxn:
    #multi-threaded connection
        #multi-threaded connection is used to execute multiple SQL commands in a single thread
        #this requires a knowledge of the order in which they cursors are executed, rollbacks, and committed
        #and how they curors affects each other threads. 
    cursor1 = cnxn.cursor()
    cursor2 = cnxn.cursor()
    
    #autocommit False by default
    print('Autocommit: ' + str(cnxn.autocommit))    #here we are printing the value of autocommit as a confirmation of the default value
    
    tsqlcommand1 = '''SELECT * INTO Application.PeopleBackup
                    FROM Application.People'''
    
    tsqlcommand2 = '''SELECT * INTO Application.CountriesBackup
                    FROM Application.Countries'''

    cursor1.execute(tsqlcommand1)   #executing the SQL command from the thread 1
    input('Press Enter to continue...')
    cursor2.execute(tsqlcommand2)   #executing the SQL command from the thread 2
    input('Press Enter to continue...')
    cursor1.commit()    #committing the changes of the thread 1, although thread 2 is not committed yet but will be affected either way because they use the same connection
    input('Press Enter to continue...')
    
'''
-- In SSMS, check the tables created in the database to verify the thread 1 and 2 were affected by the commit of thread 1
SELECT * 
FROM WideWorldImporters.sys.tables WITH(NOWAIT)
WHERE name in ('PeopleBackup','CountriesBackup')

'''