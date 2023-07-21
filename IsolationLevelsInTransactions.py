import pyodbc
import credentials  #the connection string values 


#Establishing connection
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+credentials.SERVER+';DATABASE='+credentials.DATABASE+';ENCRYPT=no; APP=PyodbcPythonTraining; UID='+credentials.USERNAME+';PWD='+ credentials.PWD)

#
with cnxn:
    cursor = cnxn.cursor()
    
    #query with SQL Server default isolation level
    tsqlquery = '''SELECT TOP 10 * FROM [Sales].[Invoices]''' #run the query to observe the isolation level
    cursor.execute(tsqlquery)
    cursor.commit()
    input('Press Enter to continue...') #pause execution and check the isolation level in the database

    #change the isolation level through pyodbc
    cnxn.set_attr(pyodbc.SQL_ATTR_TXN_ISOLATION, pyodbc.SQL_TXN_REPEATABLE_READ)    #TXN_REPEATABLE_READ is the specified isolation level
    cursor.execute(tsqlquery)   #run the query to observe the isolation level
    cursor.commit()
    input('Press Enter to continue...') #pause execution and check the isolation level in the database

    #enable the isolation level through SQL
        #SNAPSHOT is the specified isolation level encapsulated in the SQL query, read by the Database directly
    cnxn.autocommit=True    #ALTERING a DATABASE is only possible if autocommit is set to True because SQL Server will not allow any other transaction with more commands in it
    tsqlenablenewlevel = '''ALTER DATABASE [WideWorldImporters] 
                    SET ALLOW_SNAPSHOT_ISOLATION ON'''  #SNAPSHOT is turned ON here because this DB does not have this isolation level enabled by default
    cursor.execute(tsqlenablenewlevel)

    #set the connexion to use this new isolation level
    cnxn.autocommit=False   #falling back to the default to controll the other transactions
    tsqlsetnewlevel = '''SET TRANSACTION ISOLATION LEVEL SNAPSHOT'''    #explicitly set the isolation level to SNAPSHOT so the rest of the transactions uses it instead, despite SNAPSHOT not supported by pyodbc (hence its encapsulation in the SQL query)
    cursor.execute(tsqlsetnewlevel) #run the query to observe the isolation level
    cursor.commit()
    cursor.execute(tsqlquery)   #run the previous query to observe the isolation level
    cursor.commit()
    input('Press Enter to continue...') #pause execution and check the isolation level in the database

    cnxn.close()        


# Use this SQL query to observe the isolation level
'''
SELECT session_id,[program_name],
CASE transaction_isolation_level 
WHEN 0 THEN 'Unspecified' 
WHEN 1 THEN 'ReadUncommitted' 
WHEN 2 THEN 'ReadCommitted' 
WHEN 3 THEN 'Repeatable' 
WHEN 4 THEN 'Serializable' 
WHEN 5 THEN 'Snapshot' END AS TRANSACTION_ISOLATION_LEVEL 
FROM sys.dm_exec_sessions 
WHERE [program_name] LIKE 'Pluralsight%';

'''
