@echo off
cd /d C:\Users\BoulePiou\cockpit-raphael
start /min cmd /c "streamlit run app.py --server.headless true --browser.gatherUsageStats false"
ping 127.0.0.1 -n 6 >nul
start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" --start-maximized --app=http://localhost:8501
