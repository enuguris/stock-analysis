#!/usr/bin/python

import re

def lastline():
  f_su = open('scrip_urls.txt', 'r')
  for line in f_su:
    m = re.search('http://www.moneycontrol.com/india/stockpricequote/.*/.*/.*$', line)
    if m:
      last_line=m.group()
  f_su.close()
  return last_line

#print lastline()
