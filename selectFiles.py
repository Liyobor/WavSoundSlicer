from datetime import datetime
from tqdm import tqdm
import Ray_Python_Tools
import os
from os.path import join,split
import numpy
import shutil

path = input('input\n')
explorer = Ray_Python_Tools.SimpleFileExplorer()
explorer.walk(path)

label_filename_map = {}

for index,file in enumerate(tqdm(explorer.files)):
    fileNameTail = split(file)[1]
    fileNameHead = split(file)[0]
    label = fileNameTail[7:9]
    if label in label_filename_map:
        label_filename_map[label].append(file)
    else:
        label_filename_map[label] = [file]

for key in tqdm(label_filename_map):
    selectedFiles = numpy.random.choice(label_filename_map[key],150,False)
    date = datetime.now().strftime("%m%d")
    selectedFilesHead = split(selectedFiles[0])[0]
    selectedFilesTail = split(selectedFiles[0])[1]
    newFolder = join(split(selectedFilesHead)[0],date+"_selected_Sliced")

    if not os.path.exists(newFolder):
        os.mkdir(newFolder)
    for file in selectedFiles:
        shutil.copyfile(file,join(newFolder,split(file)[1]))
    print(selectedFiles)
