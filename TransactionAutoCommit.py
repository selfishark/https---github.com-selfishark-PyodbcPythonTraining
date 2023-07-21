import pyodbc
import credentials  #the connection string values 


#Establishing connection
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+credentials.SERVER+';DATABASE='+credentials.DATABASE+';ENCRYPT=no;UID='+credentials.USERNAME+';PWD='+ credentials.PWD)

#
with cnxn:
    cursor = cnxn.cursor()
    #autocommit False by default
    print('Autocommit: ' + str(cnxn.autocommit))    #here we are printing the value of autocommit as a confirmation of the default value

        #create a table and populate it
    tsqlcreatetable = '''CREATE TABLE [Sales].[SpecialDeals-Copy1](
            [SpecialDealID] [int] NOT NULL,
        [StockItemID] [int] NULL,
        [CustomerID] [int] NULL,
        [BuyingGroupID] [int] NULL
        )'''
        #populate the table based on another table
    tsqlpopulatetable = '''
            INSERT INTO [Sales].[SpecialDeals-Copy1]
            SELECT [SpecialDealID],[StockItemID],[CustomerID],[BuyingGroupID]
            FROM
            [Sales].[SpecialDeals] ORDER BY DiscountPercentage DESC'''

    cursor.execute(tsqlcreatetable) #execute the create table command
    input('Press Enter to continue...') #pause the script to allow the user to check the table creation
    cursor.execute(tsqlpopulatetable)   #execute the populate table command
    input('Press Enter to continue...') #pause the script to allow the user to check the table population
    cnxn.rollback() #rollback the transaction
    input('Press Enter to continue...') #pause the script to allow the user to check the table is empty
    

    #autocommit set to True
    cnxn.autocommit=True
    print('Autocommit: ' + str(cnxn.autocommit))

    #same commands but with Autocommit set to True

    cursor.execute(tsqlcreatetable)
    input('Press Enter to continue...')
    cursor.execute(tsqlpopulatetable)
    input('Press Enter to continue...')
    cnxn.rollback() #this rollback is not necessary as the autocommit is set to True; There is nothing to rollback from.
    input('Press Enter to continue...')

    #drop the table
    tsqldroptable = 'DROP TABLE [Sales].[SpecialDeals-Copy1]'
    cursor.execute(tsqldroptable)   #the table is dropped 
    input('Press Enter to continue...')
    cnxn.rollback()     #the rollback is not necessary because the table is dropped already due to the autocommit set to True
    input('Press Enter to continue...')

    cursor.close()


# from SSMS run the following commands to check the transaction isolation levels and the locks

'''
--Check the Transaction isolation levels
SELECT sess_trans.session_id,open_transaction_count, sqltext.text 
FROM sys.dm_tran_session_transactions sess_trans 
INNER JOIN sys.dm_exec_connections conns ON conns.session_id = sess_trans.session_id
CROSS APPLY sys.dm_exec_sql_text(conns.most_recent_sql_handle) sqltext 

--Check the locks
SELECT lcks.request_session_id,lcks.resource_type, request_mode, count(*) lockCount
FROM sys.dm_tran_locks lcks
INNER JOIN sys.dm_tran_session_transactions sess_trans ON sess_trans.session_id = lcks.request_session_id
INNER JOIN sys.dm_exec_connections conns ON conns.session_id = sess_trans.session_id
CROSS APPLY sys.dm_exec_sql_text(conns.most_recent_sql_handle) sqltext 
GROUP BY request_session_id,resource_type,request_mode

--Check the tables
SELECT * 
FROM WideWorldImporters.sys.tables WITH(NOWAIT)
WHERE name = 'SpecialDeals-Copy1'

SELECT * FROM WideWorldImporters.[Sales].[SpecialDeals-Copy1]

'''