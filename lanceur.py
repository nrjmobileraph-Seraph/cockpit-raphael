import subprocess, sys, os, time, webbrowser
os.chdir(r'C:\Users\BoulePiou\cockpit-raphael')
proc = subprocess.Popen([sys.executable, '-m', 'streamlit', 'run', 'app.py', '--server.headless=true'])
time.sleep(3)
webbrowser.open('http://localhost:8501')
proc.wait()
