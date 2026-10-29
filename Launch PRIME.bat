@echo off
title PRIME App Server
echo Starting PRIME...
cd /d "%~dp0"
".venv/Scripts/python.exe" -m streamlit run ./src/main.py
pause