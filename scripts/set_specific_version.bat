REM Variable Part
set /p package_name=<.\..\package_name.txt

REM Constant Part
set package_path=.\..\%package_name%

set cmd_data=python -m incremental.update --path=%package_path% %package_name%
call activate_vir_env.bat
echo %2
%cmd_data% %1 %3
call deactivate_vir_env.bat