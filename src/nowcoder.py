# coding=utf-8
import json
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

from src.login import login

problem_id = list(range(750, 761, 1))

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
    '水箭龟队': 169,
    'BUAA_魔法少女': 170,
    '1145141919810': 171,
    '希望这次能出线': 172,
    'cxccxc': 172,
}

statuses = {}
rank_list = []


def parse_team_name_nowcoder():
    # rank-main class
    f = open('board/nowcoder_board.html', 'r', encoding='utf-8')
    html = f.readline()
    soup = BeautifulSoup(html, "html.parser")

    team_table = soup.find_all('table')[0]
    rank_table = soup.find_all('table')[1]

    team_rows = team_table.find_all('tr')[1:]
    row_num = len(team_rows)
    buaa = []

    for i in range(row_num):
        row = team_rows[i]
        team_name = row.find_all('td')[1].text.strip()
        if team_name not in team_id_nowcoder:
            print(team_name + ' not found.')
            buaa.append(-1)
        else:
            buaa.append(team_id_nowcoder[team_name])

    rank_rows = rank_table.find_all('tr')[1:]
    session = login()
    for i in range(row_num):
        row = rank_rows[i]
        team = buaa[i]
        if team == -1:
            continue
        pid = 0
        for grid in row.find_all('td'):
            status = grid.text.strip()
            wrong_tries = 0
            pass_time = -1

            if ':' in status:
                time_str = status[:8]
                hour, minute, _ = list(map(int, time_str.split(':')))
                pass_time = hour * 60 + minute
            if '(' in status:
                wrong_tries = -int(status.split('(')[1].split(')')[0])
            if not (pass_time == -1 and wrong_tries == 0):
                data = {
                    'problem': problem_id[pid],
                    'team': team,
                    'passed': pass_time >= 0,
                    'dirt': wrong_tries,
                }
                if data['passed']:
                    sub_time = datetime.strptime('2021-08-07T12:00:00', '%Y-%m-%dT%H:%M:%S') + \
                               timedelta(minutes=pass_time)
                    data['submission_time'] = sub_time.strftime('%Y-%m-%dT%H:%M:%S+08:00')
                r = session.post(f'http://127.0.0.1:8000/training/submission/', data=data)
                print(r.json())
                print(r.status_code)
            pid += 1


if __name__ == '__main__':
    parse_team_name_nowcoder()
