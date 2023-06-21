import subprocess
import os
import sys

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'streamlit'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'torch'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'joblib'])

os.system('cmd /C "python -m streamlit run app.py"')
