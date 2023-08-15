from create_award_films import create_awards_list
import os


class MapMagic:
    def __init__(self):
        self.__map_open = "I solemnly swear that I am up to no good."
        self.__map_close = "Mischief managed."

    def get_map_open(self):
        print(self.__map_open)

    def get_map_close(self):
        print(self.__map_close)


class MarauderMap(MapMagic):
    __films_titles = {
        "results": [
            {
                "imdb_id": "tt1201607",
                "title": "Harry Potter and the Deathly Hallows: Part 2"
            },
            {
                "imdb_id": "tt0241527",
                "title": "Harry Potter and the Sorcerer's Stone"
            },
            {
                "imdb_id": "tt0926084",
                "title": "Harry Potter and the Deathly Hallows: Part 1"
            },
            {
                "imdb_id": "tt0304141",
                "title": "Harry Potter and the Prisoner of Azkaban"
            },
            {
                "imdb_id": "tt0417741",
                "title": "Harry Potter and the Half-Blood Prince"
            },
            {
                "imdb_id": "tt0295297",
                "title": "Harry Potter and the Chamber of Secrets"
            },
            {
                "imdb_id": "tt0330373",
                "title": "Harry Potter and the Goblet of Fire"
            },
            {
                "imdb_id": "tt0373889",
                "title": "Harry Potter and the Order of the Phoenix"
            }
        ]
    }

    @staticmethod
    def get_films_titles():
        title = [film['title']for film in MarauderMap.__films_titles['results']]
        return title

    def __init__(self, path):
        super().__init__()
        self.path = path

    def map_generator(self):

        self.get_map_open()
        awards = create_awards_list(self.path)
        dir_main = 'Harry_Potter'
        titles = self.get_films_titles()

        if not os.path.exists(dir_main):
            os.mkdir(dir_main)
            print("Створена директорія")
        else:
            print("Директорія вже існує")

        os.chdir(dir_main)

        title_film = []
        for title in titles:
            update_title = title.replace(' ', '_').replace(':', '')
            title_film.append(update_title)
            os.makedirs(update_title, exist_ok=True)

        os.chdir('..')
        path_sub_list = []

        for title in title_film:
            for i in range(ord('A'), ord('Z')):
                path_sub_dir = dir_main + '/' + title + '/' + chr(i)
                os.makedirs(path_sub_dir, exist_ok=True)

                for j in awards:
                    if path_sub_dir[-1:] == j['award_name'][:1] and j['title_film'] == \
                            path_sub_dir[(len(dir_main)):-2].replace('/',''):
                        path_sub_list.append(os.path.join(path_sub_dir, j['award_name']))

        for i in path_sub_list:
            with open(i + '.txt', 'w', encoding='UTF-8') as file_award:
                for j in awards:
                    if j['award_name'] == i[i.rfind('\\') + 1:] and \
                            j['title_film'] == i[(len(dir_main)):i.rfind('\\') - 2].replace('/', ''):
                        file_award.write(j['award'] + '\n')

        self.get_map_close()


map = MarauderMap('films_awards.json')
map.map_generator()