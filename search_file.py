import os

path = 'd:\Project Documentation'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if 'Falafivka' in file:
            files.append(os.path.join(r, file))

for f in files:
    print(f)
