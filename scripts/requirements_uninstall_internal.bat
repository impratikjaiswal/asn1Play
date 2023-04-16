call activate_vir_env.bat
echo UnInstalling Internal requirements
pip uninstall -r ..\requirements_internal_name.txt -y
call deactivate_vir_env.bat
