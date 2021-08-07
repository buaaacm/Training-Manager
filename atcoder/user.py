import requests
from bs4 import BeautifulSoup
from datetime import datetime
from json import loads
from time import sleep
from atcoder.login import login


def crawl(username, id, session):
    r = requests.get(f'https://atcoder.jp/users/{username}?lang=en')
    if r.status_code != 200:
        print(f'{username} failed')
        return
    soup = BeautifulSoup(r.text, 'html.parser')
    tables = soup.find_all('table')
    data = {
        'username': soup.find(class_='username').span.string,
        'country_region': list(tables[0].tr.td.stripped_strings)[0],
    }
    if len(tables) > 1:
        contest_info = tables[1]
        info = contest_info.find_all('tr')
        if len(info) == 4:
            # inactive
            info = [0] + info
        else:
            data['rank'] = int(info[0].td.string[0:-2])
        data['rating'] = int(info[1].span.string)
        data['max_rating'] = int(info[2].span.string)
        data['rated_matches'] = int(info[3].td.string)
        data['last_competed'] = datetime.strptime(info[4].td.string, '%Y/%m/%d').date()
    print(data)
    r = session.put(f'http://127.0.0.1:8000/atcoder/user/{id}/', data=data)
    print(r.text)


def update_all(session):
    r = session.get('http://127.0.0.1:8000/atcoder/user/')
    users = r.json()
    for user in users:
        # if user['last_updated'] >= '2020-08-16T20:47:52.613462+08:00':
        #     continue
        crawl(user['username'], user['id'], session)
        sleep(1)


if __name__ == '__main__':
    session = login()
    update_all(session)
    # users = ['zhongzihao',
    #          'chielo',
    #          'prime21',
    #          'maxdumbledore',
    #          'Hardict',
    #          'Atlantis592',
    #          'PotassiumWings',
    #          'qxforever',
    #          'nikkukun',
    #          'ws_zzyer',
    #          'x342333349',
    #          'shyakocat',
    #          'TownYan',
    #          'Marvolo',
    #          'liyuankai',
    #          'kipple',
    #          'holmium_jwh',
    #          'infinity37',
    #          'Zars19',
    #          'Craddy',
    #          'minamikotori',
    #          'Devil_Gary',
    #          'withinlover',
    #          'Rchen',
    #          'yyxzhj',
    #          'selia',
    #          'FYHSSGSS',
    #          'wxgwxg',
    #          'Mychael',
    #          'shjzhqm',
    #          'Bazoka13',
    #          'JJLeo',
    #          'L_RUA',
    #          'aspirine',
    #          'MisakaTao',
    #          'lgwza',
    #          'iuiou',
    #          'QuantumBolt',
    #          'kongyoubuaa',
    #          'serein',
    #          'dragonylee',
    #          'Member22335',
    #          'hujin',
    #          'sharco',
    #          'gobegobe',
    #          'YUKILSY',
    #          'wzy2001wzy',
    #          'airbust',
    #          'kazamori',
    #          'K98',
    #          ]
    # for user in users:
    #     crawl(user)
