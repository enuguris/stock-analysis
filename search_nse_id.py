#!/usr/bin/python 

from lxml import html
import requests,sys,re

#arg=sys.argv[1]

def search_id(arg):
  try:
    page=requests.get(arg)
    tree=html.fromstring(page.content)
    company_title=tree.xpath('//div[@class="b_42 PT5 PR"]/h1/text()')
    nse_scrip_id=tree.xpath('//div[@class="FL gry10"]/text()')
    name=re.sub('NSE:','', nse_scrip_id[1])
    if type(name)==str:
      return name.strip()
  except (IndexError,NameError):
    return None 


#print search_id(arg)

