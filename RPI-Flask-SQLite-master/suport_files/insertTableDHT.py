#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  insertTableDHT.py
#  
# Developed by Marcelo Rovai, MJRoBot.org @ 9Jan18
#  
# Insert dada on table "DHT_data" 

import sqlite3 as lite
import sys

con = lite.connect('sensorsData.db')

with con:
    
    cur = con.cursor() 
    cur.execute("INSERT INTO DHT_data VALUES(datetime('now'), 2, 3)")
    cur.execute("INSERT INTO DHT_data VALUES(datetime('now'), 4, 5)")
    cur.execute("INSERT INTO DHT_data VALUES(datetime('now'), 6, 7)")


