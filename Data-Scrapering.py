from bs4 import BeautifulSoup
import requests

url ='https://en.wikipedia.org/wiki/Demographics_of_India'

p=requests.get(url)

s=BeautifulSoup(p.text,'html')
# a=s.find_all('tr')

# print(s.find('tr'))
# print(s.find_all('table')[0])
# print(s.find('table',class_ ='wikitable sortable'))
table=s.find_all('table')[8]
title = table.find_all('th')
wot=[a.text.strip() for a in title]

# for b in wot:
#     print(b)
# print(wot)
import pandas as pd
heading=pd.DataFrame(columns=wot)
# print(heading)
col=table.find_all('tr')
for row in col[1:]:
    row_data=row.find_all('td')
    rd=[data.text.strip() for data in row_data]
    # print(rd)
    le=len(heading)
    heading.loc[le]=rd
print(heading)
heading.to_csv(r'C:\Users\JATIN MEHRA\Desktop\Jatin\Pandas\companies1.csv',index=False)

