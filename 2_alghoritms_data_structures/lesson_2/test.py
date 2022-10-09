import requests
from hashlib import md5
from uuid import uuid4
html = requests.get('https://gb.ru/lessons/259309').text
file = open('gb.html', 'wb')
file.write(html.encode('utf-8'))
mydict = {}
mydict['a']=file
f = mydict['a']

pass


def add_to_cache(self, url: str):
    salt = uuid4().hex
    cashe_url = md5(url.encode('utf-8') + salt.encode('utf-8'))
    if cashe_url not in self.cache.keys():
        try:
            html = requests.get(url).text
            file = open(f'{url}.html', 'wb')
            file.write(html.encode('utf-8'))
            self.cache[cashe_url] = file
        except Exception as err:
            print(err)
            return err