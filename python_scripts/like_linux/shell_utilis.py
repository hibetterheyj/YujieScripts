import os

## make a dir just as in Linux
def mkdir(path):
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print(path + " created successfully")
        return True
    else:
        print(path + " already exists")
        return False


## filter files with specfic extensions
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

"""
Reference:
1. https://stackoverflow.com/questions/5351766/use-fnmatch-filter-to-filter-files-by-more-than-one-possible-file-extension
"""
