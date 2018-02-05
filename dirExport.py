import os
from os.path import join
from datetime import date as dt


def dirExport(path)
myfile = open('listfiles.txt', 'w')

for foldername, subfolders, filenames in os.walk(p):
    #fld.append('The Current Folder is ' + foldername)

    for subfolder in subfolders:
        #sfld = ('SubFolder of ' + foldername + ': ' + subfolder)

        for filename in filenames:
            mdt = dt.fromtimestamp(os.stat(join(foldername, filename)).st_atime)
            num = int(os.stat(join(foldername, filename)).st_size)
            myfile.writelines(foldername + ': ' + filename + ': ' + str(mdt) + ': ' + str(num) + '\n')            #print([os.stat(p, filename).st_size for filename in filenames])


myfile.close()