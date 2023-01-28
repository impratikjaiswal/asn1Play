call activate_vir_env.bat
echo Upgrading requirements
pip install -r ..\requirements.txt --upgrade
call deactivate_vir_env.bat