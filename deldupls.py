#!/usr/bin/env python3

from sys import argv
import os
import hashlib
from collections import defaultdict
import filecmp


def get_hash(filename, method='blake2b'):
    with open(filename, 'rb', buffering=0) as f:
        return hashlib.file_digest(f, method).hexdigest()


kwargs = {}
if len(argv) > 1:
    kwargs = dict(arg.split('=') for arg in argv[1:])

if 'path' in kwargs:
    path = kwargs['path']
else:
    path = os.getcwd()

if 'safe' in kwargs:
    safe: bool = kwargs['safe']
else:
    safe = False

files_by_size = defaultdict(list)
for filename in os.listdir(path):
    file = os.path.join(path, filename)
    if os.path.isfile(file):
        files_by_size[os.stat(file).st_size].append(file)

same_size_files = [files for files in files_by_size.values() if len(files) > 1]
hashes = {file: get_hash(file) for list_of_files in same_size_files for file in list_of_files}

to_delete = {}
for files in same_size_files:
    for i in range(len(files)-1):
        file1 = files[i]
        if file1 not in to_delete:
            for file2 in files[i+1:]:
                if file2 not in to_delete:
                    if hashes[file1] == hashes[file2]:
                        if safe:
                            if filecmp.cmp(file1, file2, shallow=False):
                                to_delete[file2] = os.stat(file2).st_size
                        else:
                            to_delete[file2] = os.stat(file2).st_size

print(f'{len(to_delete)} duplicated files ({sum(to_delete.values())/1000**2}MB)')
while True:
    delete = input('Do you want to delete them? (y/n)').lower()
    if delete == 'y' or delete == 'yes':
        for filename in to_delete.keys():
            os.remove(filename)
        break
    elif delete == 'n' or delete == 'no':
        break
