# -*- coding: cp936 -*-
import pymssql


def findschoolcn(school_id,major_id):
    server="127.0.0.1"          
    user="sa"
    password="trouble"
    db="school"
    conn=pymssql.connect(server,user,password,db)
    cursor=conn.cursor()    
    cursor.execute("select major_cn,school_cn from major where school_id='%s' and major_id='%s'"%(school_id,major_id))
    data=cursor.fetchall()
    conn.commit()
    conn.close()
    return data[0][0].encode('unicode_escape').decode('string_escape'),data[0][1].encode('unicode_escape').decode('string_escape')

def select():
    server="127.0.0.1"          
    user="sa"
    password="trouble"
    db="school"
    conn=pymssql.connect(server,user,password,db)
    cursor=conn.cursor()    
    cursor.execute("select * from score where real_score=309")   #755
    
    for row in cursor:
        a,b=findschoolcn(row[0],row[5])
        print a+"  "+b[16:-8]
    
    conn.commit()
    conn.close()

def selectSchoolByMajor(school_id,major_id,score):
    server="127.0.0.1"          
    user="sa"
    password="trouble"
    db="school"
    conn=pymssql.connect(server,user,password,db)
    cursor=conn.cursor()    
    cursor.execute("select * from score where school_id='%s' and zy1='%s' and all_score<'%s'"%(school_id,major_id,score))   #755
    
    for row in cursor:
        a,b=findschoolcn(row[0],row[5])
        print a+"  score:"+row[2].encode('unicode_escape').decode('string_escape')+"  school: "+b[16:-8]
    
    conn.commit()
    conn.close()
def selectSchoolbyId():
    server="127.0.0.1"          
    user="sa"
    password="trouble"
    db="school"
    conn=pymssql.connect(server,user,password,db)
    cursor=conn.cursor()    
    cursor.execute("select * from score where school_id='367'")   #755
    
    for row in cursor:
        a,b=findschoolcn(row[0],row[5])
        print a+row[5]+"  score:"+row[2].encode('unicode_escape').decode('string_escape')
    
    conn.commit()
    conn.close()

def selectMajor():
    server="127.0.0.1"          
    user="sa"
    password="trouble"
    db="school"
    conn=pymssql.connect(server,user,password,db)
    cursor=conn.cursor()    
    cursor.execute("select * from major where major_cn like '%s'"%(u'%学前教育%'.encode('utf8')))   #755
    
    for row in cursor:
        selectSchoolByMajor(row[0],row[1],'450')    
    conn.commit()
    conn.close()

selectMajor()
