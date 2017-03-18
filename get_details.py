#!/usr/bin/python

from lxml import html
import requests,sys
import re
import datetime


def format_tday(arg):
  month_dic = { 'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun': '06', 'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12' }
  
  for x in arg:
    m = re.search(r'(.*) (.*),.*', x)
    if m:
      try:
        month = month_dic[m.group(1)]
        day = m.group(2)
        now = datetime.datetime.now()
        year = str(now.year)
        if day == str(now.day-1):
          return year+month+day
      except KeyError:
        return '000000'
      

def get_todays_price_details(arg):
  page=requests.get(arg)
  tree=html.fromstring(page.content)
  trad_day=tree.xpath('//div[@id="nse_upd_time" and @class="CL"]/text()')
  cprice=tree.xpath('//span[@id="Nse_Prc_tick" and @class="PA2"]/strong/text()')
  oprice=tree.xpath('//div[@id="n_open" and @class="gD_12 PB3"]/strong/text()')
  low=tree.xpath('//span[@id="n_low_sh" and @class="PR5"]/text()')
  high=tree.xpath('//span[@id="n_high_sh" and @class="PL5"]/text()')
  vol=tree.xpath('//span[@id="nse_volume" and @class="gD_12"]/strong/text()')
  todays_prices = [ format_tday(trad_day), ','.join(oprice), ','.join(high), ','.join(low), ','.join(cprice), ','.join(vol).replace(',','') ]
  if todays_prices[0] != '000000':
    return todays_prices

if __name__ == "__main__":
  print sys.argv[1]
  print get_todays_price_details(sys.argv[1])

