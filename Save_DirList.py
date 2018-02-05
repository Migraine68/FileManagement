import os
from os.path import join
from datetime import date as dt


def mypath(path):
    pname = os.path.basename(path)
    dirfile = open(path + '\\' + pname + '_DirList.txt', 'w')

    for foldername, subfolders, filenames in os.walk(path):

        for subfolder in subfolders:

            for filename in filenames:
                mdt = dt.fromtimestamp(os.stat(join(foldername, filename)).st_atime)
                num = int(os.stat(join(foldername, filename)).st_size)
                dirfile.writelines(foldername + ': ' + filename + ': ' + str(mdt) + ': ' + str(
                    num) + '\n')

    dirfile.close()
