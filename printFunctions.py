import pyodbc

#print the collect result from the cursor (ROW-BASED)
def PrintResults(rows):
        if len(rows)==0:        #check if nothing came back
                print('No rows returned')
        else:
                print(str(len(rows)) + ' row(s) returned:')     #check the row lenght to know how many results are returned
                print(', '.join(c[0] for c in rows[0].cursor_description))      #print the column name based on the description metadata
                for row in rows:
                        print(', '.join(str(value) for value in row))           #print the value of the row with a datatype convertion function 'str'

#print the collected result metadata from the cursor (COLUMN-BASED)
def PrintResultsInfo(cursor):
        print('Result description:')
        for column in cursor.description:       #for each column in the metadata description (refer to the cursor documentation to know the correct index value [] to use)
                print('Name: ' + column[0])     #get the name of the column
                print('Python type: ' + str(column[1])) #get the python type
                print('Nullable: ' + str(column[6]))