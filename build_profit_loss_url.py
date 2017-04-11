#!/usr/bin/python

import re
import sys

def financials_pageurl(arg):
   m=re.search("(http://www.moneycontrol.com/)india/stockpricequote/.*/(.*)/(.*)$", arg)
   if m:
     part_url=m.group(1)
     comp_title=m.group(2)
     comp_id=m.group(3)
     pl_url=part_url+"financials/"+comp_title+"/profit-lossVI/"+comp_id
     return pl_url

if __name__ == "__main__":
  print financials_pageurl(sys.argv[1])
	 
