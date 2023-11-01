call activate_vir_env.bat
echo Installing Internal tools requirements
pip install -r ..\requirements_internal_tool.txt
call deactivate_vir_env.bat
