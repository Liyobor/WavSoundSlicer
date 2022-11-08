import os
path = input('input\n')
dirNameList = os.listdir(path)
dirNameList.sort()
for index,file in enumerate(dirNameList):
    fullFilePath = os.path.join(path,file)
    fileNameTail = os.path.split(fullFilePath)[1]
    classLabel = fileNameTail[0:fileNameTail.index('_')]
    print(classLabel)
    # print(f"fileNameEndPosition = {fileNameEndPosition}")
    # print(f"fileNameStartPosition = {fileNameStartPosition}")
    
