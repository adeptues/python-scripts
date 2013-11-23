#!/usr/bin/python

import os
import glob

# All files in a dir with a given extention
def all_files(path,ext):
    os.chdir(path)
    files =  glob.glob(ext)
    return files


# Gets all the dirs in a directory
def all_dirs(path):
    dirs = os.listdir(path)
    return dirs

# build the csv into a dict
def build_csv(dirs,path,ext):
    data = {}
    for i in range(len(dirs)):
        dir = dirs[i]
        files = all_files(path + "/"+dir,ext)
        for file in files:
            filepath = path + "/"+dir+"/"+file
            data[filepath] = i
    return data

# output csv to file
def write_csv(data):
    f = open('csv_file','w')
    for k,v in data.iteritems():
        out = k+","+str(v)+"\n"
        print out
        f.write(out)
    f.close()

cwd = os.getcwd()        
path  = "/home/adeptues/pycv/faces/facedb"

ext = "*.pgm"

dirs = all_dirs(path)

data = build_csv(dirs,path,ext)

os.chdir(cwd)

write_csv(data)

