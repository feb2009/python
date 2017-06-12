# -*- coding:UTF-8 -*-
import mysql

import mysql.connector

config = {
  'user': 'feb',
  'password': 'feb123',
  'host': '127.0.0.1',
  'database': 'employees',
  'raise_on_warnings': True,
}
cnx = mysql.connector.connect(config)
cnx.close()


import cx_Oracle

