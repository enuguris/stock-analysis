#!/bin/bash

statement="select b.scrip_name as SYMBOL,a.trade_date as Date,a.traded_vol as Total_Traded_Volume,a.delivery_vol as Delivery_Volume,a.delivery_percentage as Delivery_Percentage from delivery as a join scrip as b on a.scrip_id = b.scrip_id where b.scrip_name='$1' order by a.trade_date"
echo $statement
mysql -u senuguri -pnaafavorite -D nse -e "${statement};"
statement="select b.scrip_name as SYMBOL,a.trade_date as Date,a.traded_vol as Total_Traded_Volume,a.delivery_vol as Delivery_Volume,a.delivery_percentage as Delivery_Percentage, c.cprice as Closing_Price from delivery as a join scrip as b on a.scrip_id = b.scrip_id join nse_data as c on a.scrip_id=c.scrip_id where a.trade_date=c.trad_day and b.scrip_name='$1' order by a.trade_date"
echo $statement
mysql -u senuguri -pnaafavorite -D nse -e "${statement};"
