import requests
from bs4 import BeautifulSoup
import telepot
import os


#도발선수 토큰
#token="1224672949:AAGd26GAig_ouhtmqYASgZluqoDHyZEy348"
#임도연 개인톡
#mc="1228410238"
#클라이밍 채널
#mc="-1001429706075"


#sclimbing2_bot 위원회 톡
token="5185677324:AAGg_eTPiqJdD9iIiO5KwQwnvKSUVZ1WhL0"

#위원회 톡
mc="-1001592845381"

bot=telepot.Bot(token)


#경기력4향상위원회
url5 = "https://kaf.or.kr/bbs/board.php?bo_table=committee_14"

#심판위원회
url6 = "https://kaf.or.kr/bbs/board.php?bo_table=committee_16"

#스포츠클라이밍위원회
url7 = "https://kaf.or.kr/bbs/board.php?bo_table=committee_07"


resp5 = requests.get(url5)
resp6 = requests.get(url6)
resp7 = requests.get(url7)

# 전송된 HTML 문서 얻기
html5 = resp5.text
html6 = resp6.text
html7 = resp7.text
#print(html5)

# HTML 문서를 DOM으로 변환
soup5 = BeautifulSoup(html5,"lxml")
soup6 = BeautifulSoup(html6,"lxml")
soup7 = BeautifulSoup(html7,"lxml")

# 목표 HTML 요소 선택
#print(soup5)
#elem1 = soup1.find("td",{"class": "sbj"})
elem5 = soup5.find("a",{"class": "na-subject"})
elem6 = soup6.find("a",{"class": "na-subject"})
elem7 = soup7.find("a",{"class": "na-subject"})

#print(elem5)

#text11 = elem11.get('href')
#text21 = elem21.get('href')
#text31 = elem31.get('href')


#경기력향상위원회
text5 = elem5.get_text()
text5 = text5.replace('\n','')
text5 = text5.replace(' ','')
text5 = text5.replace('\t','')
text5 = text5.replace('\r','')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(BASE_DIR, 'compare5.txt'), 'r')
line5 = f.readline()
print(line5)
f.close()

if line5 == text5:
    print("None")
else:
    # send message
    bot.sendMessage(mc,'[경기력향상위원회]'+text5+'https://kaf.or.kr/bbs/board.php?bo_table=committee_14')
    #bot.sendMessage(mc,'http://old.kaf.or.kr/kafseoul/forum.php?mid=35')
    #bot.sendMessage(mc,'https://kaf.or.kr/bbs/board.php?bo_table=committee_14')

    fw = open(os.path.join(BASE_DIR, 'compare5.txt'), 'w')
    fw.write(text5)    
    
#심판위원회
text6 = elem6.get_text()
text6 = text6.replace('\n','')
text6 = text6.replace(' ','')
text6 = text6.replace('\t','')
text6 = text6.replace('\r','')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(BASE_DIR, 'compare6.txt'), 'r')
line6 = f.readline()
print(line6)
f.close()

if line6 == text6:
    print("None")
else:
    # send message
    bot.sendMessage(mc,'[심판위원회]'+text6+'https://kaf.or.kr/bbs/board.php?bo_table=committee_16')
    #bot.sendMessage(mc,'http://old.kaf.or.kr/kafseoul/forum.php?mid=35')
    #bot.sendMessage(mc,'https://kaf.or.kr/bbs/board.php?bo_table=committee_16')

    fw = open(os.path.join(BASE_DIR, 'compare6.txt'), 'w')
    fw.write(text6)        
    
#스포츠클라이밍위원회
text7 = elem7.get_text()
text7 = text7.replace('\n','')
text7 = text7.replace(' ','')
text7 = text7.replace('\t','')
text7 = text7.replace('\r','')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(BASE_DIR, 'compare7.txt'), 'r')
line7 = f.readline()
print(line7)
f.close()

if line7 == text7:
    print("None")
else:
    # send message
    bot.sendMessage(mc,'[스포츠클라이밍위원회]'+text7+'https://kaf.or.kr/bbs/board.php?bo_table=committee_07')
    #bot.sendMessage(mc,'http://old.kaf.or.kr/kafseoul/forum.php?mid=35')
    #bot.sendMessage(mc,'https://kaf.or.kr/bbs/board.php?bo_table=committee_07')

    fw = open(os.path.join(BASE_DIR, 'compare7.txt'), 'w')
    fw.write(text7)            