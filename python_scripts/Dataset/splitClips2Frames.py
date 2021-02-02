from utilis import mkdir, seq_file_filter
import argparse
import os

def split_clips_to_frames(CLIPS_DIR, FRAMES_DIR, START, END):
    #CLIPS_DIR = './JAAD_clips/'
    #FRAMES_DIR = './JAAD_frames/'
    files = os.listdir(CLIPS_DIR)
    # filter mp4 files
    videoList = list(filter(seq_file_filter, files))
    mkdir(FRAMES_DIR)
    for videoName in videoList[START-1:END]:
        print("=== " + videoName + " ===")
        
        videoLoc = CLIPS_DIR + videoName
        videoFrameDir = FRAMES_DIR + videoName[:-4] + '/'
        mkdir(videoFrameDir)
        
        # use ffmpeg
        os.system("ffmpeg -i " + videoLoc + 
                  " -start_number 0 -f image2 -qscale 1 " +
                  videoFrameDir + "/%05d.png")
        
        print(videoName + " finished!")

    print("=== Finished! ===")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', default=1, type=int)
    parser.add_argument('--end', type=int)
    args = parser.parse_args()
    
    #CLIPS_DIR = './JAAD_clips/'
    #FRAMES_DIR = './JAAD_frames/'
    CLIPS_DIR = 'H:/Dataset/JAAD_clips/'
    FRAMES_DIR = 'H:/Dataset/JAAD_imgs/'
    split_clips_to_frames(CLIPS_DIR, FRAMES_DIR, args.start, args.end)

# python .\splitClips2Frames.py --start 241 --end 291