#!/usr/bin/env python3
r""" """

import os
import hashlib

def get_hash(filename, method='md5'):
    with open(filename, 'rb', buffering=0) as f:
    	return hashlib.file_digest(f, method)

safe_comparison = False
PATH = os.getcwd

files = [file for file in os.path.listdir(PATH) if os.isfile(os.path.join(PATH, file))]
to_delete = {}
hashes = {}

for i in len(files):
	file1 = files[i]
	if file1 not in to_delete:
		for file2 in files[i:]:
			if file2 not in to_delete:
				size_1 = os.stat(file1).st_size
				size_2 = os.stat(file2).st_size
				if size_1 == size_2:
					if file1 not in hashes:
						hashes̈́[file1] = get_hash(file1)
					if file2 not in hashes:
						hashes̈́[file2] = get_hash(file2)
					if hashes̈́[file1] == hashes̈́[file2]:
						if safe_comparison:
							if filecmp.cmp(file1, file2, shallow=False):
								to_delete[file2] = size_2
						else:
							to_delete[file2] = size_2


# ---- Create hashes in advance ----
# files = [(file, os.stats(file).st_size, get_hash(file)) for file in os.path.listdir(PATH) if os.isfile(os.path.join(PATH, file))]
# to_delete = {}
#
# for i in len(files):
# 	file_1 = files[i]
# 	if file_1[0] not in to_delete:
# 		for file_2 in files[i:]:
# 			if file_2[0] not in to_delete:
# 				if file_1[1] == file_2[1]:
# 					if file_1[2] == file_2[2]:
# 						if safe_comparison:
# 							if filecmp.cmp(file_1[0], file_2[0], shallow=False):
# 								to_delete.add(file_2[0])
# 						else:
# 							to_delete.add(file_2[0])


print(f'There are {len(to_delete)} duplicated files ({sum(to_delete.values())/1024**2}MB)')


# CHUNK_SIZE = 65536  # 64kb
#
# def get_md5(file, chunk_size)
# 	md5 = hashlib.md5()
# 	with open(file, 'rb') as f:
# 	    while True:
# 	        chunk = f.read(chunk_size)
# 	        if not chunk:
# 	            break
# 	        md5.update(chunk)
# 	    return md5