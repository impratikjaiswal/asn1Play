call activate_vir_env.bat
echo UnInstalling Internal tools requirements
pip uninstall -r ..\requirements_internal_tool_name.txt -y
call deactivate_vir_env.bat
