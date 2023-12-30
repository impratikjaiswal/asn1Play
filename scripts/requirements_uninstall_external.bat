call activate_vir_env.bat
echo UnInstalling External requirements
pip uninstall -r ..\requirements_external_name.txt -y
call deactivate_vir_env.bat
