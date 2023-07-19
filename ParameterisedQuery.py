import pyodbc
import credentials  #the connection string values 
import printFunctions as pf
import sys

sys.path.append(sys.path[0]+'/../..')


'''Example of simple query with parameters with the use of 'State variable'
    #pay attention to the size of the caracters lengts used in each 'State variable' (can create many plan cache entries)
    #so the use of 'RECOMPILE' hint can be used to avoid this problem (query3)

'''
#Establishing connection
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+credentials.SERVER+';DATABASE='+credentials.DATABASE+';ENCRYPT=no;UID='+credentials.USERNAME+';PWD='+ credentials.PWD)
with cnxn:
    cursor = cnxn.cursor()
    #parameterised query within the cursor connection
    query1 = '''--parameterised query taken from states
                SELECT TOP 10 cities.CityID, cities.CityName, cities.LatestRecordedPopulation,sprovs.StateProvinceName
                FROM Application.Cities cities 
                INNER JOIN Application.StateProvinces sprovs
                ON cities.StateProvinceID=sprovs.StateProvinceID
                WHERE StateProvinceName = ? 
                AND cities.LatestRecordedPopulation IS NOT NULL
                ORDER BY cities.LatestRecordedPopulation DESC;'''
    state1 = 'California'   
    state2 = 'Texas'       
    cursor.execute(query1,state1)
    cursor.execute(query1,state2)
    input('Press Enter to continue...')

    #parameterized with input size
    cursor.setinputsizes([(pyodbc.SQL_WVARCHAR, 50, 0)])
    query2 = '''--parameterised with type size
                SELECT TOP 10 cities.CityID, cities.CityName, cities.LatestRecordedPopulation,sprovs.StateProvinceName
                FROM Application.Cities cities   
                INNER JOIN Application.StateProvinces sprovs
                ON cities.StateProvinceID=sprovs.StateProvinceID
                WHERE StateProvinceName = ?
                AND cities.LatestRecordedPopulation IS NOT NULL
                ORDER BY cities.LatestRecordedPopulation DESC;'''
    state1 = 'California'
    state2 = 'Texas'
    cursor.execute(query2,state1)
    cursor.execute(query2,state2)
    input('Press Enter to continue...')


    # Querying the cursor connection with RECOMPILE and a state variable
        #Example of simple query with parameters with the use of 'State variable' and 'RECOMPILE' hint
    cursor = cnxn.cursor()
    query3 = '''SELECT TOP 10 cities.CityID, cities.CityName, cities.LatestRecordedPopulation, sprovs.StateProvinceName
              FROM Application.Cities cities 
              INNER JOIN Application.StateProvinces sprovs 
              ON cities.StateProvinceID = sprovs.StateProvinceID
              WHERE StateProvinceName = ?
              AND cities.LatestRecordedPopulation IS NOT NULL
              ORDER BY cities.LatestRecordedPopulation DESC
              OPTION (RECOMPILE);'''
    state1 = 'California'
    state2 = 'Texas'    
    cursor.execute(query3, state1)
    cursor.execute(query3, state2)
    rows = cursor.fetchall()


    # Print cursor row count
    print('Cursor row count: ' + str(cursor.rowcount))


    # Print metadata and rows results using the print functions
    pf.PrintResultsInfo(cursor)  # Metadata
    pf.PrintResults(rows)        # Rows results

    input('Press Enter to continue...')

cnxn.close()
