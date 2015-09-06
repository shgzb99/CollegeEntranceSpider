import pymysql

conn=pymysql.connect(host='localhost',port=3306,user='root',passwd='trouble',db='test',charset='utf8')
cur=conn.cursor()
cur.execute("select * from ta")
for r in cur:
    print(r)

cur.close()

conn.close()

