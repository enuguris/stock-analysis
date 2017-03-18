#!/usr/bin/python

from lxml import html
import urllib2,sys

#arg=sys.argv[1]

redirect_title="Stock/Share Market Investing - Live BSE/NSE, India Stock Market Recommendations and Tips, Live Stock Markets, Sensex/Nifty, Commodity Market, Investment Portfolio, Financial News, Mutual Funds"

def check_title(arg):
  request=urllib2.urlopen(arg)
  page=request.read()
  tree=html.fromstring(page)
  Title=tree.xpath("//title/text()")
  title_found=Title[0].strip()
  if redirect_title == title_found:
    return True

#print check_title(arg)

