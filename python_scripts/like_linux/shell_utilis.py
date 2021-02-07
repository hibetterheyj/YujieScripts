import os

## TODO: list files with specfic extensions

## make a dir just as in Linux
def mkdir(path):
    import os
    path=path.strip()
    path=path.rstrip("\\")
    isExists=os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print(path+' created successfully')
        return True
    else:
        print(path+' already exists')
        return False
    
## filter files with specfic extensions
# TODO: write a class
# example:
# files = os.listdir(CLIPS_DIR)
# videoList = list(filter(seq_file_filter, files))
def img_file_filter(f):
    if f[-4:] in ['.jpg', '.png', '.bmp']:
        return True
    else:
        return False

def seq_file_filter_mp4(f):
    if f[-4:] in ['.mp4']: # , '.avi', '.mov'
        return True
    else:
        return False

# Reference:
# stackoverflow - https://stackoverflow.com/questions/974071/python-library-for-playing-fixed-frequency-sound
# https://stackoverflow.com/questions/974071/python-library-for-playing-fixed-frequency-sound