    """batch_resize_apriltag.py
    wget https://april.eecs.umich.edu/media/apriltag/tag36h11.tgz
    tar -xvzf ./tag36h11.tgz
    python batch_resize_apriltag.py
    """

from utilis import mkdir, seq_file_filter_png
import argparse
import os

def batch_resize(SOURCE_DIR, DIST_DIR, START, END):

    #SOURCE_DIR = './tag36h11/'
    #DIST_DIR = './tag36h11_big/'
    files = os.listdir(SOURCE_DIR)
    # filter mp4 files
    pngList = list(filter(seq_file_filter_png, files))
    mkdir(DIST_DIR)
    for pngName in pngList[START-1:END]:
        print("=== " + pngName + " ===")
        
        sourceLoc = SOURCE_DIR + pngName
        distLoc = DIST_DIR + pngName[:-4] + '_big.png'
        
        # use convert
        # convert tag36_11_00000.png -scale 5000% tag36_11_00000_big.png
        os.system("convert " + sourceLoc + 
                  " -scale 5000% " + distLoc)
        
        print(pngName + " finished!")

    print("=== Finished! ===")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--start', default=1, type=int)
    parser.add_argument('--end', type=int)
    args = parser.parse_args()
    
    SOURCE_DIR = './tag36h11/'
    DIST_DIR = './tag36h11_big/'
    batch_resize(SOURCE_DIR, DIST_DIR, args.start, args.end)