call activate_vir_env.bat
echo Starting Flask Server
cd ..
flask --app asn1_play/app.py --debug run
cd scripts
call deactivate_vir_env.bat
