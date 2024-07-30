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
    initialize()

    organize()

def initialize():
    # get the configuration settings from file
    global conf
    with open('conf.yaml', 'r') as f:
        conf = yaml.safe_load(f)

    # loop conf to set default paths
    if conf['src']['path'] == 'default':
        conf['src']['path'] = os.path.join(os.path.expanduser('~'), 'Downloads')

    for key, val in conf['dest'].items():
        if val['path'] == 'default':
            # set to default path
            conf['dest'][key]['path'] = os.path.join(os.path.expanduser('~'), 'Documents', key)
            # make sure the dest folder exists
            try:
                os.mkdir(os.path.join(os.path.expanduser('~'), 'Documents', key))
            except:
                continue

def organize():
    # validate src folder
    if conf['src']['path'] == '':
        return False
    if conf['src']['path'] == os.path.expanduser('~'):
        return False

    # get list of all files in the downloads folder
    files = os.listdir(conf['src']['path'])

    # for all files in list, check file type and move into proper folder
    for file in files:
        # check if its a file or dir
        if os.path.isfile(os.path.join(conf['src']['path'], file)):
            moveFile(file)
        else:
            moveDir(file)
    return True
    
# function that takes a file as input, gets the extension and moves it to the appropriate place
def moveFile(file):
    # get file extension
    ext = re.split(r'[.]', file).pop()
    
    # put in correct destination
    
    # loop over possible destinations until a ext match is found 
    for key, val in conf['dest'].items():
        for item in val['extensions']:
            # check if ext match
            if ext == item:
                # move file to current type
                os.rename(os.path.join(conf['src']['path'], file), os.path.join(conf['dest'][key]['path'], file))


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