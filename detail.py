from BeautifulSoup import BeautifulSoup
import pymssql

def saveTomssql(a,b,c,d,e,f,g,h,i,j,k,l):
    server="192.168.1.114"          
    user="sa"
    password="trouble"
    db="school"
    conn=pymssql.connect(server,user,password,db)
    cursor=conn.cursor()    
    cursor.execute("INSERT INTO score (school_id,all_score,real_score,nation,sex,zy1,zy2,zy3,zy4,zy5,zy6,istiaoji)\
VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (a,b,c,d,e,f,g,h,i,j,k,l))
    conn.commit()
    conn.close()


schoollist=[]
listfile=open('links.txt')
for line in listfile:
      schoollist.append(line.strip('\n'))
listfile.close()

for school in schoollist:
      filename='score/'+school+".html"
      f=open(filename).read().decode('gb2312')
      soup=BeautifulSoup(f)
      scores=soup.findAll('tr')
      for score in scores[2:-1]:
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
            j=str(unicode(td[8].text).encode('utf-8'))
            k=str(unicode(td[9].text).encode('utf-8'))
            l=str(unicode(td[10].text).encode('utf-8'))

            saveTomssql(a,b,c,d,e,f,g,h,i,j,k,l)
      print school



