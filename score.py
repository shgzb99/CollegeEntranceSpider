from bs4 import BeautifulSoup
import pymysql

def saveTomssql(a,b,c,d,e,f,g,h,i,j,k,l):
    server="localhost"          
    user="root"
    password="trouble"
    db="zhiyuan"
    conn=pymysql.connect(host=server,user=user,passwd=password,db=db,charset='utf8')
    cursor=conn.cursor()    
    cursor.execute("INSERT INTO 14_3_2score (school_id,all_score,real_score,nation,sex,zy1,zy2,zy3,zy4,zy5,zy6,istiaoji)\
VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (a,b,c,d,e,f,g,h,i,j,k,l))
    conn.commit()
    conn.close()

loca='2014/zhuanke/like/'
schoollist=[]
listfile=open(loca+'links.txt')
for line in listfile:
      schoollist.append(line.strip('\n'))
listfile.close()

for school in schoollist:
      filename=loca+'score/'+school+".html"
      f=open(filename).read()
      soup=BeautifulSoup(f,"html.parser")
      scores=soup.findAll('tr')
      for score in scores[2:-1]:
            td=score.findAll('td')
            a=school
            b=td[0].text
            c=td[1].text
            d=td[2].text
            e=td[3].text
            f=td[4].text
            g=td[5].text
            h=td[6].text
            i=td[7].text
            j=td[8].text
            k=td[9].text
            l=td[10].text

            saveTomssql(a,b,c,d,e,f,g,h,i,j,k,l)
      print(school)



