import requests
from bs4 import BeautifulSoup
# 1. 요청 보낼 url
url = 'http://m.exchange.daum.net/mobile/exchange/exchangeMain.daum'
# 2. 응답 받은 본문 내용을 response에 저장
response = requests.get(url).text
# 3. string을 조작하기 편한 형태(html문서)로 변환 
soup = BeautifulSoup(response, 'html.parser')

result = soup.select(".link")

for country in result:
    print(country.select_one('.name').text)
    print(country.select_one('.idx').text)

