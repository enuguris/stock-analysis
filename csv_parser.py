#!/usr/bin/python

import csv
import db
import os
import sys
import re
from datetime import date
from decimal import *

todays_date = date.strftime(date.today(), "%d%m%Y")

report=sys.argv[1]

report_date = str(re.findall('\d+', report)[0])

trade_date = report_date[-4:]+report_date[2:4]+report_date[:2]


if not os.path.isfile('deliveryReport_'+report_date+'.csv'):
  print('deliveryReport_'+report_date+'.csv'+' does not exist. Exiting')
  sys.exit()


# Insert column headers in delivery.csv
f = open('delivery.csv', 'w')
#f.write("trade_date,scrip_id,total_traded_volume,delivery_volume,delivery_percentage\n")
f.close()

f = open('deliveryReport_'+report_date+'.csv', 'rb')
reader = csv.reader(f)


#skip the first three lines
for skip in range(4):
  next(reader)

for line in reader:
   if line[3]=="EQ":
     scrip_id = db.get_nseid(line[2])
     total_traded_volume = int(line[4])
     delivery_volume = int(line[5])
     delivery_percentage = line[6]
     if scrip_id is not None:
       with open ('delivery.csv', 'a') as outfile:
         writer = csv.writer(outfile, delimiter=',')
         writer.writerow([trade_date,scrip_id,total_traded_volume,delivery_volume,delivery_percentage])
     else:
       log = open('parser_'+todays_date+'.log', 'a')
       log.write(line[2]+" - nseid not found for this symbol.\n")
       log.close()

f.close()

#Import delivery.csv into delivery table
db.load_csv_into_mysql('delivery.csv')

