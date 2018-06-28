#!/usr/bin/env python
## Run on all .txt files the doctest, convert to doxygen and run doxygen
import doctest
import os

for fileName in os.listdir("."):
  if fileName.endswith(".doctest"):
    result = doctest.testfile(fileName)
    print "%-30s %-30s"%(fileName,result,)
    txtFile = open(fileName,'r')
    doxyFile= open(fileName[:-7]+"doxy",'w')
    for line in txtFile:
      if "#doctest: +SKIP" in line:  line=line.replace('#doctest: +SKIP','')
      elif "doctest"       in line:  continue
      doxyFile.write(line)
    txtFile.close()
    doxyFile.close()

if os.path.exists('doxygenOutput.txt'):
  os.unlink("doxygenOutput.txt")
os.system("doxygen")
os.system("rm *.doxy")
if os.path.exists('doctest.png'):
  os.unlink('doctest.png')

#commit to github
message = raw_input("Enter github message? [empty: no commit] ")
if len(message)>3:
  with open(".gitignore", "rt") as fin:
    with open("out.txt", "wt") as fout:
      for line in fin:
        fout.write(line.replace('A', 'Orange'))
  os.system("git add -A")
  os.system('git commit -m "'+message+'"')
  os.system('git push -u origin master')
