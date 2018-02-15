import os
import Save_DirList

sdl = Save_DirList

p = r'C:\users\dgriffi6\documents'
sdl.mypath(p)

print(os.path.basename(p))
