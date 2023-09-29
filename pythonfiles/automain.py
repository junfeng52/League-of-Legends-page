import numpy as np
import re

def replacefile(newfile):
    with open("main.html", mode="w") as file:
        file.write(newfile)

with open("main.html", mode="r") as file:
    fileread = file.read()
    pattern = r"https:\/\/images\.contentstack\.io\/v3\/assets\/[a-zA-Z0-9]+\/[a-zA-Z0-9]+\/[a-zA-Z0-9]+\/"
    newtext = re.findall(pattern, fileread)
    for text in newtext:
        fileread = fileread.replace(text,"Imgenes/")
        replacefile(fileread)
