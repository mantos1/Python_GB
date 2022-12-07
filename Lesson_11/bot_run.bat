@echo off

call %~dp0venv\Scripts\activate

cd %~dp0

::SET /P TOKEN =<TOKEN.txt

python bot_aiogram.py
 
pause