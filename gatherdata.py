from BeautifulSoup import BeautifulSoup
import urllib2



def getdata(url):
    req=urllib2.Request(url)
    html=urllib2.urlopen(url)
    return html.read()

def addLink(link):
    f=open(getlocation("links.txt"),'a')
    f.write(link+'\n')
    f.close()

def geturl(stringg):
    return "http://www.nm.zsks.cn/zy_7_1_2014/7_A_"+stringg

def getlocation(stringg):
    return '2014/zhuanke/wenke/'+stringg
mainurl=geturl('11.html')
soup=BeautifulSoup(getdata(mainurl))




    
schoollist=[]
schools=soup.findAll('tr')
for school in schools[3:-1]:
      tds=school.findAll('td')
      schoollist.append(tds[0].text)


print len(schoollist)

knownLinkList=[]
linkfile=open(getlocation("links.txt"))
for line in linkfile:
    knownLinkList.append(line.strip('\n'))
linkfile.close()
i=0
for item in schoollist:
    if str(item) not in knownLinkList: 
        url=geturl(item+"_11.html")
        #url=geturl(item+"_11_detail.html")
        i=i+1
        data=getdata(url)
        filename=item+".html"
        output=open(getlocation("school/")+str(filename),'w')
        output.write(data)
        output.close()
        addLink(str(item))
        print float(i)/float(len(schoollist))*100
    else:
        print "pass"
        i=i+1
    




