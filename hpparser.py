from bs4 import BeautifulSoup

def findCode(text: str, toMatch: str) -> str | None:
    soup = BeautifulSoup(text, features='lxml')
    asess = soup.find_all('a')
    for a in asess:
        if toMatch in a.string:
            return a.attrs['href']
    return None

def findImg(text: str) -> str | None:
    soup = BeautifulSoup(text, features='lxml')
    asess = soup.find_all('img')
    for a in asess:
          return 'http://www.bancocn.com/' + a.attrs['src']
    return None