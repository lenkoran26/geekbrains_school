import requests
from uuid import uuid4
from hashlib import md5

class Cache():
    # инициализируем кэш и соль
    def __init__(self, cashe=None):
        if cashe is None:
            cashe = {}
        self.cache = cashe
        self.salt = uuid4().hex

    # добавляем страницу в кэш, если ее нет. В качестве ключей используем хэш-значение URL
    def add_to_cache(self, url: str):
        # получаем хэш адреса
        cashe_url = md5(url.encode('utf-8')+self.salt.encode('utf-8')).hexdigest()
        # если адреса страницы в кэше нет, создаем html-файл и добавляем в кэш
        if cashe_url not in self.cache.keys():
            try:
                html = requests.get(url).text
                filename = url.replace('/', '_')
                file = open(f'{filename}.html', 'wb')
                file.write(html.encode('utf-8'))
                self.cache[cashe_url] = file
            except Exception as err:
                print(err)
                return err

    # получение страницы из кэша
    def get_html(self, url):
        cashe_url = md5(url.encode('utf-8')+self.salt.encode('utf-8')).hexdigest()
        if cashe_url in self.cache.keys():
            return self.cache[cashe_url]
        # если страницы в кэше нет, скачиваем и отдаем пользователю (упрощенно)
        else:
            req = requests.get(url)
            html = req.text
            return html

