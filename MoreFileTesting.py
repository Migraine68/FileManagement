import os
from os.path import join
from datetime import date as dt



#pp = pprint.pprint
p = (r'c:\users\migra\downloads')
f = (r'C:\Users\migra\Downloads\_SensorKit_Python_code_for_RaspberryPi-master.zip')

myfl = open('listfiles.txt', 'w')

fld =[]
sfld = []
fl = []

for foldername, subfolders, filenames in os.walk(p):
    #fld.append('The Current Folder is ' + foldername)

    for subfolder in subfolders:
        #sfld = ('SubFolder of ' + foldername + ': ' + subfolder)

        for filename in filenames:
            mdt = dt.fromtimestamp(os.stat(join(foldername, filename)).st_atime)
            num = int(os.stat(join(foldername, filename)).st_size)
            myfl.writelines(foldername + ': ' + filename + ': ' + str(mdt) + ': ' + str(num) + '\n')            #print([os.stat(p, filename).st_size for filename in filenames])


myfl.close()







