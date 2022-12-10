with open("Day7\input.txt") as file:
    lines = file.read().strip().split("\n")


folders = set()
foldersdetail = {}
files = {}
curdir = []

for line in lines:
    if line.startswith("$"):
        if line.startswith("$ cd"):
            if line.startswith("$ cd .."):
                curdir.pop()
            else:
                curdir.append(line[5:])
    else:
        if line.startswith("dir"):
            folders.add("/".join(curdir) + "/" + line[4:])
        if line.split()[0].isnumeric():
            size, name = line.split()
            files["/".join(curdir) + "/" + name] = int(size)

for folder in folders:
    foldersize = 0
    for name, size in files.items():
        if name.startswith(folder):
            foldersize += size
        foldersdetail[folder] = foldersize

part1size = 0
for foldername, foldersize in foldersdetail.items():
    if foldersize <= 100000:
        part1size += foldersize
    print(foldername, foldersize)
print("The answer to Part 1 is:", part1size)

totalspace, usedspace, neededspace = 70000000, 0, 30000000
for _, size in files.items():
        usedspace += size
freespace = totalspace - usedspace
deletespace = 30000000 - freespace

smallestfolder = 70000000
for foldername, foldersize in foldersdetail.items():
    if foldersize >= deletespace and foldersize < smallestfolder:
        smallestfolder = foldersize
print("The answer to Part 2 is:", smallestfolder)