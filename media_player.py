
from bs4 import BeautifulSoup
import requests
from datetime import datetime


class Playlist:
    def __init__(self):
        self.link = None
        self.year = None
        self.subscription = None
        self.title = None
        self.like = None

    def search_film(self):
        try:
            url = "https://megogo.net/ua/films"
            py_headers = ({'User-Agent': 'Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
            py_wpage = requests.get(url, headers=py_headers)
            py_wpage.raise_for_status()
            py_soup = BeautifulSoup(py_wpage.content, "html.parser")
            parent = py_soup.find_all("div", class_="card-content video-content")
            data = []
            for i in parent:
                self.link = i.a['href']
                self.year = i.find('span', class_='video-year').text
                self.subscription = i.find('div', class_='free-label')
                if self.subscription is not None:
                    self.subscription = "Безкоштовно"
                self.title = i.find("h3", class_="video-title card-content-title").text
                data_films = (self.title + ' ' + self.link + ' ' + self.year + ' ' + str(self.subscription))\
                    .replace('\n', '').replace('  ', '')
                data.append(data_films)
            return data
        except requests.exceptions.HTTPError as errh:
            print("HTTP Error")
            print(errh.args[0])
        except requests.exceptions.ReadTimeout as errt:
            print("Time out")
        except requests.exceptions.ConnectionError as conerr:
            print("Connection error")

    def add_film_favorites(self):
        data = self.search_film()
        for all_films in data:
            if '2022' in all_films:
                films_2022 = all_films
                #print(films_2022)
                if "Безкоштовно" in films_2022:
                    films_2022_free = films_2022[films_2022.find('https'): films_2022.find('html') + 4]
                    url = films_2022_free
                    py_headers = ({'User-Agent': 'Safari/537.36', 'Accept-Language': 'en-US, en;q=0.5'})
                    py_wpage = requests.get(url, headers=py_headers)
                    py_soup = BeautifulSoup(py_wpage.content, "html.parser")
                    self.like = py_soup.find("button", class_="vote-button is-like").find('span').text[:-4]
                    if int(self.like) > 0:
                        file = open('to_watch_in_the_evening.txt', 'w', encoding='utf-8')
                        file.write(films_2022)
                        file.close()


class Player:

    def __init__(self, title, link, time=datetime.now().minute):
        self.title = title
        self.link = link
        self.time = time

    def play(self):
        with open('to_watch_in_the_evening.txt', 'r') as f:
            film = f.read()
        if self.title in film:
            return f'Фільм {self.title} доступний за посиланням {self.link}'
        elif self.title not in film:
            return f'Фільм {self.title} доступний за посиланням {self.link}'

    def pause(self):
        self.time = f'{str(self.time)} хвилині https://drive.google.com/file/d/1Nl_C8633uvz3lG1fWnO599nZErlCF_my/view?usp=drive_link'
        return f'Ви зупинилися на {self.time}'


playlist = Playlist()
playlist.search_film()
playlist.add_film_favorites()

player1 = Player('Я плюю на ваші могили', 'https://megogo.net/ua/view/24989-ya-plyuyu-na-vashi-mogili.html')
player2 = Player('Гангстер, Коп і Диявол', 'https://megogo.net/ua/view/5274455-gangster-kop-i-diyavol.html')
print(player1.play())
print(player1.pause())
# print(player2.play())
# print(player2.pause())