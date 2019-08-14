#!/usr/bin/python

import mysql.connector
from mysql.connector import Error

config = {'user': 'root', 'password': '******', 'host': '127.0.0.1', 'database': 'nse'}


def get_nseid(symbol):
  query = "select scrip_id from scrip where scrip_name='"+symbol+"';"
  
  try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(query)
    if not cursor.rowcount:
      return None
    else:
       for row in cursor.fetchall():
         return row[0]

  except Error as e:
    print(e)

  finally:
    cursor.close()
    conn.close()

def insert_into_delivery(trade_date,scrip_id,traded_vol,delivery_vol,delivery_percentage):
  query = "INSERT INTO delivery VALUES (%s %d,%d,%d,%d)" % (trade_date,scrip_id,traded_vol,delivery_vol,delivery_percentage)
  
  try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
  
  except Error as e:
    print(e)

  finally:
    cursor.close()
    conn.close()


def load_csv_into_mysql(arg):
  query = "LOAD DATA LOCAL INFILE '" + arg + "' INTO TABLE delivery FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' (trade_date,scrip_id,traded_vol,delivery_vol,delivery_percentage);"
  
  try:
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute('LOAD DATA INFILE "/root/scripts/python/moneycontrol/delivery.csv" INTO TABLE delivery FIELDS TERMINATED BY "," LINES TERMINATED BY "\n" (trade_date,scrip_id,traded_vol,delivery_vol,delivery_percentage);')
    conn.commit()

  except Error as e:
    print(e)
 
  finally:
    cursor.close()
    conn.close()
