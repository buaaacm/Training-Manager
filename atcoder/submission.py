import requests
from bs4 import BeautifulSoup
import json
from atcoder.login import login


def query(session, contest, index, username, user_id=-1):
    data = {
        'name': contest['name'],
        'start_time': contest['start'],
        'duration_time_second': contest['duration'],
    }
    print(data)
    r = session.post('http://127.0.0.1:8000/atcoder/contest/', data=data)
    print(r.text)

    contest_code = contest['code']
    url = f'https://atcoder.jp/contests/{contest_code}/submissions'
    task_code = contest_code.replace('-', '_') + '_' + index.lower(),
    params = {
        'f.Task': task_code,
        'f.Status': 'AC',
        'f.User': username,
        'lang': 'en',
    }
    r = requests.get(url, params=params)
    soup = BeautifulSoup(r.text, features='html.parser')
    soup = soup.find_all('table')
    if not soup:
        return
    soup = soup[0]
    soup = soup.tbody
    submissions = soup.find_all('tr')
    for submission in submissions:
        infos = submission.find_all('td')
        submission_time = infos[0].time.string
        problem_name = infos[1].a.string.split('-')[1].strip()
        language = infos[3].string
        score = infos[4].string
        verdict = 'AC'
        time_consumed = infos[7].string.split()[0]
        space_consumed = infos[8].string.split()[0]
        submission_id = infos[9].a['href'].split('/')[-1]

        r = session.get('http://127.0.0.1:8000/atcoder/contest/get_contest/', params={'name': contest['name']})
        contest_id = r.json()[0]['id']
        data = {
            'contest': contest_id,
            'index': index,
            'name': problem_name,
            'points': score,
        }
        print(data)
        r = session.post('http://127.0.0.1:8000/atcoder/problem/', data=data)
        print(r.text)

        r = session.get('http://127.0.0.1:8000/atcoder/problem/get_problem',
                        params={'contest': contest_id, 'index': index})
        problem_id = r.json()[0]['id']
        data = {
            'id': submission_id,
            'user': user_id,
            'problem': problem_id,
            'creation_time': submission_time,
            'programming_language': language,
            'verdict': verdict,
            'time_consumed_millis': time_consumed,
            'memory_consumed_bytes': space_consumed,
        }
        print(data)
        r = session.post('http://127.0.0.1:8000/atcoder/submission/', data=data)
        print(r.text)


if __name__ == '__main__':
    session = login()
    users = [
        'Zars19',
        'Craddy',
        'JJLeo',
        'L_RUA',
        'aspirine',
        'MisakaTao',
        'lgwza',
        'iuiou',
        'QuantumBolt',
        'kongyoubuaa',
        'Bazoka13',
        'serein',
        'dragonylee',
        'hujin',
        'sharco',
        'qxforever',
        'nikkukun',
        'ws_zzyer',
        'x342333349',
        'shyakocat',
        'TownYan',
        'Marvolo',
        'liyuankai',
        'kipple',
        'holmium_jwh',
        'infinity37',
        'gobegobe',
        'YUKILSY',
        'wzy2001wzy',
        'airbust',
        'Kazamori',
        'minamikotori',
        'Devil_Gary',
        'withinlover',
        'Rchen',
        'yyxzhj',
        'selia',
        'FYHSSGSS',
        'wxgwxg',
        'Mychael',
        'shjzhqm',
        'zhongzihao',
        'K98',
        'Member22335',
        'chielo',
        'Prime21',
        'maxdumbledore',
        'Hardict',
        'Atlantis592',
        'PotassiumWings',
    ]
    for user in users:
        r = session.get('http://127.0.0.1:8000/atcoder/user/get_user', params={'username': user})
        user_id = r.json()['id']
        print(user, user_id)
        with open('info.json', 'r') as fpin:
            contests = json.load(fpin)
            for contest in contests:
                problems = contest['problems']
                for index in range(problems):
                    index = chr(ord('A') + index)
                    try:
                        query(session, contest, index, user, user_id)
                    except Exception:
                        pass
