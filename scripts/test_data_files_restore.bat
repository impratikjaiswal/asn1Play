@ECHO ON

SET FileList=test_data_files_list.txt
SET Source=E:\Backup\D\Other\Github_Self\asn1play\data
SET Destination=D:\Other\Github_Self\asn1play\data

FOR /F "USEBACKQ TOKENS=*" %%F IN ("%FileList%") DO XCOPY /F /Y "%Source%\%%~F" "%Destination%\%%~F"

GOTO :EOF