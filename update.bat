@echo off
cls
REN ver.txt ver1.txt
setlocal
for /f "tokens=4-5 delims=. " %%i in ('ver') do set VERSION=%%i.%%j
::windows 7
if "%version%" == "6.1" goto win7
::windows 10
if "%version%" == "10.0" goto win10
:win7
cls
powershell -Command "(New-Object Net.WebClient).DownloadFile('https://raw.githubusercontent.com/congaterori/pythonA.I/beta-for-windows-10/ver.txt', 'ver.txt')"
goto next
:win10
cls
powershell -Command "Invoke-WebRequest https://raw.githubusercontent.com/congaterori/pythonA.I/beta-for-windows-10/ver.txt -OutFile ver.txt"
goto next
:next
cls
setlocal DisableDelayedExpansion
for /f "Delims=" %%a in (ver.txt) do set ver=%%a
setlocal DisableDelayedExpansion
for /f "Delims=" %%a in (ver1.txt) do set ver1=%%a
FC ver.txt ver1.txt > NUL && goto same || goto no
:same
cls
echo your version: %ver1%
echo have new update %ver%
echo do you want to update?
echo 1.yes
echo 2.no
set /p que=
if %que% == 1 goto yes
if %que% == 2 goto done
:yes
cls
echo downloading...
if "%version%" == "6.1" powershell -Command "(New-Object Net.WebClient).DownloadFile('https://github.com/congaterori/pythonA.I/archive/refs/heads/beta-for-windows-10.zip', 'pythonA.I-master.zip')"
if "%version%" == "10.0" powershell -Command "Invoke-WebRequest https://github.com/congaterori/pythonA.I/archive/refs/heads/beta-for-windows-10.zip -OutFile pythonA.I-master.zip"
if not exist pythonA.I-master.zip goto done
unzip.exe pythonA.I-master.zip > nul
pause
timeout 5 > nul
Del pythonA.I-master.zip
Del ver.txt
REN ver1.txt ver.txt
set now = %CD%
cd ..
echo md C:\Users\DELL\Downloads\pythonA.I-beta-for-windows-10 > up.bat
echo xcopy /A "pythonA.I-beta-for-windows-10\pythonA.I-beta-for-windows-10" "C:\Users\DELL\Downloads\pythonA.I-beta-for-windows-10" >> up.bat
echo RD /S /Q pythonA.I-beta-for-windows-10 >> up.bat
echo md pythonA.I-beta-for-windows-10 >> up.bat
echo xcopy /A "C:\Users\DELL\Downloads\pythonA.I-beta-for-windows-10" "C:\Users\DELL\Documents\pythonA.I-beta-for-windows-10" >> up.bat
echo RD /S /Q C:\Users\DELL\Downloads\pythonA.I-beta-for-windows-10 >> up.bat
echo msg * update done >> up.bat
start up.bat
timeout 1 > nul
Del up.bat
cd %CD%
endlocal
exit
:no
cls
echo no update yet
echo your version is: %ver1%
echo new version is: %ver%
pause
goto done
:done
endlocal
call Vevoast.py