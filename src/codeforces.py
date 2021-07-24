# coding=utf-8
from bs4 import BeautifulSoup
from src.login import login
from datetime import datetime, timedelta

problem_id = list(range(672, 684, 1))

team_id_codeforces = {
    'Kaguya-sama wanna me AC': 153,
    'the_best_fishmen': 154,
    'DaLao666': 155,
    'Poor Math': 156,
    'Legal string': 157,
    'So you also play ACM': 158,
    'AAUB': 159,
    'so far so weak': 160,
    'the anonymous': 161,
    'FamerWzyYuki': 162,
    'I dont know.png': 163,
    'hotpot': 164,
    # 'Equilateral triangle': 165,
    '总之就是非常离谱': 166,
    'Debuggers': 167,
    '大吉大利，今晚吃 mian();': 168,
    'Blastoise': 169,
    'Ypa Girls': 170,
    'Life in BUAA with Involution from Zero': 171,
}


def parse_codeforces():
    f = open('board/codeforces_board.html', 'r', encoding='utf-8')
    html = ''.join(f.readlines())
    soup = BeautifulSoup(html, "html.parser")
    session = login()

    for row in soup.find_all('tr')[1:-1]:
        info = row.find_all('td')
        team = info[1].text.strip().split(':')[0]
        if team[0] == '*':
            continue
        if team not in team_id_codeforces:
            print(team)
            continue
        team = team_id_codeforces[team]

        pid = 0

        for detail in info[4:]:
            status = detail.text.strip()
            time = -1
            if ':' not in status:
                if '-' in status:
                    tries = -int(status)
                else:
                    tries = 0
            else:
                w, t = status.split('\n')
                h, m = list(map(int, t.split(':')))
                time = h * 60 + m
                if len(w) == 1: # +
                    tries = 0
                else:
                    tries = int(w[1:])
            if not (time == -1 and tries == 0):
                data = {
                    'problem': problem_id[pid],
                    'team': team,
                    'passed': time >= 0,
                    'dirt': tries,
                }
                if data['passed']:
                    sub_time = datetime.strptime('2021-07-22T12:00:00', '%Y-%m-%dT%H:%M:%S') + \
                               timedelta(minutes=time)
                    data['submission_time'] = sub_time.strftime('%Y-%m-%dT%H:%M:%S+08:00')
                print(data)
                r = session.post(f'http://127.0.0.1:8000/training/submission/', data=data)
                print(r.json())
                print(r.status_code)
            pid += 1
