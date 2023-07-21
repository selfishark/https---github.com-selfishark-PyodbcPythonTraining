import pyodbc
import credentials  #the connection string values 
import printFunctions as pf
import sys
sys.path.append(sys.path[0]+'/../..')


#Establishing connection
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+credentials.SERVER+';DATABASE='+credentials.DATABASE+';ENCRYPT=no;UID='+credentials.USERNAME+';PWD='+ credentials.PWD)

#Example 1: Working with data types
with cnxn:
    cursor = cnxn.cursor()
    #Converting bool to bit
    tsqlparam = '''--bool to bit
            SELECT count(*) FROM Application.People
            WHERE IsPermittedToLogon=?'''
    parameter = False #converts boolean (true/false) to bit (1/0)
    cursor.execute(tsqlparam,parameter)
    print('Result: ' + str(cursor.fetchval()))
    input('Press Enter to continue...')

    #Converting Unicode to Varchar
    cursor.setinputsizes([(pyodbc.SQL_VARCHAR, 50, 0)]) #set the size of the input parameter but also the type
    tsqlparamsized = '''--unicode to varchar
            SELECT TOP 10 cities.CityID, cities.CityName, cities.LatestRecordedPopulation,sprovs.StateProvinceName
            FROM Application.Cities cities 
            INNER JOIN Application.StateProvinces sprovs
            ON cities.StateProvinceID=sprovs.StateProvinceID
            WHERE StateProvinceName = ?
            AND cities.LatestRecordedPopulation IS NOT NULL
            ORDER BY cities.LatestRecordedPopulation DESC;'''
    state1 = 'California'
    cursor.execute(tsqlparamsized,state1)
    input('Press Enter to continue...')

    #Converting XML to Python string
    tsqlparamsized = '''--XML to str
            SELECT TOP 3 cities.CityID, cities.CityName, cities.LatestRecordedPopulation,sprovs.StateProvinceName
            FROM Application.Cities cities 
            INNER JOIN Application.StateProvinces sprovs
            ON cities.StateProvinceID=sprovs.StateProvinceID
            WHERE StateProvinceName = ?
            AND cities.LatestRecordedPopulation IS NOT NULL
            ORDER BY cities.LatestRecordedPopulation DESC
            FOR XML AUTO;'''    #XML AUTO returns a single XML document / XML is an actual data type in SQL Server
    state1 = 'California'
    cursor.execute(tsqlparamsized,state1)
    result = cursor.fetchval()
    print('Result Type: ' + str(type(result)))  #convert the XML received as a python string
    print('Result: ' + result)
    input('Press Enter to continue...')


#Example2: Text-based data types conversionn for unsupported data types in python
    #A Text-based consersion
    #no conversion
    tsql1 = '''--no conversion
            SELECT SupplierName, DeliveryLocation   --DeliveryLocation is a geometry data type that is not recognized by Python
            FROM [Website].[Suppliers]'''
    cursor.execute(tsql1)
    try:
            rows = cursor.fetchall()
    except pyodbc.Error as pyodbcerror:
            print('Error: ' + str(pyodbcerror))

    input('Press Enter to continue...')

    #with conversion
    tsql2 = '''--with conversion
            SELECT SupplierName, DeliveryLocation.STAsText()    --STAsText() converts the geometry data type to a text-based data type to process it in Python
            FROM [Website].[Suppliers]'''
    cursor.execute(tsql2)
    rows = cursor.fetchall()
    pf.PrintResultsInfo(cursor)
    pf.PrintResults(rows)

    input('Press Enter to continue...')

    cnxn.close() 
