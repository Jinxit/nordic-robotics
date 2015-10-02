#!/usr/bin/python2

import sys
import fileinput
from subprocess import call

tag = ""
if len(sys.argv) > 1:
    tag = "--branch %s " % sys.argv[1]

with open("deps.txt") as f:
    for line in f:
        folder = line.split("/")[-1:][0]
        call(("rm -R -f %s" % (folder)).split(" "))
        call(("git clone %s--depth=1 %s" % (tag, line)).split(" "))