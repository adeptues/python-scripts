#!/usr/bin/python

import zipfile


def unlock(zfile,passWord):
    try:
        zfile.extractall(pwd=line)
        return True
    except Exception, e:
        return False


def main():
    zfile = zipfile.ZipFile('evil.zip','r')
    passfile = open('dictionary.txt','r')
    for line in passfile.readlines():
        line = line.strip('\n')
        guess = unlock(zipfile,line)
        print "[*] Found password: "+line
        if guess:
            exit(0)


#main method
if  __name__ =='__main__':main()
