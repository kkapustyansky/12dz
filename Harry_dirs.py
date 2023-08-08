import os
from title_file import films_titles
from Harry_awards import awards


def Harry_dirs():
    dir_main = 'Harry_Potter'
    if not os.path.exists(dir_main):
        os.mkdir(dir_main)
        print("Створена директорія")
    else:
        print("Директорія вже існує")
    
    os.chdir(dir_main)
    
    title_film = []
    for i in films_titles['results']:
        update_title = i['title'].replace(' ', '_').replace(':', '')
        title_film.append(update_title)
        os.makedirs(update_title, exist_ok=True)
    
    os.chdir('..')
    path_sub_list = []
    for title in title_film:
        for i in range(ord('A'), ord('Z')):
            path_sub_dir = dir_main + '/' + title + '/' + chr(i)
            os.makedirs(path_sub_dir, exist_ok=True)
    
            for j in awards:
                if path_sub_dir[-1:] == j['award_name'][:1] and j['title_film'] == path_sub_dir[(len(dir_main)):-2].replace('/', ''):
                    path_sub_list.append(os.path.join(path_sub_dir, j['award_name']))
    
    for i in path_sub_list:
        with open(i + '.txt', 'w', encoding='UTF-8') as file_award:
            for j in awards:
                if j['award_name'] == i[i.rfind('\\')+1:] and \
                        j['title_film'] == i[(len(dir_main)):i.rfind('\\')-2].replace('/', ''):
                    file_award.write(j['award'] + '\n')
