import os


def create_dir():
    path_dir = []
    dir_main = 'film_storage'
    for i in range(ord('A'), ord('Z')):
        path_sub_dir = dir_main + '/' + chr(i)
        path_dir.append(path_sub_dir)
        os.makedirs(path_sub_dir, exist_ok=True)
    return path_dir
