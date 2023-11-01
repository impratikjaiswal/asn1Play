call activate_vir_env.bat
echo UnInstalling Internal lib requirements
pip uninstall -r ..\requirements_internal_lib_name.txt -y
call deactivate_vir_env.bat
