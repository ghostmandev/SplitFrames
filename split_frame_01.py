import cv2
import imageio
import os
import shutil
from moviepy.editor import *

def getFrame(sec,nameFiles):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    #cv2.putText(image,str(count),(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,255,0),cv2.LINE_4)
    if hasFrames:
#         nameF = nameFiles.translate({ord(i):None for i in '.mp4'})
        nameF = filename[:-4]
        os.chdir(path_of_the_directory+nameF)
        frame = cv2.imwrite(nameF + '-' + str(count) + ".jpg", image)  # save frame as JPG file
    return hasFrames

def createFolder(filename):
#     print('xxxxxxx ==>', filename)
#     nameF = filename.translate({ord(i):None for i in '.mp4'})  # delete .mp4
    nameF = filename[:-4]
#     print('yyyyyy ==>', nameF)
    try:
        os.mkdir(path_of_the_directory+nameF)  # Create target Directory
        print("Directory " , nameF ,  " Created ")
    except FileExistsError:
        print("Directory " , nameF ,  " already exists")

def duration(filename,path_of_the_directory):
    clip = VideoFileClip(path_of_the_directory + filename)
    duration = clip.duration
    ChargeRate = round(duration/75,6)             # 75 average frame per clips
    print("Duration : " + str(duration) + '  ' + 'seconds')
    print("Frame Rate : " + str(ChargeRate) + '  ' + 'seconds/Frames')
    return ChargeRate


currentPath = 'D:\\TSLT\\PyCharm\\SplitFrames\\clips\\'
# frameRate = 0.04
allFrame = 0
countDir = 0
countClips = 0
for folderName in os.listdir(currentPath):
    if folderName[0] == 'D':
        path_of_the_directory = currentPath + folderName + '/'
        print(path_of_the_directory)
        countDir = countDir + 1
        eachFolderFrame = 0
        for filename in os.listdir(path_of_the_directory):
            if (filename != '.DS_Store') and (filename != 'desktop.ini'):
                sec = 0
                count = 1
                countClips = countClips + 1
                print(filename)
                frameRate = duration(filename, path_of_the_directory)
                path = os.path.join(path_of_the_directory, filename)
                newfolder = createFolder(filename)
                vidcap = cv2.VideoCapture(path)
                success = getFrame(sec, filename)
                while success:
                    count = count + 1
                    eachFolderFrame = eachFolderFrame + 1
                    allFrame = allFrame + 1
                    sec = sec + frameRate
                    sec = round(sec, 6)
                    success = getFrame(sec, filename)
                print('Image Frames = ', count - 1)

        print('In Folder Frame', eachFolderFrame)
        print('')
print('All Clips = ', countClips)
print('All Image Frames = ', allFrame)
print('Average Frame = ', allFrame / countClips)
print('Number of Directory = ', countDir)