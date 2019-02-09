import requests
from bs4 import BeautifulSoup
import re
count=0
url=input()
search=input()
r=requests.get(url)
bs=BeautifulSoup(r.text,'html.parser')
b=bs.get_text()
l=b.lower()
s=re.findall(search,l)
print(len(s))
