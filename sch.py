from BeautifulSoup import BeautifulSoup
import pymssql

def saveTomssql(a,b,c,d,e,f,g,h,i,j):
    server="127.0.0.1"          
    user="sa"
    password="trouble"
    db="school"
    conn=pymssql.connect(server,user,password,db)
    cursor=conn.cursor()    
    cursor.execute("INSERT INTO major (school_id,major_id,major_cn,plannum,minscore,realnum,money,location,elseinfo,school_cn)\
VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (a,b,c,d,e,f,g,h,i,j))
    conn.commit()
    conn.close()


schoollist=[]
listfile=open('links.txt')
for line in listfile:
      schoollist.append(line.strip('\n'))
listfile.close()

for school in schoollist:
      filename='school/'+school+".html"
      f=open(filename).read().decode('gb2312','ignore')
      soup=BeautifulSoup(f)
      j=str(unicode(soup.find('td',{'class':'report1_1_1'}).text).encode('utf-8'))
      scores=soup.findAll('tr')
      for score in scores[3:-2]:
            
            td=score.findAll('td')
            a=str(school)
            b=str(unicode(td[0].text).encode('utf-8'))
            c=str(unicode(td[1].text).encode('utf-8'))
            d=str(unicode(td[2].text).encode('utf-8'))
            e=str(unicode(td[3].text).encode('utf-8'))
            f=str(unicode(td[4].text).encode('utf-8'))
            g=str(unicode(td[5].text).encode('utf-8'))
            h=str(unicode(td[6].text).encode('utf-8'))
            i=str(unicode(td[7].text).encode('utf-8'))

            saveTomssql(a,b,c,d,e,f,g,h,i,j)
      print school
