import os

path = input('input\n')
path2 = input('input\n')
dirNameList = os.listdir(path)
dirNameList.sort()

dirNameList2 = os.listdir(path2)
dirNameList2.sort()
dl = []
dl2 = []

for dir in dirNameList:
    dl.append(dir[0:3])


for dir in dirNameList2:
    dl2.append(dir[0:3])

print(dl)
print(dl2)
