SET /P versionValue=Please Enter Project Version:

@ECHO OFF
:firstQuo
set versionValue2=%versionValue:~0,1%
if '^%versionValue2%' == '^"' goto lastQuo
if not '^%versionValue2%' == '^"' set versionValue="%versionValue%

:lastQuo
set versionValue2=%versionValue:~-1%
if '^%versionValue2%' == '^"' goto finalC
if not '^%versionValue2%' == '^"' set versionValue=%versionValue%"

:finalC
@ECHO ON

call set_specific_version.bat --newversion "Setting Specific Version" %versionValue%