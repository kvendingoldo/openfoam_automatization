# -*- coding: utf-8 -*-
# @Author: Alexander Sharov

import sys, getopt
from mongo import *

def main(args):
    db = ''
    collection = ''
    directory = ''
    mesh_type = ''
    mesh_name = ''
    time = ''
    exp_name = ''

    try:
        opts, args = getopt.getopt(argv,"hd:c:f:m:t:e:",["database=","collection=","file=","mesh=","type=","time="])
    except getopt.GetoptError:
        print('main.py -d <db> -c <collection> -f <file> -m <mesh> --type <mesh_type> -t <time> -e <exp_name>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('main.py -d <db> -c <collection> -f <file> -m <mesh> --type <mesh_type> -t <time> -e <exp_name>')
        if opt in ("-d", "--database"):
            db = arg
        elif opt in ("-c", "--collection"):
            collection = arg
        elif opt in ("-f", "--file"):
            directory = arg
        elif opt in ("-m", "--mesh"):
            mesh_name = arg
        elif opt in ("--type"):
            mesh_type = arg
        elif opt in ("-t", "--time"):
            time = arg
        elif opt in ("-e"):
            exp_name = arg

    write(db, collection, directory, mesh_type, mesh_name, time, exp_name)

if __name__ == "__main__":
    main(sys.argv[1:])
