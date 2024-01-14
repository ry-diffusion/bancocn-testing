from string import ascii_lowercase
from random import choice

def randomString(length: int):
   letters = ascii_lowercase
   return ''.join(choice(letters) for i in range(length))
