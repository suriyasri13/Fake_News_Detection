@echo off
title FactGuard AI Ultra - Launcher
echo ===================================================
echo   🛡️  FactGuard AI Ultra: Starting Dual Services...
echo ===================================================
echo.

echo [1/2] 🚀 Starting Streamlit Analysis Engine...
start "Streamlit Dashboard" cmd /k "streamlit run app.py"

echo.
echo [2/2] 🌐 Starting React Landing Page...
start "Vite Dev Server" cmd /k "cd landing && npm run dev"

echo.
echo ===================================================
echo   🎉 Done! Both services are opening in new windows.
echo ===================================================
pause
