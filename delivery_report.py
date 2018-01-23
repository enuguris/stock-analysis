#!/usr/bin/python

import sys
import requests
from datetime import date

try:
  todays_date=sys.argv[1]
except IndexError:
  todays_date = date.strftime(date.today(), "%d%m%Y")
#todays_date = sys.argv[1]

url = "https://www.nseindia.com/archives/equities/mto/MTO_"+todays_date+".DAT"
#url = "https://www.nseindia.com/archives/equities/mto/MTO_12012018.DAT"

r = requests.get(url)
if r.status_code == 200:
  open('deliveryReport_'+todays_date+'.csv', 'wb').write(r.content)
else:
  print("No delivery report available for the date "+todays_date)
  print("Pass the report date as an arugment in the format ddmmyyyy. Ex: "+sys.argv[0]+" "+todays_date)
