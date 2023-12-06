call activate_vir_env.bat
echo UnInstalling requirements
pip uninstall -r ..\requirements_external_name.txt -y
call deactivate_vir_env.bat
