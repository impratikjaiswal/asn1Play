call activate_vir_env.bat
python.exe -m pip install --upgrade pip
echo Upgrading requirements
pip install -r ..\requirements.txt --upgrade
call deactivate_vir_env.bat