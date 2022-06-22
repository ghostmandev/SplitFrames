
import os

allFrame = 0
countsubFolder = 0
countDir = 0
currentPath = 'D:\\TSLT\\PyCharm\\SplitFrames\\clips\\'
for folderName in os.listdir(currentPath):
    if folderName[0] == 'D':
        path_of_the_directory = currentPath + folderName + '\\'
        countDir += 1
        for folder in os.listdir(path_of_the_directory):
            count = 0
            if folder[-4:] != '.mp4' and folder != 'desktop.ini':
                countsubFolder += 1
                for files in os.listdir(path_of_the_directory + folder + '\\'):
                    count += 1
                    allFrame += 1
                    # print(files)
                if count != 75:
                    print('Files = ', path_of_the_directory + folder + '\\')

print('All Image Frames = ', allFrame)
print('Number of Sub Directory = ', countsubFolder)
print('Number of Directory = ', countDir)