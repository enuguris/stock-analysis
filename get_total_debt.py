#!/usr/bin/python 

from lxml import html
import requests,sys

def get_total_debt(arg):
  page=requests.get(arg)
  tree=html.fromstring(page.content)
  tdeb=tree.xpath('//div[@class="FR w252"]/div[1]/table/tr[3]/td[1]/text()')
  tdeb_val=tree.xpath('//div[@class="FR w252"]/div[1]/table/tr[3]/td[2]/span/text()')
  tdeb_dict=dict(zip(tdeb,tdeb_val))
  print (tdeb_dict)

if __name__ == "__main__":
  get_total_debt(sys.argv[1])
