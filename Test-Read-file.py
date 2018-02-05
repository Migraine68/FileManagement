import os
import Save_DirList

sdl = Save_DirList

p = r'C:\Users\dgriffi6\Documents\CoE_Reports'

sdl.mypath(p)

print(os.path.basename(p))
print('Done')