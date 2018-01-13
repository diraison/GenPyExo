#!/usr/bin/python3

VERSION = "0.1"

from sys import exit, argv, stdin, stdout, stderr
from optparse import OptionParser

parser = OptionParser(usage="usage: %prog [options] exercice.dat", version="%prog {}".format(VERSION))
parser.set_defaults(force=False)
parser.add_option("-f", "--force", action="store_true", dest="force", help="continue when unknown entry type met")
options, args = parser.parse_args()
Force = options.force

if len(args) == 1:
    filename = args[0]
else:
    parser.error("incorrect number of arguments")


try:
    with open("modele.html") as file:
        modele = file.read()
except FileNotFoundError:
    print("modele.html file is missing", file=stderr)
    exit(1)

try:
    with open(filename) as file:
        titre1 = file.readline().rstrip("\n")
        titre2 = file.readline().rstrip("\n")
        enonce = file.readline().rstrip("\n")
        pyresp = file.readline().rstrip("\n")
        jsinpt = file.readline().rstrip("\n")
        pycode = file.read().rstrip('\n')
except FileNotFoundError:
    print(filename + " file is missing", file=stderr)
    exit(1)

modele = modele.replace("##TITRE1##", titre1)
modele = modele.replace("##TITRE2##", titre2)
modele = modele.replace("##ENONCE##", enonce)
modele = modele.replace("##PYRESP##", pyresp)
modele = modele.replace("##JSINPT##", jsinpt)
modele = modele.replace("##PYCODE##", pycode)

if filename[-4:] == ".dat":
    filename = filename[:-4]

try:
    with open(filename+".html", "w+") as file:
        file.write(modele)
except FileNotFoundError:
    print(filename+".html" + " can't be written", file=stderr)
    exit(1)

