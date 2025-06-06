#!/bin/python3
from sys import argv
from lxml import etree as et
from git import Repo


print(argv)
if argv[1]=="clone":
    git_url="https://github.com/godotengine/godot.git"
    repo_dir="./gd"
    Repo.clone_from(git_url, repo_dir)
