# 1 how to install pyodbc

# create the virtual environment
#C:\Users\ltwansi\OneDrive\Documents Synching\Python Scripts\venv>python -m venv selfisharkpy

#activate the virtual environment
#C:\Users\ltwansi\OneDrive\Documents Synching\Python Scripts\venv>selfisharkpy\Scripts\activate

#install pyodbc libraries in the environment and in the global python of the machine
#(selfisharkpy) C:\Users\ltwansi\OneDrive\Documents Synching\Python Scripts\venv>pip install pyodbc

# 2 connect to your database with mssql extention, add pylint for python file support


## 3 create a connection string to the database
import pyodbc
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
SERVER = r'W3-DEV-005\MSSQLSERVEREVAL' #r is used to pass raw string with special characters
DATABASE = 'WideWorldImporters'
USERNAME = 'username'
PWD = 'password'
# ENCRYPT defaults to yes starting in ODBC Driver 18.
# It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+SERVER+';DATABASE='+DATABASE+';ENCRYPT=no;UID='+USERNAME+';PWD='+ PWD)
cursor = cnxn.cursor()
cnxn.close()

CONNECTION_STRING = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+SERVER+';DATABASE='+DATABASE+';ENCRYPT=no; APP=PyodbcPythonTraining; UID='+USERNAME+';PWD='+ PWD
#Connection #1
connection = pyodbc.connect(CONNECTION_STRING)
cursor = connection.cursor()
    ## printing some attributes of the connection
print('Connection Attributes:')
print('Autocommit: ' + str(connection.autocommit))
print('Timeout: ' + str(connection.timeout))

input('Press Enter to continue...')

connection.close()

#Test the current connection to the server (valid for all connection methods):
SELECT sess.session_id,login_time,[host_name],[program_name],client_interface_name,login_name,dbs.[name] dbname,
[status],open_transaction_count, conns.net_packet_size
FROM 
sys.dm_exec_sessions sess 
INNER JOIN sys.databases dbs ON sess.database_id=dbs.database_id
INNER JOIN sys.dm_exec_connections conns ON sess.session_id=conns.session_id
WHERE [program_name] LIKE 'PyodbcPython%';

#Connection #2 overriding odbc timeout
try:
	with pyodbc.connect(CONNECTION_STRING, timeout=5) as connection:
		print('Connection did not time out')
except:
	print('Connection timed out')
finally:
	input('Press Enter to continue...')
	

#Connection #3 using ODBC constants for advanced changes
    #Constant values (use the browser Find function): https://github.com/Microsoft/ODBC-Specification/blob/master/Windows/inc/sqlext.h
    #Explanation of settings: https://docs.microsoft.com/en-us/sql/odbc/reference/syntax/sqlsetconnectattr-function
SQL_ATTR_TRACE=104 # look for the trace file (.LOG) in the %Temp% directory
SQL_ATTR_PACKET_SIZE = 112 ## overdire the packet size if need be
with pyodbc.connect(CONNECTION_STRING, attrs_before={SQL_ATTR_TRACE : 1, 
						    SQL_ATTR_PACKET_SIZE : 1024 * 32}) as connection:
	input('Press Enter to continue...')

