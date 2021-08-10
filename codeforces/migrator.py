import requests
import json


if __name__ == '__main__':
    with open('tmp.txt', 'r', encoding='utf-8') as fpin:
        lines = fpin.readlines()
        r = requests.get('http://127.0.0.1:8000/codeforces/contest/')
        r = json.loads(r.text)
        for line in lines:
            line = line.split('$')
            data = {
                "id": line[1],
                "name": line[2],
                "type": line[3],
                "start_time": line[4] + '+00:00',
                "duration_time_second": line[5],
                "division": line[6],
                "division_comment": line[7],
            }
            r = requests.post(f'http://127.0.0.1:8000/codeforces/contest/', data=data)
            print(r.text)