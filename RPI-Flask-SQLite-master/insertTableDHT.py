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

con = lite.connect('sensorsData.db',check_same_thread=False)

with con:
    
    cur = con.cursor() 
    cur.execute("INSERT INTO DHT_data VALUES(datetime('now'), 10, 26)")
    cur.execute("INSERT INTO DHT_data VALUES(datetime('now'), 35, 45)")
    cur.execute("INSERT INTO DHT_data VALUES(datetime('now'), 50, 70)")


