import requests
import json
from time import sleep
from util.login import login


if __name__ == '__main__':
    params = {
        'team[]': '苍响',
        'begin_time': '2020-07-10T00:00:00+08:00',
        'end_time': '2020-09-04T00:00:00+08:00',

    }
    r = requests.get(f'http://127.0.0.1:8000/statistic/codeforces/problem_detail/', params=params)
    print(r.text)
