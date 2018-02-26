#!
# Function to loop through every file within path provided and write the
#   [Path|Filename|Last Accessed Date|Size in bytes] to a file.
import os
from os.path import join
from datetime import date as dt

#Added for Work to save files to 1 local location
c = r'C:\FileMgmt'


def mypath(path):

    os.chdir(path)
    pname = os.path.basename(path)
    dirfile = open(c + '\\' + pname + '_DirList.txt', 'w')

    for foldername, subfolders, filenames in os.walk(path):

        for folder in subfolders:

            for filename in filenames:
                mdt = dt.fromtimestamp(os.stat(join(foldername, filename)).st_atime)
                num = int(os.stat(join(foldername, filename)).st_size)
                dirfile.writelines(foldername + ': ' + filename + ': ' + str(mdt) + ': ' + str(
                    num) + '\n')

    dirfile.close()
