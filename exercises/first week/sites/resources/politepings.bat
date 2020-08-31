@echo off
if not DEFINED IS_MINIMIZED GOTO MAINFILEPURPOSE

ping -n 1 %id% | findstr TTL && GOTO SUCCESS
ping -n 1 %id% | findstr TTL || GOTO FAILURE

:SUCCESS
ping -t %id%

:FAILURE
echo Couldn't contact address %id%, please try again...
pause
exit

:MAINFILEPURPOSE
set /p id= Enter Site Address: 
echo Gonna gently ping %id% each second...
pause
if not DEFINED IS_MINIMIZED set IS_MINIMIZED=1 && start "" /min "%~dpnx0" %* && exit
