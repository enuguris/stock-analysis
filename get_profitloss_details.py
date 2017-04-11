#!/usr/bin/python 

from lxml import html
import requests,sys,re
import build_profit_loss_url
import return_xpath

def get_pat_details(arg):
  page=requests.get(arg)
  tree=html.fromstring(page.content)
  path=return_xpath.get_xpath(arg)
  m = re.search('^(.*)\/td\[1\]$', path)
  if m:
    pat=tree.xpath(m.group(1)+'/*/text()')
  else:
    print "not found."
  results=[]
  for val in pat[1:]:
    results.append(str.replace(str(val),',',''))
  return results

if __name__ == "__main__":
  print  get_pat_details(sys.argv[1])
