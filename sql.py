import pymysql as dbapi
import sys
import csv

dbServer='localhost'
dbPass='supersecretpassword'
dbSchema='dbTest'
dbUser='root'

dbQuery='SELECT * FROM pbTest.Orders;'

db=dbapi.connect(host=dbServer,user=dbUser,passwd=dbPass)
cur=db.cursor()
cur.execute(dbQuery)
rows = cur.fetchall()
fp = open('/tmp/file.csv', 'w')
myFile = csv.writer(fp)
myFile.writerows(rows)
fp.close()