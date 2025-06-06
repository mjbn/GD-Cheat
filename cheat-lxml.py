#!/bin/python3
from sys import argv
from lxml import etree as et
from subprocess import run
from os.path import join
from requests import get
from bs4 import BeautifulSoup as bs
from time import sleep
from os import makedirs
import json


headers = {'User-Agent': 'Jodzilla/1.0 (Arch Gnu Linux 6.1.1)'}
repo_dir="./gd"
subdir = "doc/classes"


if argv[1]=="get":
    doc_url="https://github.com/godotengine/godot/tree/master/doc/classes"
    page = get(doc_url, headers=headers)
    soup = bs(page.text, "html.parser")
    page.close()
    links = soup.find_all('script', type='application/json')
    data = json.loads(links[len(links)-1].text)
    cleanData = data["payload"]["tree"]["items"]
    #print(data["payload"]["tree"]["items"])
    #print(len(data["payload"]["tree"]["items"]))
    with open('class.json', 'w') as fp:
        json.dump(cleanData, fp)
    print("Please wait for 5 seconds")
    sleep(5)
    print("Done.")


if argv[1]=="dlxml":
    makedirs(join(repo_dir,subdir),exist_ok=True)
    ## Downloading XML
    raw_url ="https://raw.githubusercontent.com/godotengine/godot/refs/heads/master/doc/classes/"
    with open('class.json', 'r') as f:
        data = json.load(f)
    for i in data:
        print(i["name"])
        xmlf = get(raw_url+i["name"], headers=headers)
        with open(join(repo_dir,subdir,i["name"]), "w") as x:
            x.write(xmlf.text)

if argv[1]=="mktex":
    pass

if argv[1]=="make":
    pass



