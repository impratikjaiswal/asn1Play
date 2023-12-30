call activate_vir_env.bat
echo UnInstalling Experimental requirements
pip uninstall -r ..\requirements_experimental_name.txt -y
call deactivate_vir_env.bat
