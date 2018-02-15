import pathlib

pl = pathlib

p = pl.Path('c:/users/migra/downloads')

#for files in p.iterdir():
 #   print(files)


import os

for folderName, subfolders, filenames in os.walk('C:\\users\\migra\\downloads'):
    print('The current folder is ' + folderName)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
    for filename in filenames:
        print('FILE INSIDE ' + folderName + ': '+ filename)

    print('')

