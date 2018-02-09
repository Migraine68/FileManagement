import os
import Save_DirList

sdl = Save_DirList

p = r'd:'
ls = os.path.splitdrive(p)
d = os.chdir(ls[0] + '\\')

os.chdir(p)

print(os.getcwd())

sdl.mypath(p)

print(os.path.basename(p))
