#!/usr/bin/python

import re
import sys
import string
import search_nse_id
import check_redirect
import time
import find_lastline
import find_line_pos

def get_file_name():
  m = re.search("http://.*/(.*)$", last_line)
  return m.group(1)[0]+'.urls'
  
def get_startfile_first_char_pos():
  m = re.search("http://.*/(.*)$", last_line)
  char = m.group(1)[0]
  for pos, letter in enumerate(string.ascii_uppercase):
    if char == letter:
      return pos
	  
def get_startfile_first_char():
  m = re.search("http://.*/(.*)$", last_line)
  return m.group(1)[0]
  
 
last_line = find_lastline.lastline()
last_line_pos = find_line_pos.get_lastline_pos()
ignore_link = "http://www.moneycontrol.com/india/stockpricequote/\n"
file_name = get_file_name()
alphabet_pos = get_startfile_first_char_pos()
char = get_startfile_first_char()

for alphabet in string.ascii_uppercase[alphabet_pos:]:
  f1=open(alphabet+'.urls', 'r')
  f2=open('debug.log', 'a')
  f3=open('scrip_urls.txt', 'a')
  
  if char == alphabet:
    for line in f1:
      if line == last_line+'\n':
        break
  
  for link in f1:
    if link != ignore_link:
      if not check_redirect.check_title(link):
        f2.write('Looking for NSE id in page ' + link + '\n')
        f2.flush()
        name = search_nse_id.search_id(link)
        if name != None and len(name) > 0:
          print name + " --> " + link
          f3.write(name + ' --> ' + link + '\n')
          f3.flush()
          time.sleep(1)
  f1.close()
  f2.close()
  f3.close()

