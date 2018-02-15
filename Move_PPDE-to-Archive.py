import shutil
import os


Src = os.listdir('C:\\PPDE')
pth = (r'c:\ppde')
Dest = (r'B:\Reports\PPDE_Reports\Archive')

for files in Src:
    if files.endswith('.zipx'):
        shutil.move(pth + '\\' + files, Dest)
