# -*- coding: utf-8 -*-

import os

def readFile():
    print os.path.join(os.path.dirname(__file__),'test1.txt')
    with open(os.path.join(os.path.dirname(__file__),'test1.txt').replace("\\","/"), 'r') as f:
        data = f.read()
        print data

readFile()