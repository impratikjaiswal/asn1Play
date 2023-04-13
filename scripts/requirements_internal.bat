call activate_vir_env.bat
echo Installing requirements
pip install -r ..\requirements_internal.txt
call deactivate_vir_env.bat
