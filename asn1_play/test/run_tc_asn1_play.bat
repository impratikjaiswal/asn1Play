@echo off
pushd %~dp0
echo.
echo.
echo.
echo.
echo "sgp22_v3_0_0__epp_v3_2__sgp32_v1_1"

cd ..
cd ..
cd scripts
call activate_vir_env.bat
cd ..
python -m asn1_play.main.asn1play > asn1_play\test\logs\sgp22_v3_0_0__epp_v3_2__sgp32_v1_1.log
cd scripts
call deactivate_vir_env.bat
cd ..
echo.
echo.
echo.
echo.
echo "Batch Execution Done"
