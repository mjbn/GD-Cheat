#!/bin/python3
from sys import argv
from lxml import etree as et
from git import Repo
from subprocess import run
from os.path import join


print(argv)
if argv[1]=="clone":
    git_url="https://github.com/godotengine/godot.git"
    repo_dir="./gd"
    subdir = "doc/classes"
    rep = Repo.clone_from(git_url, repo_dir, no_checkout=True)
    rep.git.sparse_checkout("init")
    rep.git.sparse_checkout("set", subdir)
    rep.git.checkout("main")
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

