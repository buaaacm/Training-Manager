from util.login import login
import json
import requests
from datetime import timedelta, datetime


if __name__ == '__main__':
    session = login()

    contest_id = 77
    problem_num = 11

    for i in range(problem_num):
        index = chr(i + ord('A'))
        r = session.post(f'http://127.0.0.1:8000/training/problem/',
                      data={'contest': contest_id, 'index': index})
        print(r.json())
