#!/usr/bin/python

import mysql.connector
import os
import sys
import get_details
import time
import re
import build_profit_loss_url
import get_profitloss_details

#arg=sys.argv[1]

def get_scripid():
  config={
    'user': 'senuguri',
    'password': 'naafavorite',
    'host': '127.0.0.1',
    'database': 'nse'
  }

  cnx=mysql.connector.connect(**config)
  cursor=cnx.cursor()

  query="select a.scrip_id,b.scrip_url from scrip as a join scrip_urls as b on a.scrip_id = b.scrip_id order by a.scrip_id;"
  cursor.execute(query)

  f = open('pat_details.csv','w+')
  for x in cursor.fetchall():
    m = re.search('\((\d+),.*(http://.*)\'\)$',str(x))
    if m:
      scrip_id=m.group(1)
      scrip_url=m.group(2)
    try:
      fin_page_url=build_profit_loss_url.financials_pageurl(scrip_url)
      details=','.join(get_profitloss_details.get_pat_details(fin_page_url))
      f.write(scrip_id+','+details+'\n')
      f.flush()
    except TypeError:
      pass

  cnx.close()

get_scripid()
#os.system("mysql -u senuguri -pnaafavorite -D nse -e \"LOAD DATA LOCAL INFILE 'results.csv' INTO TABLE nse_data FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' (scrip_id,trad_day,oprice,high,low,cprice,vol);\"")
