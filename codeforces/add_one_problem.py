import requests
import json
from time import sleep


if __name__ == '__main__':
    data = {
        'contest': 1376,
        'index': 'A1',
        'name': 'Sort the Numbers',
        'type': 'PROGRAMMING',
        # 'rating': 2100,
        # 'points': 2000,
        # 'alias': 425,
    }
    r = requests.post('http://127.0.0.1:8000/codeforces/problem/', data=data)
    print(r.text)
