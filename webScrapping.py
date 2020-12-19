import requests
from bs4 import BeautifulSoup


li=[]
data=requests.get("https://www.imdb.com/find?s=ep&q=Triller&ref_=nv_sr_sm")
soap=BeautifulSoup(data.content, 'html.parser')
#print(soap.prettify())
moviesTable=soap.find('table', {'class':'findList'})
print(moviesTable)
rows=moviesTable.findAll('tr')
for row in rows:
    rowData=row.findAll('td')
    print(rowData[1].a.text)
    subUrl=rowData[1].a['href']
    subData=requests.get("https://www.imdb.com"+subUrl)
    print(subData)
    childSoap= BeautifulSoup(subData.content, "html.parser")
    if childSoap.find('div',{'class':'see-more inline canwrap'}):
        genre=childSoap.find('div',{'class':'see-more inline canwrap'})
        if genre.a.text=="Dpcumentary":
            #print(genre.a.text)
           # print(rowData[1].a.text)
            li.append(rowData[1].a.text)
print(li)