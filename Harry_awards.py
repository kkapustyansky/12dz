from film_award import films_awards
from pprint import pprint as pp


awards_list = []
title_f = ''
for i in films_awards:
    for j in i['results']:
        title_f = j['movie']['title'].replace(' ', '_').replace(':', '')
        if title_f:
            awards_list.append({
                                'type': j['type'],
                                'award_name': j['award_name'],
                                'award': j['award'],
                                'title_film': title_f
                })

# pp(awards_list)

awards = sorted(awards_list, key=lambda award: award['award_name'])
#print(awards)



