#!/usr/local/bin/python
import os
import re

# title: Generate a README file for this repo
# description: Looks through all the files and writes a markdown file to README.md
# description: has a list of exclude file patterns (e.g. *.swp) and directories (e.g. .git, configs)

path = "./"
filelist = []
contents = ""
excludefiles = ['.*\.swp', 'CONTRIBUTING.md', 'README.md']
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
        print("{}{}{}/".format(prefix*directory_level, indent*(directory_level), os.path.basename(root)))
#      contents+=print("{}{}{}/".format(prefix*directory_level, indent*(directory_level), os.path.basename(root)))
#     filelist.append(os.path.join(root,file))
      for file in files:
        testme = '(?:% s)' % '|'.join(excludefiles)
        if (re.search(testme,file)): next
#        else: filelist.append(os.path.join(root,file))
        else: print("{}{}{}".format(prefix*(directory_level+1), indent, file))

exit
ToC=["# title: README", "# description: Here are the files in the repo, with a title and description.","# description: generated from generate_readme.py",""]


tmatch='^#*\s*title:'
dmatch='^#*\s*description:'

# print(filelist)
for name in filelist:
  # print(name)
  t=0
  d=0
  # open file, read the top parts, get the title: and description: 
  # then generate markup for it
  with open(name, "rt") as myfile:
    for myline in myfile: 
      if (t!=0):
        if (d==1):
          # we are either in the description, or out of it entirely
          if (re.search(dmatch,myline)):
            ToC.append("    * " + re.sub(dmatch, "", myline).strip()) 
          else: # we WERE in the description and now we're not
            ToC.append("")
            break
        else: # we haven't seen a description yet, but we have seen the title
            if (re.search(dmatch,myline)):
              d=1
              ToC.append("    * " + re.sub(dmatch, "", myline).strip()) 
      if (re.search(tmatch,myline)):
        t=1
        ToC.append("* " + name[2:].strip() + " - " + re.sub(tmatch, "", myline.strip()))

with open("README.md", "w") as outfile:
  for i in ToC:
    outfile.write(i + "\n")
