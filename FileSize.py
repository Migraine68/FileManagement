import os

from os.path import join, getsize

p = (r'c:\users\migra\downloads')
rt = []
fn = []
size = []

for root, dirs, files in os.walk(p):
    rt = (root + ': ')
    fn = list(name + ': ' for name in files)
    size = list([os.stat(join(root,name)).st_size for name in files])
    #print(root + '\n')#print("bytes in", len(files), "non-directory files")
    size = [os.stat(join(root, files)).st_size]
    print(size)
