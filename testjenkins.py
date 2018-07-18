# -*- coding: utf-8 -*-

import os

def readFile():
    print os.path.join(os.path.dirname(__file__),'test1.txt')
    with open(r'D:/workspace_python/hello/test1.txt', 'r') as f:
        data = f.read()
        print data

readFile()
