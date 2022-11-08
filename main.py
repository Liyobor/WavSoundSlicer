import tqdm
import Ray_Python_Tools
from Counter import Ray_Counter
import random
from datetime import datetime
path = input('input\n')
explorer = Ray_Python_Tools.SimpleFileExplorer()
slicer = Ray_Python_Tools.WavSlicer()
c = Ray_Counter(5)
explorer.walk(path)
map_combine = {}
map_notcombine = {}
errorFileList = []

labelDict = {}
# explorer.getCurrentPath()


# slice length,unit:ms
lengthOfSlicedSound = 2000

explorer.sortDirs()
for dir in tqdm.tqdm(explorer.dirs):
    explorer.walk(dir)
    for file in tqdm.tqdm(explorer.files,leave=False):
    # for file in explorer.files:
        try:
        
            slicer.loadWavFile(file,16000)
            fileNameEndPosition = file.rindex('\\')
            fileNameStartPosition = file[:file.rindex('\\')].rindex('\\')
        
            # example:
            # file = C:\\Users\\Aurismart_Ray\\Desktop\\0914_organized\\0914_organized_0912\\000FireAlarmA\\{filename}
            # so fileNameEndPosition = Last Index Of (C:\\Users\\Aurismart_Ray\\Desktop\\0914_organized\\0914_organized_0912\\000FireAlarmA\\ <-here )
            # fileNameStartPosition = Last Index Of (C:\\Users\\Aurismart_Ray\\Desktop\\0914_organized\\0914_organized_0912\\ <-here )


            # catch the abbreviation from filename
            classLabel = file[fileNameStartPosition+1:fileNameStartPosition+4]


            # label coding
            if classLabel not in labelDict:
                labelDict[classLabel] = len(labelDict)


            labelNumber = str(labelDict[classLabel])
            if len(labelNumber) == 1:
                labelNumber = "00"+str(labelNumber)
            elif len(labelNumber) == 2:
                labelNumber = "0"+str(labelNumber)
                
                

            sliceStartMillisecond = 0

            

            # stop when file remaining length not enough
            while(sliceStartMillisecond+lengthOfSlicedSound<slicer.wav_duration):

                
                slicer.cut(sliceStartMillisecond,sliceStartMillisecond+lengthOfSlicedSound)

                # align file name
                if(slicer.soundAfterSlice.max_dBFS+100 >=100):
                    newFileName = (str((slicer.soundAfterSlice.max_dBFS+100)*100)[0:5]+'_'+labelNumber+'_'+classLabel+'_'+c.getFormattedCount())+'.wav'
                else:
                    newFileName = ('0'+str((slicer.soundAfterSlice.max_dBFS+100)*100)[0:4]+'_'+labelNumber+'_'+classLabel+'_'+c.getFormattedCount())+'.wav'


                # get date,2022-09-20 -> date = 0920
                date = datetime.now().strftime("%m%d")
                # set folder name
                
                newFolder = path[0:path.rindex('\\')]+'\\'+date+f'_sliced_{int(lengthOfSlicedSound/1000)}s'+'\\'+classLabel

                # save sliced file
                slicer.exportCuttedWav(newFileName,newFolder)

                # decide start point of next wav slice
                sliceStartMillisecond+=random.randint(100,500)

                # c is a counter for wav filename coding
                c.plusOne()
            
        except Exception as e:
            # if file have errors,keep its filename
            errorFileList.append(file)
            print('filename = ',file)
            print('error message = ',e)
        # slicer.cut()
    c.resetCount()
# show error file
print(errorFileList)
# print(f"save at {os.path.split(newFolder)[0]}")