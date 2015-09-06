import pymssql


def findschool(school_id,major_id):
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
        a,b=findschool(row[0],row[5])
        print a+"  "+b[16:-8]
    
    conn.commit()
    conn.close()

def select2():
    server="127.0.0.1"          
    user="sa"
    password="trouble"
    db="school"
    conn=pymssql.connect(server,user,password,db)
    cursor=conn.cursor()    
    cursor.execute("select * from score where school_id='755' and zy1='A5'")   #755
    
    for row in cursor:
        a,b=findschool(row[0],row[5])
        print a+"  score:"+row[2].encode('unicode_escape').decode('string_escape')
    
    conn.commit()
    conn.close()
def select3():
    server="127.0.0.1"          
    user="sa"
    password="trouble"
    db="school"
    conn=pymssql.connect(server,user,password,db)
    cursor=conn.cursor()    
    cursor.execute("select * from score where school_id='367'")   #755
    
    for row in cursor:
        a,b=findschool(row[0],row[5])
        print a+"  score:"+row[2].encode('unicode_escape').decode('string_escape')
    
    conn.commit()
    conn.close()
select3()
