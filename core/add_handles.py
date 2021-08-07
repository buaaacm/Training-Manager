import requests
import json
from time import sleep
from util.login import login


if __name__ == '__main__':
    session = login()
    with open('handle.csv', 'r', encoding='utf-8') as fpin:
        lines = fpin.readlines()
        r = session.get('http://127.0.0.1:8000/participant/')
        users = json.loads(r.text)
        user_id_map = {user['name']: user['id'] for user in users}
        for line in lines:
            line = line.strip().split(',')
            if not line[3]:
                continue
            data = {
                # 'codeforces': line[1],
                # 'atcoder': line[2],
                'topcoder': line[3],
            }
            print(data)
            id = user_id_map[line[0]]
            r = session.patch(f'http://127.0.0.1:8000/participant/{id}/', data=data)
            print(r.text)
