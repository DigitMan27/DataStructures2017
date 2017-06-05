@echo off
set argument=%1
set message1=Welcome to the Executioner Program
set message2=Execute..
set message3=Executioner Quits Now.Thank you! 
echo %message1%
echo %message2%
py Main.py %argument%
rd /s /q __pycache__
echo %message3%
