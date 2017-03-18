#!/usr/bin/python

import mysql.connector
from mysql.connector.constants import ClientFlag 
flags = [ClientFlag.LOCAL_FILES] 


def load_csv_into_table():
  config = {
    'user': 'root',
    'password': 'naafavorite',
    'host': '127.0.0.1',
    'database': 'nse' }

 
  cnx = mysql.connector.connect(**config)
  cursor = cnx.cursor()
  
  query = "LOAD DATA LOCAL INFILE 'results.csv' INTO TABLE nse_data FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' (scrip_id,trad_day,oprice,high,low,cprice,vol);"
  cursor.execute('LOAD DATA INFILE "/root/scripts/python/moneycontrol/results.csv" INTO TABLE nse_data_test FIELDS TERMINATED BY "," LINES TERMINATED BY "\n" (scrip_id,trad_day,oprice,high,low,cprice,vol);')
#  cursor.execute(query)
 
  cnx.commit() 
  cnx.close()

if __name__ == "__main__":
  load_csv_into_table()
