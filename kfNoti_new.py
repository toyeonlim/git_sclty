import requests
from bs4 import BeautifulSoup
import telepot
import os


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

elem11 = soup1.find("a",{"class": "b"})
elem21 = soup1.find("a",{"class": "b"})
elem31 = soup1.find("a",{"class": "b"})

text11 = elem11.get('href')
text21 = elem21.get('href')
text31 = elem31.get('href')

# 목표 텍스트 추출
text1 = elem1.get_text()
text1 = text1.replace('\n','')
text1 = text1.replace(' ','')
text1 = text1.replace('\t','')
text1 = text1.replace('\r','')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(BASE_DIR, 'compare1.txt'), 'r')
line1 = f.readline()
print(line1)
f.close()

if line1 == text1:
    print("None")
else:
    # send message
    bot.sendMessage(mc,text1)
    bot.sendMessage(mc,'http://new.kaf.or.kr/' + text11)

    fw = open(os.path.join(BASE_DIR, 'compare1.txt'), 'w')
    fw.write(text1)

#print(elem2)
# 목표 텍스트 추출
text2 = elem2.get_text()
text2 = text2.replace('\n','')
text2 = text2.replace(' ','')
text2 = text2.replace('\t','')
text2 = text2.replace('\r','')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(BASE_DIR, 'compare2.txt'), 'r')
line2 = f.readline()
print(line2)
f.close()

if line2 == text2:
    print("None")
else:
    # send message
    bot.sendMessage(mc,text2)
    bot.sendMessage(mc,'http://new.kaf.or.kr/' + text21)

    fw = open(os.path.join(BASE_DIR, 'compare2.txt'), 'w')
    fw.write(text2)
    print(text2)

# print(elem3)
# 목표 텍스트 추출
text3 = elem3.get_text()
text3 = text3.replace('\n','')
text3 = text3.replace(' ','')
text3 = text3.replace('\t','')
text3 = text3.replace('\r','')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(BASE_DIR, 'compare3.txt'), 'r')
line3 = f.readline()
print(line3)
f.close()

if line3 == text3:
    print("None")
else:
    # send message
    bot.sendMessage(mc,text3)
    bot.sendMessage(mc,'http://new.kaf.or.kr/' + text31)

    fw = open(os.path.join(BASE_DIR, 'compare3.txt'), 'w')
    fw.write(text3)