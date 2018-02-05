import os
import Save_DirList

sdl = Save_DirList

p = r'C:\users\migra'
sdl.mypath(p)

print(p)
print(os.path.basename(p))
