import urllib.request
import argparse
import os
from utilis import mkdir
        
videoSet = {1:4, 2:3, 3:19, 4:16, 5:2, 6:9}

def VideoSetDL(setNum):
    url =  "http://data.nvision2.eecs.yorku.ca/PIE_dataset/PIE_clips/"
    baseFolder = './PIE_dataset/'
    videoBaseName = 'video_00' # 后续使用videoNum.zfill(2)补足
    ext = '.mp4'
    #print(videoSet[setNum])
    setName = 'set0' + str(setNum) + '/'
    setFolder = baseFolder + setName
    setURL = url + setName
    mkdir(setFolder)
    for i in range(start, videoSet[setNum]):
        videoNum = str(i+1)
        videoName = videoBaseName + str(videoNum.zfill(2)) + ext
        videoURL = setURL + videoName
        videoLoc = setFolder + videoName
        print(videoName + ' Started !')
        urllib.request.urlretrieve(videoURL, videoLoc)
        print(videoName + ' Finished !')
    print(setFolder + ' Finished !')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("setNum", help="targeted set number",
                        type=int)
    parser.add_argument('--start', default=1, type=int)
    args = parser.parse_args()
    start = args.start-1
    VideoSetDL(args.setNum)