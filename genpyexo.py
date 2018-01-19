#!/usr/bin/python3

VERSION = "0.2"

from sys import exit, argv, stdin, stdout, stderr
from optparse import OptionParser

parser = OptionParser(usage="usage: %prog [options] exercice.dat", version="%prog {}".format(VERSION))
parser.set_defaults(force=False)
parser.set_defaults(model="modele.html")
parser.add_option("-f", "--force", action="store_true", dest="force", help="continue when unknown entry type met")
parser.add_option("-m", "--model", action="store_true", dest="model", help="use given model html file as template")
options, args = parser.parse_args()
Force = options.force
Model = options.model

if len(args) == 1:
    filename = args[0]
else:
    parser.error("incorrect number of arguments")


try:
    with open(Model) as file:
        modele = file.read()
except FileNotFoundError:
    print(Model + " file is missing", file=stderr)
    exit(1)


def readblock(file):
    block = ""
    for ligne in file:
        if ligne[:3] == "===":
            break
        block += ligne
    return block


try:
    with open(filename) as file:
        titre1 = readblock(file).rstrip("\n")
        titre2 = readblock(file).rstrip("\n")
        enonce = readblock(file)
        pyresp = readblock(file)
        jstest = readblock(file).rstrip("\n")
        pycode = readblock(file)
except FileNotFoundError:
    print(filename + " file is missing", file=stderr)
    exit(1)

modele = modele.replace("##TITRE1##", titre1)
modele = modele.replace("##TITRE2##", titre2)
modele = modele.replace("##ENONCE##", enonce)
modele = modele.replace("##PYRESP##", pyresp)
modele = modele.replace("##JSTEST##", jstest)
modele = modele.replace("##PYCODE##", pycode)

if filename[-4:] == ".dat":
    filename = filename[:-4]

try:
    with open(filename+".html", "w+") as file:
        file.write(modele)
except FileNotFoundError:
    print(filename+".html" + " can't be written", file=stderr)
    exit(1)

