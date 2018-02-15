import shutil
import os

Src = os.listdir('C:\\PPDE')
src = (r'c:\ppde')
Dest = (r'B:\Reports\PPDE_Reports\Archive')
f = 'PPDE_SourceData_*.zipx'

for files in Src:
    if files.endswith('.zipx'):
        print(files)
