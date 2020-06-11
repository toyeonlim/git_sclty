import requests
from bs4 import BeautifulSoup
import telepot
import sqlite3

#도발선수 토큰
token="1224672949:AAGd26GAig_ouhtmqYASgZluqoDHyZEy348"
mc="1228410238"
bot=telepot.Bot(token)

#공지사항
url1 = "http://new.kaf.or.kr/?c=5/33"
#시도연맹
url2 = "http://new.kaf.or.kr/?c=5/34"
#경기결과
url3 = "http://new.kaf.or.kr/?c=5/116"

resp1 = requests.get(url1)
resp2 = requests.get(url2)
resp3 = requests.get(url3)

# 전송된 HTML 문서 얻기
html1 = resp1.text
html2 = resp2.text
html3 = resp3.text
#print(html)

# HTML 문서를 DOM으로 변환
soup1 = BeautifulSoup(html1,"lxml")
soup2 = BeautifulSoup(html2,"lxml")
soup3 = BeautifulSoup(html3,"lxml")

# 목표 HTML 요소 선택
#print(soup)
elem1 = soup1.find("td",{"class": "sbj"})
elem2 = soup2.find("td",{"class": "sbj"})
elem3 = soup3.find("td",{"class": "sbj"})

print(elem1)
# 목표 텍스트 추출
text1 = elem1.get_text()
text1 = text1.replace('\n','')
text1 = text1.replace(' ','')
text1 = text1.replace('\t','')

if 'new' in text1:
    # send message
    bot.sendMessage(mc,text1)
else:
    print("None")

print(elem2)
# 목표 텍스트 추출
text2 = elem2.get_text()
text2 = text2.replace('\n','')
text2 = text2.replace(' ','')
text2 = text2.replace('\t','')

if 'new' in text2:
    # send message
    bot.sendMessage(mc,text2)
else:
    print("None")

print(elem3)
# 목표 텍스트 추출
text3 = elem3.get_text()
text3 = text3.replace('\n','')
text3 = text3.replace(' ','')
text3 = text3.replace('\t','')

if 'new' in text3:
    # send message
    bot.sendMessage(mc,text3)
else:
    print("None")