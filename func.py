import requests
from bs4 import BeautifulSoup as bs

def GetState():
    cookie = {
    "my":'YysBgNUA',
    "yandexuid":'1047500711468836365',
    "yandex_gid":'213'
    }
    
    html=requests.get('http://m.yandex.ru', cookies=cookie).text
    print(len(html))
    soup = bs(html, 'html.parser')
    print(soup.find_all("td", class_="b-region")[0].text)
    a=soup.find_all("strong", class_="num")[0].text
    try:
        b=soup.find_all('img', class_='arr' )[0].get('src')
        if b[-8:]=='wn':
            b=False
        else:
            b=True
        print(b)
    except BaseException:
        b=None
    return [int(a),'Количество баллов равно '+a+' из 10',b]


print(GetState())
