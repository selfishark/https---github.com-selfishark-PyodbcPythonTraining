-- after installing an new instance of SSMS with the Machine Leaning Services option, run this script to check and change the To change database-level settings
-- To change database-level settings, use the ALTER DATABASE statement. For example, to enable the execution of scripts on the server, run the following statement:
EXEC sp_configure 'external scripts enabled';

-- To enable the execution of scripts on the server, set the external scripts enabled option to 1.
EXEC sp_configure 'external scripts enabled',1;
RECONFIGURE;

-- Example of a Python script Execution
--Example 1: 
EXEC sp_execute_external_script @language=N'Python', -- this script will 
@script=N'OutputDataSet = InputDataSet',
@Input_data_1 = N'SELECT 42'
WITH RESULT SETS ((TheAnswer int)); 


EXEC sp_execute_external_script @script=N'import sys;print(sys.version)',@language=N'Python'
GO


-- Example 2: 
EXEC sp_execute_external_script @language=N'Python',
@script=N'
import time
OutputDataSet = InputDataSet
time.sleep(1800)
',
@Input_data_1 = N'SELECT 42'
WITH RESULT SETS ((TheAnswer int));


