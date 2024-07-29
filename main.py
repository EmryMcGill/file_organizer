# author: Emry McGill

# imports
import os, re, shutil, yaml, sys, PyInquirer
from tkinter import filedialog

# define paths
src = os.path.join(os.path.expanduser('~'), 'downloads')
docs = '/home/emry/Documents/docs'
photos = '/home/emry/Pictures'
media = '/home/emry/Documents/media'
misc = '/home/emry/Documents/misc'



def main():
    pass


def organize():
    # validate src folder
    global src
    if src == '':
        return False
    if src == os.path.expanduser('~'):
        return False

    # get list of all files in the downloads folder
    files = os.listdir(src)

    # for all files in list, check file type and move into proper folder
    for file in files:
        # check if its a file or dir
        if os.path.isfile(os.path.join(src, file)):
            moveFile(file)
        else:
            moveDir(file)
    return True
    
# function that takes a file as input, gets the extension and moves it to the appropriate place
def moveFile(file):
    # get file extension
    ext = re.split(r'[.]', file).pop()
    # put in correct destination
    if ext == 'pdf' or ext == 'odt' or ext == 'xls':
        os.rename(os.path.join(src, file), os.path.join(docs, file))
    elif ext == 'mp4' or ext == 'mp3':
        os.rename(os.path.join(src, file), os.path.join(media, file))
    elif ext == 'jpg' or ext == 'png':
        os.rename(os.path.join(src, file), os.path.join(photos, file))
    else:
        os.rename(os.path.join(src, file), os.path.join(misc, file))


def moveDir(dir):
    # check if its media
    if re.search('1080p', dir):
        shutil.move(os.path.join(src, dir), os.path.join(media, dir))
    else:
        shutil.move(os.path.join(src, dir), os.path.join(misc, dir))


def chooseFolder(label):
    global src
    src = filedialog.askdirectory()
    label.set(src)



if __name__ == '__main__':
    main()