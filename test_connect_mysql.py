import MySQLdb

host = "192.168.150.143"
db = MySQLdb.connect(host=host,user='',passwd='123455',db='123')

conn = db.cursor()

conn.execute("select 123");


import pdb;pdb.set_trace()
