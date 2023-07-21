import struct   #for handling RAW data conversion and in this case datetimeoffset because pyodbc does not support it
import pyodbc
import credentials  #the connection string values 
import printFunctions as pf
import sys
sys.path.append(sys.path[0]+'/../..')


    ## Credit to the Pyodbc developers for the conversion function!
        #It taakes the binary representation and converts it to a Python, keeping the SQL code transparent
def handle_datetimeoffset(dto_value):
    # ref: https://github.com/mkleehammer/pyodbc/issues/134#issuecomment-281739794
    tup = struct.unpack("<6hI2h", dto_value)  # e.g., (2017, 3, 16, 10, 35, 18, 0, -6, 0) #unpacks the binary representation of datetimeoffset
    tweaked = [tup[i] // 100 if i == 6 else tup[i] for i in range(len(tup))]    #modifies the tuple to be used in the format function based on the actual raw data
    return "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d}.{:07d} {:+03d}:{:02d}".format(*tweaked) # e.g., '2017-03-16 10:35:18.0000000 -06:00'

#Establishing connection
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+credentials.SERVER+';DATABASE='+credentials.DATABASE+';ENCRYPT=no;UID='+credentials.USERNAME+';PWD='+ credentials.PWD)

#Example Working with data types
with cnxn:
        cursor = cnxn.cursor()
#Example 3: Handling datetimeoffset data type using output converters
    #B Output converter function are 'only used for output' data types; 
        #very effective when Text-based conversion is not possible
        tsqloutputconvert = '''SELECT TOP 5 InvoiceDate, DeliveryInstructions, 
                ToDateTimeOffset(ConfirmedDeliveryTime,120) ConfirmedDateTimeOffset
                FROM [Sales].[Invoices]
                ORDER BY ConfirmedDeliveryTime DESC'''
       
        cursor.execute(tsqloutputconvert)
        try:
                rows = cursor.fetchall()
        except pyodbc.Error as pyodbcerror:
                print('Error: ' + str(pyodbcerror))

        input('Press Enter to continue...')

        #with conversion (-155 is the code for datetimeoffset, which is used to register the function to handle the datetimeoffset data type conversion)
        cnxn.add_output_converter(-155, handle_datetimeoffset)  #register the function to handle the datetimeoffset data type
        cursor.execute(tsqloutputconvert)       #execute the query (each corresponding datatype is converted automatically, NOTE the SQL Code remains the same
        rows = cursor.fetchall()
        pf.PrintResultsInfo(cursor)
        pf.PrintResults(rows)

        cnxn.clear_output_converters()  #clear the output converter when the conversion is not required anymore; 
        input('Press Enter to continue...')

        cnxn.close() 


'''
EXAMPLE OF LOGIC BEHIND THE CONVERSION FUNCTION

For this example, let's assume that `custom_data_type` represents a unique identifier composed of two integers. We'll use the `struct.unpack` function to convert the binary value into a tuple of two integers.

Here's how you might create a conversion function for `custom_data_type`:

```python
import struct

def handle_custom_data_type(binary_value):
    # Assuming custom_data_type is represented as two 32-bit integers (total 8 bytes)
    unpacked_data = struct.unpack("<ii", binary_value)
    # If the data is represented as two 64-bit integers, use "<qq" in the unpack format string

    # Add any additional processing or manipulation here if needed
    return unpacked_data

# Example usage:
binary_data = b'\x01\x00\x00\x00\x02\x00\x00\x00'  # Replace with the actual binary data returned by the database
result = handle_custom_data_type(binary_data)
print(result)  # Output: (1, 2)
```

In this example, we use the `<ii` format string with `struct.unpack` to interpret the first 4 bytes as the first 32-bit integer and the next 4 bytes as the second 32-bit integer. If the data is represented differently (e.g., two 64-bit integers), adjust the format string accordingly (e.g., use `<qq`).

Remember that the exact implementation of the conversion function depends on the specific binary representation and data type you are working with. Always refer to the database documentation or consult with the database provider to obtain the necessary information about the binary representation of the data type.
'''
