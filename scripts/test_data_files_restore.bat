REM Fetch Parent Folder Name
FOR %%I IN (..) DO SET parent_dir_name=%%~nI%%~xI
echo %parent_dir_name%

@ECHO ON

SET FileList=test_data_files_list.txt
SET Source=E:\Backup\D\Other\Github_Self\%parent_dir_name%\data
SET Destination=D:\Other\Github_Self\%parent_dir_name%\data

FOR /F "USEBACKQ TOKENS=*" %%F IN ("%FileList%") DO echo f | XCOPY /F /Y "%Source%\%%~F" "%Destination%\%%~F"

GOTO :EOF

pause