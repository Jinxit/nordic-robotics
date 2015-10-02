#!/usr/bin/python2

import sys
import os
import fileinput
from subprocess import call, check_output

tag = ""
if len(sys.argv) > 1:
    tag = "--branch %s " % sys.argv[1]

dir = os.getcwd() + "/"

with open("deps.txt") as f:
    for line in f:
        folder = line.split("/")[-1:][0][:-5]
        call(("mkdir -p %s" % folder).split(" "))
        os.chdir(folder)
        unpushed = check_output("git log origin/master..master".split(" "))
        uncommitted = check_output("git status --porcelain".split(" "))
        problem = ""
        problem_text = ""

        if unpushed:
            problem = "unpushed"
            problem_text = problem_text + "Unpushed:\n" + unpushed + "\n"
        if uncommitted:
            problem = "uncommitted"
            problem_text = problem_text + "Uncommitted:\n" + uncommitted + "\n"

        if problem:
            print problem_text
            choice = raw_input("%s has %s changes! Do you wish to overwrite changes? (y/n) " % (folder, problem))
            while choice != "y" and choice != "n":
                choice = raw_input("Make a choice, nerd! (y/n) ")
            if choice == "n":
                print "Aborting..."
                sys.exit(0)

        os.chdir(dir)
        call(("rm -R -f %s" % (folder)).split(" "))
        call(("git clone %s--depth=1 %s" % (tag, line)).split(" "))