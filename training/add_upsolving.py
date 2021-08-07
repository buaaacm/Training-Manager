from util.login import login
import json
import requests
from datetime import timedelta, datetime


if __name__ == '__main__':
    session = login()

    name2team = dict()
    with open('../data/training/user_team_id.csv', 'r') as fpin:
        for line in fpin:
            line = line.strip().split(',')
            name2team[line[0]] = (line[1], line[2])

    print(name2team)
    problem_start = 704
    with open('../data/training/2021upsolving.csv', 'r') as fpin:
        lines = fpin.readlines()
    title = lines[0].strip().split(',')
    lines = lines[1:]
    print(title)
    for line in lines:
        upsolving = line.strip().split(',')
        name = upsolving[0]
        team_id, uid = name2team[name]
        length = len(upsolving)
        for i in range(1, length):
            pid = problem_start + ord(title[i]) - ord('A')
            if upsolving[i]:
                print(pid, team_id, uid, upsolving[i])
                data = {
                    'problem': pid,
                    'user': uid,
                    'team': team_id,
                }
                print(data)
                r = session.post(f'http://127.0.0.1:8000/training/upsolving/', data=data)
                print(r.text)
                print(r.status_code)

    # for i in range(problem_num):
    #     index = chr(i + ord('A'))
    #     print(r.json())
