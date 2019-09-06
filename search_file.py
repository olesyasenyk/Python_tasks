import os
import sys

path = sys.argv [1]
name = sys.argv [2]

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if name in file:
            files.append(os.path.join(r, file))

for f in files:
    print(f)
