from bs4 import BeautifulSoup
import pymysql

def saveTomssql(a,b,c,d,e,f,g,h,i,j):
    server="localhost"          
    user="root"
    password="trouble"
    db="zhiyuan"
    conn=pymysql.connect(host=server,user=user,passwd=password,db=db,charset='utf8')
    cursor=conn.cursor()    
    cursor.execute("INSERT INTO 14_3_1major (school_id,major_id,major_cn,plannum,minscore,realnum,money,location,elseinfo,school_cn)\
VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (a,b,c,d,e,f,g,h,i,j))
    conn.commit()
    conn.close()

loca='2014/zhuanke/wenke/'
schoollist=[]
listfile=open(loca+'links.txt')
for line in listfile:
      schoollist.append(line.strip('\n'))
listfile.close()

for school in schoollist:
      filename=loca+'school/'+school+".html"
      f=open(filename).read()
      soup=BeautifulSoup(f,"html.parser")
      j=soup.find('td',{'class':'report1_1_1'}).text
      scores=soup.findAll('tr')
      for score in scores[3:-2]:
            
            td=score.findAll('td')
            a=school
            b=td[0].text
            c=td[1].text
            d=td[2].text
            e=td[3].text
            f=td[4].text
            g=td[5].text
            h=td[6].text
            #i=str(unicode(td[7].text).encode('utf-8'))
            i=td[7].text
            saveTomssql(a,b,c,d,e,f,g,h,i,j)
            
      print(school)
