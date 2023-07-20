
###
#APPROACH 1: Batching with Temp Tables
###
#1 create the SP that will use the @TVP

'''
USE [WideWorldImporters]
GO

SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

-- create the SP that will use the @TVP
CREATE OR ALTER PROCEDURE [Website].[GetItemNameAndRetailPrice]
@OrderLines Website.OrderLineList READONLY 	-- @TVPs are READONLY in SQL based; @OrderLines is based on a user-defined OderlineList
WITH EXECUTE AS OWNER
AS
BEGIN	-- Passes the values in the TVP @OrderLines and join it to the table StockItems
    SELECT ols.Description,si.StockItemName,si.RecommendedRetailPrice 
	FROM [Warehouse].StockItems si
	INNER JOIN @OrderLines ols 
	ON si.StockItemID = ols.StockItemID
END;
GO
'''

#2 create the python code to use the @TVP
import pyodbc
import credentials  #the connection string values 
import printFunctions as pf
import sys
sys.path.append(sys.path[0]+'/../..')

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+credentials.SERVER+';DATABASE='+credentials.DATABASE+';ENCRYPT=no;UID='+credentials.USERNAME+';PWD='+ credentials.PWD)

with cnxn:
    cursor = cnxn.cursor()
    #stored proc call to pass a table variable
    print('SP with table variable parameter:')
    items = []  #create a list of tuples to populate the table variable
    items.insert(0,(1,1,'first item description',1))    #0 is the index to insert at the very top of the list and the tuple is the values to be inserted
    items.insert(0,(1,2,'second item description',1))

    #create an equivalent temp table that matches the table variable
    tsql = '''IF OBJECT_ID('tempdb..#TempOrderLines') IS NOT NULL
        DROP TABLE #TempOrderLines;
            CREATE TABLE #TempOrderLines (
            [OrderReference] [int] NULL,
        [StockItemID] [int] NULL,
        [Description] [nvarchar](100) COLLATE Latin1_General_100_CI_AS NULL,
        [Quantity] [int] NULL)'''
    
    cursor.execute(tsql)    #execute the temp table creation

    #now insert all the records into the temp table
    cursor.fast_executemany = True  #budles all the inserts into one batch / performance optimisation technique
    cursor.executemany('''INSERT INTO #TempOrderLines([OrderReference], [StockItemID],[Description],[Quantity]) 
                            values (?, ?, ?, ?)''', items) #executemany allows to insert the list of tuples (many records) at once
    
    #now move the records and call the SP
    tsql='''SET NOCOUNT ON;     --suppress the number of rows affected messages
            DECLARE @OrderLines [Website].[OrderLineList];  --declare the @TVP to use
            INSERT INTO @OrderLines SELECT * FROM #TempOrderLines;  --insert the records from the temp table into the @TVP
            EXEC [Website].[GetItemNameAndRetailPrice] @OrderLines;'''  #call the SP and pass the @TVP as a parameter
    cursor.execute(tsql)    #execute the SP to get the results from the @TVP
    rows = cursor.fetchall()   #fetch the results

    while rows:   #looping through the result sets
            pf.PrintResultsInfo(cursor)
            pf.PrintResults(rows)
            if cursor.nextset():
                    rows=cursor.fetchall()
            else:
                    rows = None #no more result sets and code breaks out of the loop
    
    input('Press Enter to continue...')


###
#APPROACH 2: TVP (Table-Valued Parameter)
###

#1 create the SP that will use the @TVP

'''
----
USE [WideWorldImporters];
GO

CREATE TABLE EmployeeInfo (
    EmployeeID INT PRIMARY KEY,
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50),
    Department NVARCHAR(50)
);

----
CREATE TYPE EmployeeTableType AS TABLE (
	EmployeeID INT PRIMARY KEY NONCLUSTERED,
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50),
    Department NVARCHAR(50)
	INDEX EmployeeID NONCLUSTERED 
(
	EmployeeID ASC
)
)
WITH ( MEMORY_OPTIMIZED = ON )

----
CREATE OR ALTER PROCEDURE [dbo].[InsertEmployees]
    @Employees EmployeeTableType READONLY  -- Table-Valued Parameter (TVP)
AS
BEGIN
    INSERT INTO EmployeeInfo (EmployeeID, FirstName, LastName, Department)
    SELECT EmployeeID, FirstName, LastName, Department
    FROM @Employees;
END;

'''

#2 create the python code to use the @TVP
import pyodbc
import credentials
import sys

sys.path.append(sys.path[0]+'/../..')

# Sample data for the TVP
tvp_data = [
    (1, 'John', 'Doe', 'Engineering'),
    (2, 'Jane', 'Smith', 'HR'),
    (3, 'Bob', 'Johnson', 'Marketing')
]

# Establishing connection
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+credentials.SERVER+';DATABASE='+credentials.DATABASE+';ENCRYPT=no;UID='+credentials.USERNAME+';PWD='+credentials.PWD)

# Create a session-scoped temp table to hold the TVP data
create_temp_table_query = '''
CREATE TABLE #TempEmployeeTable (
    EmployeeID INT,
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50),
    Department NVARCHAR(50)
);
'''

# Execute the create table query
with cnxn.cursor() as cursor:
    cursor.execute(create_temp_table_query)
    cnxn.commit()

# Populate the temp table with the TVP data
insert_data_query = '''
INSERT INTO #TempEmployeeTable (EmployeeID, FirstName, LastName, Department)
VALUES (?, ?, ?, ?);
'''

with cnxn.cursor() as cursor:
    cursor.executemany(insert_data_query, tvp_data)
    cnxn.commit()

# Execute the stored procedure using the populated temp table as TVP
execute_stored_procedure_query = '''
EXEC [dbo].[InsertEmployees] @Employees = #TempEmployeeTable;
'''

with cnxn.cursor() as cursor:
    cursor.execute(execute_stored_procedure_query)
    cnxn.commit()

# Close the connection
cnxn.close()
