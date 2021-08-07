from util.login import login
import json
import requests
from datetime import timedelta, datetime


if __name__ == '__main__':
    session = login()
    r = session.get('http://127.0.0.1:8000/training/contest/')
    problems = session.get('http://127.0.0.1:8000/training/problem/').json()
    teams = set()

    teams_id = [
        [2, '试炼者'],
        [3, '我不知道.png'],
        [5, '未闻WA'],
        [7, '将来我一定比你聪明比你强'],
        [9, '奔跑的小菜鸡'],
        [12, '火锅队'],
        [14, '路人队伍的养成方法'],
        [15, '我们不会起名'],
        [17, '周末早上请不要训练'],
        [19, '从前往后做'],
        [20, '神奈川冲浪里'],
        [4, '仰望星空'],
        [10, '铲车人'],
        [1, '苍响'],
        [18, '普通攻击是WA而且触发TLE还能RE的弟弟你喜欢吗'],
        [8, '大吉大利，今晚吃 mian();'],
        [16, '地址过低'],
        [11, '辉夜大小姐想让我AC'],
        [13, '合法字符串'],
        [135, '三个队友跑了'],
        [6, '从爆零开始的ACM生活'],
        [136, '欺负人没有数理基础？'],
    ]

    for contest in r.json():

        # for i in range(num):
        #     index = chr(i + ord('A'))
        #     r = session.post(f'http://127.0.0.1:8000/training/problem/',
        #                   data={'contest': contest['id'], 'index': index})
        #     print(r.json())

        board = json.loads(contest['board'])
        if board['date'][:4] == '2020':
            for team, value in board['statuses'].items():
                teams.add(team)
                num = len(value)
                team_id = -1
                for id, name in teams_id:
                    if name == team:
                        team_id = id
                        break
                if team_id == -1:
                    print(team)
                    assert False
                for i in range(num):
                    index = chr(i + ord('A'))
                    problem_id = -1
                    for problem in problems:
                        if problem['index'] == index and problem['contest'] == contest['id']:
                            problem_id = problem['id']
                            break
                    penalty = value[i][1]
                    dirt = value[i][2]
                    if penalty == -1 and dirt == 0:
                        continue
                    data = {
                        'problem': problem_id,
                        'team': team_id,
                        'passed': penalty >= 0,
                        'dirt': dirt,
                    }
                    if data['passed']:
                        sub_time = datetime.strptime(contest['start_time'], '%Y-%m-%dT%H:%M:%S+08:00') +\
                                   timedelta(minutes=value[i][1])
                        data['submission_time'] = sub_time.strftime('%Y-%m-%dT%H:%M:%S+08:00')
                    print(data)
                    r = session.post(f'http://127.0.0.1:8000/training/submission/', data=data)
                    print(r.json())

    print(teams)
