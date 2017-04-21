#!/bin/python

import sys
# Converts a java properties file to json map

def read_file(file_path):
    lines = []
    f = open(file_path,'rb')
    for line in f:
        lines.append(line)
    f.close()
    return lines

def write_json(jmap):
    file_name = "map.json"
    print str(jmap)


def do_work(lines):
    out = {}
    for line in lines:
        if line[0] is not '#':
            items = line.split('=')
            if len(items) == 2:
                out.update({items[0].strip():items[1].strip()})
    return out

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print "first argument must be the properties file"
        sys.exit()
    file_path = sys.argv[1]
    if file_path is None:
        print "first argument must be the properties file"
        sys.exit()
    
    lines = read_file(file_path)
    jmap = do_work(lines)
    write_json(jmap)
