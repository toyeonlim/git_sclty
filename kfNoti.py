import requests
from bs4 import BeautifulSoup
import telepot
token="1140975028:AAHF5R5pN632-d2iM4ZYH_1LUQmmhGsGqyQ"
mc="1228410238"
bot=telepot.Bot(token)

#공지사항
url1 = "http://new.kaf.or.kr/?c=5/33"
#시도연맹
url2 = "http://new.kaf.or.kr/?c=5/34"

# 웹 서버에 요청(requests) 보내고 응답(resp) 받기
resp = requests.get(url1)
#print(resp)
#print(resp) -> 200 뜨면 제대로 응답 받은 것

# 전송된 HTML 문서 얻기
html = resp.text
#print(html)

# HTML 문서를 DOM으로 변환
soup = BeautifulSoup(html,"lxml")

# 목표 HTML 요소 선택
#print(soup)
elem = soup.find("td",{"class": "sbj"})
#div 안에 있는 클래스 view_se에 내용이 있어서 find명령을 씀

#print(elem)
# 목표 텍스트 추출
text = elem.get_text()
bot.sendMessage(mc,text)

resp = requests.get(url2)
#print(resp)
#print(resp) -> 200 뜨면 제대로 응답 받은 것

# 전송된 HTML 문서 얻기
html = resp.text
#print(html)

# HTML 문서를 DOM으로 변환
soup = BeautifulSoup(html,"lxml")

# 목표 HTML 요소 선택
#print(soup)
elem = soup.find("td",{"class": "sbj"})
#div 안에 있는 클래스 view_se에 내용이 있어서 find명령을 씀

#print(elem)
# 목표 텍스트 추출
text = elem.get_text()
bot.sendMessage(mc,text)


