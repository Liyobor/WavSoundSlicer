from tqdm import tqdm
import Ray_Python_Tools
import os
from os.path import join,split
path = input('input\n')
explorer = Ray_Python_Tools.SimpleFileExplorer()
explorer.walk(path)



classCount = {}

sortTable = {}

def indexFiles(classCount):
    for index,file in enumerate(tqdm(explorer.files)):
        # print(file)
        # print(os.path.split(file)[1])

        if "inf" in file:
            print(f"remove {file}")
            os.remove(file)
            continue
        fileNameTail = split(file)[1]
        # split(file)
        volume = fileNameTail[0:5]
        label = fileNameTail[7:9]
        # print(volume)
        # print(label)

        if(label in classCount):
            classCount[label]+=1
            
        else:
            
            classCount[label]=1
    classCount = dict(sorted(classCount.items()))
    return classCount


def buildSortTable(classcount):
    index = 0
    for key in classcount:
        if(index<10):
            sortTable[key] = "0" + str(index)
        else:
            sortTable[key] = str(index)
        index+=1
    return sortTable
# print(sortTable)

def renameFile(tabel):
    c = 0

    for index,file in enumerate(tqdm(explorer.files)):


        fileNameTail = split(file)[1]
        fileNameHead = split(file)[0]
        label = fileNameTail[7:9]
        if(label==tabel[label]):
            continue

        newFileNameTail = fileNameTail[:7]+tabel[label]+fileNameTail[9:]
        # if(c<10):
        #     print(fileNameTail)
        #     print(newFileNameTail)
        #     print("-"*8)
        # c+=1
        os.rename(file,join(fileNameHead,newFileNameTail))


classCount = indexFiles(classCount)

sortTable = buildSortTable(classCount)
# print(sortTable)
explorer.walk(path)
renameFile(sortTable)

print(classCount)

        