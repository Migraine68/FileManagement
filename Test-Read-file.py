import os
import Save_DirList

sdl = Save_DirList

p = r'G:\BusSystems\SSI'
p2 = os.path.abspath(p)
sdl.mypath(p)

print(p)
