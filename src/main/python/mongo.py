# -*- coding: utf-8 -*-
# @Author: Alexander Sharov

import json
import gridfs

from pymongo import MongoClient
from datetime import datetime


def connect(url='mongodb://localhost:27017/', db_name='experiments'):
    client = MongoClient(url)
    db = client[db_name]
    return db

def write(db, collection, file, mesh_type, mesh_name, time, exp_name):
    fs = gridfs.GridFS(db)

    # r - если текстовые файлы
    # rb - если бинарные

    logsFile = fs.put(open(file, 'r'))

    record = {
        "exp_name": exp_name,
        "date": datetime.now().strftime("%Y-%m-%d-%H-%M"),
        "files": {
            "logs": logsFile
        },
        "meta": {
            "mesh": {
                "type": mesh_type,
                "name": mesh_name
            },
            "execution_time": str(time)
        }
    }
    db[collection].insert(record)


def read(db, collection, date):
    return db[collection].find_one({"date": date})
