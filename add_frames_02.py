
import shutil
import os

allFrame = 0
countClips = 0
countDir = 0
currentPath = 'D:\\TSLT\\PyCharm\\SplitFrames\\clips\\'
for folderName in os.listdir(currentPath):
    if folderName[0] == 'D':
        #        print(folderName)
        path_of_the_directory = currentPath + folderName + '\\'
        print(path_of_the_directory)
        countDir += 1
        for folder in os.listdir(path_of_the_directory):
            count = 0

            if folder[-4:] != '.mp4' and folder != 'desktop.ini':
                print(folder)
                countClips += 1
                for files in os.listdir(path_of_the_directory + folder + '\\'):
                    count += 1
                    allFrame += 1
                print('Files = ', count)

                if count == 74:
                    print('=====>' + path_of_the_directory + folder + '\\')
                    src = path_of_the_directory + folder + '\\' + folder + '-74.jpg'
                    dest = path_of_the_directory + folder + '\\' + folder + '-75.jpg'
                    newfile74 = shutil.copyfile(src, dest)
                    allFrame += 1
                    print('')

                if count == 73:
                    print('=======>' + path_of_the_directory + folder + '\\')
                    src = path_of_the_directory + folder + '\\' + folder + '-73.jpg'
                    dest = path_of_the_directory + folder + '\\' + folder + '-74.jpg'
                    dest2 = path_of_the_directory + folder + '\\' + folder + '-75.jpg'
                    newfile73 = shutil.copyfile(src, dest)
                    newfile74 = shutil.copyfile(src, dest2)
                    allFrame += 2
                    print('')

                if count == 72:
                    print('=======>' + path_of_the_directory + folder + '\\')
                    src = path_of_the_directory + folder + '\\' + folder + '-72.jpg'
                    dest = path_of_the_directory + folder + '\\' + folder + '-73.jpg'
                    dest2 = path_of_the_directory + folder + '\\' + folder + '-74.jpg'
                    dest3 = path_of_the_directory + folder + '\\' + folder + '-75.jpg'
                    newfile72 = shutil.copyfile(src, dest)
                    newfile73 = shutil.copyfile(src, dest2)
                    newfile74 = shutil.copyfile(src, dest3)
                    allFrame += 2
                    print('')

                if count == 71:
                    print('=======>' + path_of_the_directory + folder + '\\')
                    src = path_of_the_directory + folder + '\\' + folder + '-71.jpg'
                    dest = path_of_the_directory + folder + '\\' + folder + '-72.jpg'
                    dest2 = path_of_the_directory + folder + '\\' + folder + '-73.jpg'
                    dest3 = path_of_the_directory + folder + '\\' + folder + '-74.jpg'
                    dest4 = path_of_the_directory + folder + '\\' + folder + '-75.jpg'
                    newfile71 = shutil.copyfile(src, dest)
                    newfile72 = shutil.copyfile(src, dest2)
                    newfile73 = shutil.copyfile(src, dest3)
                    newfile74 = shutil.copyfile(src, dest4)
                    allFrame += 2
                    print('')

                if count == 70:
                    print('=======>' + path_of_the_directory + folder + '\\')
                    src = path_of_the_directory + folder + '\\' + folder + '-70.jpg'
                    dest = path_of_the_directory + folder + '\\' + folder + '-71.jpg'
                    dest2 = path_of_the_directory + folder + '\\' + folder + '-72.jpg'
                    dest3 = path_of_the_directory + folder + '\\' + folder + '-73.jpg'
                    dest4 = path_of_the_directory + folder + '\\' + folder + '-74.jpg'
                    dest5 = path_of_the_directory + folder + '\\' + folder + '-75.jpg'
                    newfile71 = shutil.copyfile(src, dest)
                    newfile72 = shutil.copyfile(src, dest2)
                    newfile73 = shutil.copyfile(src, dest3)
                    newfile74 = shutil.copyfile(src, dest4)
                    newfile75 = shutil.copyfile(src, dest5)
                    allFrame += 2
                    print('')

        print('')

print('All Clips = ', countClips)
print('All Image Frames = ', allFrame)
print('Number of Directory = ', countDir)