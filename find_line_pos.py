#!/usr/bin/python

import re
import sys
import string
import linecache
import find_lastline

def get_lastline_pos():
  lastline = find_lastline.lastline()
  m = re.search("http://.*/(.*)$", lastline)
  file_name = m.group(1)[0]+".urls"
  
  with open(file_name) as f:
    txt = f.readlines()
  
  for pos, line in enumerate(txt):
    if lastline in line:
      lastline_pos = pos+1
      return lastline_pos 
  

get_lastline_pos()
