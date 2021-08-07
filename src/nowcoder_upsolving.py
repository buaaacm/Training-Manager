from login import login
import requests
import json
from datetime import datetime
from time import sleep

counter = {}
added = set()
session = login()

team_id_nowcoder = {
    '沃尔沃夫': 153,
    '又是困难的取名时间了': 154,
    '全场最佳观众席': 155,
    '欺负人没有数理基础？': 156,
    'LegalString': 157,
    '原来你也打ACM': 158,
    '新生队': 159,
    '我完全不会.jpg': 160,
    '起名苦手': 161,
    '罚时第一名': 162,
    '我不知道.png': 163,
    'hotpot': 164,
    '等边三角形': 165,
    '总之就是非常离谱': 166,
    '捉虫少年': 167,
    '大吉大利，今晚吃mian();': 168,
    '大吉大利，晚上吃mian();': 168,
    '水箭龟队': 169,
    'BUAA_魔法少女': 170,
    '1145141919810': 171,
    '希望这次能出线': 172,
    'cxccxc': 172,
}

contest_problem_id = {
    11253: 660,
    11254: 684,
    11255: 694,
    11256: 716,
    11257: 727,
    11258: 750,
}

total_updated = 0


def get_teams_from_contest(contest_id):
    url = ('https://ac.nowcoder.com/acm-heavy/acm/contest/' +
           'real-time-rank-data?token=&id={0}&searchUserName=' +
           '%E5%8C%97%E4%BA%AC%E8%88%AA%E7%A9%BA%E8%88%AA%E5%A4%A9%E5%A4%A7%E5%AD%A6').format(
        contest_id)
    response = requests.get(url)
    data = response.json()['data']
    problem_num = len(data['problemData'])
    names = []
    for team in data['rankData']:
        names.append(team['userName'])
    for name in names:
        if name not in team_id_nowcoder:
            print(f'name {name} not found')
    return problem_num, names


def get_status(team_name, contest_id, problem_num):
    url = ('https://ac.nowcoder.com/acm-heavy/acm/contest/status-list' +
           '?token=&id={0}&pageSize=50&statusTypeFilter=5&searchUserName={1}').format(contest_id, team_name)
    response = requests.get(url)
    data = response.json()
    solved = [None for i in range(problem_num)]
    for submission in data['data']['data']:
        if submission['userName'] == team_name:
            if team_name not in team_id_nowcoder:
                continue
            team_id = team_id_nowcoder[team_name]
            sub_time = datetime.fromtimestamp(submission['submitTime'] // 1000).strftime('%Y-%m-%dT%H:%M:%S+08:00')
            problem_index = ord(submission['index']) - ord('A')
            problem_id = contest_problem_id[contest_id] + problem_index
            data = {
                'team': team_id,
                'problem': problem_id,
                'submission_time': sub_time,
            }
            # print(data)
            if solved[problem_index] is None or solved[problem_index]['submission_time'] > data['submission_time']:
                solved[problem_index] = data
        else:
            print(f"error {submission['userName']}")
    if team_name not in counter:
        counter[team_name] = 0
    for id in solved:
        if id is not None:
            counter[team_name] += 1
            if (id['problem'], id['team']) in added:
                print(f'{id} has been added')
                continue
            print(id)
            r = session.post('http://127.0.0.1:8000/training/upsolving_submission/', data=id)
            print(r.text)
            print(r.status_code)
            global total_updated
            total_updated += 1
    return solved


if __name__ == '__main__':
    r = session.get('http://127.0.0.1:8000/training/upsolving_submission/')
    result = r.json()
    for sub in result:
        added.add((sub['problem'], sub['team']))
    contest_list = [11253, 11254, 11255, 11256, 11257, 11258]

    for contest_id in contest_list:
        print("### {0}".format(contest_id))
        problem_num, teams = get_teams_from_contest(contest_id)

        for team in teams:
            try:
                print(team, get_status(team, contest_id, problem_num))
            except requests.exceptions.ProxyError as e:
                print(e)
                sleep(10)
                print(team, get_status(team, contest_id, problem_num))

    print(counter)
    print(f'{total_updated} added this time')