#!/usr/local/bin/python
import os
import re

# title: Generate a README file for this repo
# description: Looks through all the files and writes a markdown file to README.md
# description: has a list of exclude file patterns (e.g. *.swp) and directories (e.g. .git, readme files, this file)

path = "./"
contents="# LeetCode Solutions  \nThis repository has unofficial solutions to the challenges at https://leetcode.com/problemset/all/  \n  \n"

excludefiles = ['.*\.swp', os.path.basename(__file__),'CONTRIBUTING.md', 'README.md']
# excluded directories should be comma-separated and have the format '^%s{DIR}' % path
excludedir = ['^%s.git' % path, '^%sconfigs' % path]
for root, dirs, files in os.walk(path):
    directory_level = root.replace(path, "")
    directory_level = directory_level.count(os.sep)
    indent = " " * 4
    prefix = ""
    indent = "+-- "
    testme = '(?:% s)' % '|'.join(excludedir)
    if (re.search(testme,root)):
      next
    else:
      if (directory_level > 0):
        prefix="|  "

      if (root != './'): 
        contents+=("{}{}{}  \n".format(prefix*directory_level, indent*(directory_level), os.path.basename(root)))
      for file in files:
        testme = '(?:% s)' % '|'.join(excludefiles)
        if (re.search(testme,file)): next
        else:
          contents+=("{}{}{}  \n".format(prefix*(directory_level+1), indent, file))


with open("README.md", "w") as outfile:
  outfile.write(contents)
