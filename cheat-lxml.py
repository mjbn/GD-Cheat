#!/bin/python3
from sys import argv
from lxml import etree as et
from subprocess import run
from os.path import join
from requests import get
from bs4 import BeautifulSoup as bs
from time import sleep


print(argv)
if argv[1]=="get":
    git_url="https://github.com/godotengine/godot.git"
    repo_dir="./gd"
    subdir = "doc/classes"
    headers = {'User-Agent': 'Jodzilla/1.0 (Arch Gnu Linux 6.1.1)'}
if argv[1]=="make":
    mdir = run(["ls", "-la", join(repo_dir,subdir)], capture_output=True, text=True).stdout
    filename=[]
    for f in mdir.splitlines():
            d = f.split()
            if d[8]=="." or d[8]=="..":
                continue
            if d[0][0] == "-":
                if filename!=None and isinstance(filename, list):
                    filename.append(join(repo_dir,subdir,d[8]))
            elif d[0][0] == "d":
                continue

    for f in filename:
        tree = etree.parse(f)

