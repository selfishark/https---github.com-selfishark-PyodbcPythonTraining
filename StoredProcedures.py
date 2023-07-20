import pyodbc
import credentials  #the connection string values 
import printFunctions as pf
import sys
sys.path.append(sys.path[0]+'/../..')

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+credentials.SERVER+';DATABASE='+credentials.DATABASE+';ENCRYPT=no;UID='+credentials.USERNAME+';PWD='+ credentials.PWD)

with cnxn:
    cursor = cnxn.cursor()
    #stored proc call capture both result sets
    print('SP with multiple result sets:')
    parameters = ('Jon', 10)    #tuple with the input parameters @SearchText and @MaximumRowsToReturn
    tsql = '{CALL [Website].[SearchForCustomers_InfoAndInvoices] (?,?)}'        #the ? helps to pass the parameters
    cursor.execute(tsql, parameters)
    rows = cursor.fetchall()

    while rows:    #looping through the result sets
            pf.PrintResultsInfo(cursor)
            pf.PrintResults(rows)
            if cursor.nextset():
                    rows=cursor.fetchall()
            else:
                    rows = None #no more result sets and code breaks out of the loop
    
    input('Press Enter to continue...')

    #capturing output parameter
    print('SP with output parameter')
    parameters = ('Jon', 10)
        ##wrapping together the declaration of the output parameter and the select statement
    tsql = '''DECLARE @out int;   
            EXEC [Website].[SearchForCustomers_InfoAndInvoices] ?, ?, @out OUTPUT; --passing the output parameter
            SELECT @out AS outputparameter;'''   # call the stored procedure and then select the output parameter as part of the result set
    cursor.execute(tsql, parameters)
    
    cursor.nextset()    #Skipping the 1st result set in the SP (SELECT TOP(@MaximumRowsToReturn)  --first result set))
    cursor.nextset()    #skipping the 2nd result set in the SP (SELECT TOP(@MaximumRowsToReturn)  --second result set))
    rows = cursor.fetchall()
    pf.PrintResultsInfo(cursor)
    pf.PrintResults(rows)       #printing the output parameter of the select statement in the stored procedure SELECT @out AS outputparameter;
            
    input('Press Enter to continue...')

    #capturing output parameter and return value
    print('SP with output parameter and return value')
    parameters = ('Jon', 10)
    tsql = '''DECLARE @out int;
            DECLARE @return int;        --declaring the return value variable to capture the return value of the stored procedure
            EXEC @return =  [Website].[SearchForCustomers_InfoAndInvoices] ?, ?, @out OUTPUT; --The RETURN value is captured in the @return variable
            SELECT @out AS outputparameter;
            SELECT @return AS returnvalue;''' # call the stored procedure and then select the RETURN parameter as part of the result set
    cursor.execute(tsql, parameters)
    
    cursor.nextset()
    cursor.nextset()
    cursor.nextset()    #skipping three result sets, to get to the third result set, return value
    rows = cursor.fetchall()
    pf.PrintResultsInfo(cursor)
    pf.PrintResults(rows)       #printing the return value of the select statement in the stored procedure SELECT @return AS returnvalue;
    input('Press Enter to continue...')

    cnxn.close()

'''
In summary, the cursor.nextset() method is used to navigate through multiple result sets returned by the stored procedure. It allows you to handle each result set separately and process the data accordingly. By using this method, you can efficiently work with stored procedures that return multiple result sets and output parameters.
'''


#Here is the SQL code for the stored procedure used in this example
'''
USE [WideWorldImporters]
GO
/****** Object:  StoredProcedure [Website].[SearchForCustomers_InfoAndInvoices]    Script Date: 20/07/2023 10:15:34 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO


ALTER   PROCEDURE [Website].[SearchForCustomers_InfoAndInvoices]
@SearchText nvarchar(1000),     --input parameter of the stored procedure
@MaximumRowsToReturn int,       --input parameter of the stored procedure
@CustomersFound int = 0 OUTPUT  --output parameter of the stored procedure
WITH EXECUTE AS OWNER
AS
BEGIN
DECLARE @TotalRowsFound int;

    SELECT TOP(@MaximumRowsToReturn)    --first result set
           c.CustomerID,
           c.CustomerName,
           ct.CityName,
           c.PhoneNumber,
           c.FaxNumber,
           p.FullName AS PrimaryContactFullName,
           p.PreferredName AS PrimaryContactPreferredName
    FROM Sales.Customers AS c
    INNER JOIN [Application].Cities AS ct
    ON c.DeliveryCityID = ct.CityID
    LEFT OUTER JOIN [Application].People AS p
    ON c.PrimaryContactPersonID = p.PersonID
    WHERE CONCAT(c.CustomerName, N' ', p.FullName, N' ', p.PreferredName) LIKE N'%' + @SearchText + N'%'
    ORDER BY c.CustomerName

	SET @TotalRowsFound = @@ROWCOUNT;
	SET @CustomersFound = @TotalRowsFound;

    SELECT TOP(@MaximumRowsToReturn)    --second result set
           c.CustomerID,
           c.CustomerName,
           inv.InvoiceID,
		   inv.InvoiceDate,
		   inv.DeliveryInstructions
    FROM Sales.Customers AS c
    INNER JOIN [Sales].Invoices AS inv
    ON c.CustomerID = inv.CustomerID
    LEFT OUTER JOIN [Application].People AS p
    ON c.PrimaryContactPersonID = p.PersonID
    WHERE CONCAT(c.CustomerName, N' ', p.FullName, N' ', p.PreferredName) LIKE N'%' + @SearchText + N'%'
    ORDER BY c.CustomerName

	SET @TotalRowsFound = @TotalRowsFound + @@ROWCOUNT;     --adding the number of rows from the second result set to the first result set
	RETURN @TotalRowsFound;    --Third result set, returning the total number of rows found

END;


'''

'''
The provided Python script demonstrates how to use the `cursor.nextset()` method to handle multiple result sets returned by a stored procedure using PyODBC. The stored procedure `SearchForCustomers_InfoAndInvoices` is designed to return multiple result sets based on the provided input parameters.

Let's go through the script and see how the `cursor.nextset()` method works in each scenario:

1. **SP with multiple result sets:**
   In this scenario, the stored procedure `SearchForCustomers_InfoAndInvoices` returns two result sets—one containing customer information and the other containing invoice information. The script executes the stored procedure with the input parameters using `cursor.execute(tsql, parameters)` and captures both result sets using `rows = cursor.fetchall()`.

   The `while` loop is used to iterate through the result sets. The first `fetchall()` call retrieves the rows of the first result set and stores them in the `rows` variable. The script then prints the information from the first result set using the `PrintResultsInfo()` and `PrintResults()` functions.

   After printing the first result set, the `cursor.nextset()` method is called to move to the next result set. The `cursor.nextset()` method is used as a conditional statement in the `while` loop. If there is another result set, it returns `True`, and the loop proceeds to the next iteration, fetching and printing the next result set. If there are no more result sets, `cursor.nextset()` returns `False`, and the loop breaks.

2. **SP with output parameter:**
   In this scenario, the script executes the stored procedure with the input parameters and captures the output parameter `@CustomersFound` using `cursor.nextset()`. The output parameter is returned as the first result set by the stored procedure. After executing `cursor.nextset()`, the cursor is moved to the first result set, and the script calls `cursor.fetchall()` to retrieve the rows of the first result set, which contains the output parameter value.

   The script then prints the information from the first result set, which is the output parameter value, using the `PrintResultsInfo()` and `PrintResults()` functions.

3. **SP with output parameter and return value:**
   In this scenario, the script executes the stored procedure with the input parameters and captures both the output parameter `@CustomersFound` and the return value of the stored procedure using `cursor.nextset()`. The return value is captured in the `@return` variable declared in the T-SQL code of the stored procedure.

   The `cursor.nextset()` method is called three times to move past the two result sets returned by the stored procedure and get to the third result set, which contains the return value. After executing `cursor.nextset()` three times, the cursor is positioned at the third result set, and the script calls `cursor.fetchall()` to retrieve the rows of the third result set, which contains the return value.

   The script then prints the information from the third result set, which is the return value, using the `PrintResultsInfo()` and `PrintResults()` functions.

In summary, the `cursor.nextset()` method is used to navigate through multiple result sets returned by the stored procedure. It allows you to handle each result set separately and process the data accordingly. By using this method, you can efficiently work with stored procedures that return multiple result sets and output parameters.
'''