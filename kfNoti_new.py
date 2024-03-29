import requests
from bs4 import BeautifulSoup
import telepot
import os


#도발선수 토큰
token="1224672949:AAGd26GAig_ouhtmqYASgZluqoDHyZEy348"
#임도연 개인톡
mc="1228410238"


#클라이밍 채널
#mc="-1001429706075"
bot=telepot.Bot(token)

#공지사항
#url1 = "http://kaf.or.kr/?c=5/33"
url1 = "https://kaf.or.kr/news_01"

#대한산악연맹뉴스
url2 = "https://kaf.or.kr/news_04"

#경기결과
url3 = "https://kaf.or.kr/game_31"

#서울시 산악연맹
url4 = "https://seoul.kaf.or.kr/forum_01"

resp1 = requests.get(url1)
resp2 = requests.get(url2)
resp3 = requests.get(url3)
resp4 = requests.get(url4)

# 전송된 HTML 문서 얻기
html1 = resp1.text
html2 = resp2.text
html3 = resp3.text
html4 = resp4.text
#print(html)

# HTML 문서를 DOM으로 변환
soup1 = BeautifulSoup(html1,"lxml")
soup2 = BeautifulSoup(html2,"lxml")
soup3 = BeautifulSoup(html3,"lxml")
soup4 = BeautifulSoup(html4,"lxml")

# 목표 HTML 요소 선택
#print(soup)
#elem1 = soup1.find("td",{"class": "sbj"})
elem1 = soup1.find("a",{"class": "na-subject"})
elem2 = soup2.find("h5",{"class": "card-title font-weight-bold"})
elem3 = soup3.find("a",{"class": "na-subject"})
elem4 = soup4.find("a",{"class": "na-subject"})

elem11 = soup1.find("a",{"class": "b"})
elem21 = soup1.find("a",{"class": "b"})
elem31 = soup1.find("a",{"class": "b"})

#text11 = elem11.get('href')
#text21 = elem21.get('href')
#text31 = elem31.get('href')

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
    bot.sendMessage(mc,'[공지사항]'+text1)
    #bot.sendMessage(mc,'https://kaf.or.kr/news_01' + '대한산악연맹')
    bot.sendMessage(mc, 'https://kaf.or.kr/news_01')

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
    bot.sendMessage(mc,'[연맹뉴스]'+text2)
    bot.sendMessage(mc,'https://kaf.or.kr/news_04')

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
    bot.sendMessage(mc,'[대회]'+text3)
    bot.sendMessage(mc,'https://kaf.or.kr/game_31')

    fw = open(os.path.join(BASE_DIR, 'compare3.txt'), 'w')
    fw.write(text3)

#서울시 산악연맹
text4 = elem4.get_text()
text4 = text4.replace('\n','')
text4 = text4.replace(' ','')
text4 = text4.replace('\t','')
text4 = text4.replace('\r','')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(BASE_DIR, 'compare4.txt'), 'r')
line4 = f.readline()
print(line4)
f.close()

if line4 == text4:
    print("None")
else:
    # send message
    bot.sendMessage(mc,'[서울시산악연맹]'+text4)
    #bot.sendMessage(mc,'http://old.kaf.or.kr/kafseoul/forum.php?mid=35')
    bot.sendMessage(mc,'https://seoul.kaf.or.kr/forum_01')

    fw = open(os.path.join(BASE_DIR, 'compare4.txt'), 'w')
    fw.write(text4)
