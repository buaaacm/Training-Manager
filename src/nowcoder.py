# coding=utf-8
import json
from datetime import date
from bs4 import BeautifulSoup

team_name_nowcoder = {
    'NonsenseTime': '趣味时光',
    '未定群名': '未定群名',
    '打不赢电脑': '打不赢电脑',
    'Buaa_Butter_Fly': '无限大の梦',
    'fishing': '某人征婚',
    'Alchemist': '试炼者',
    '肉夹馍': '肉夹馍',
    'CE：从爆零开始的ACM生活': 'CE：从爆零开始的ACM生活',
    '404_name_not_found': '很抱歉，该队名已被删除',
    'freshmanAirProPlus': '萌新求带',
    '根据相关法规，队名不予显示': '根据相关法规，队名不予显示',
    'ACmonster': 'AC 怪',
    '我裂开了': '我裂开了',
    '将来我一定比你聪明比你强': '将来我一定比你聪明比你强',
}

statuses = {}
rank_list = []


def parse_team_name_nowcoder(contest_name, contest_date=date.today()):
    f = open('board/nowcoder_board.html', 'r')
    html = f.readline()
    soup = BeautifulSoup(html, "html.parser")

    team_table = soup.find_all('table')[0]
    rank_table = soup.find_all('table')[1]

    team_rows = team_table.find_all('tr')[1:]
    row_num = len(team_rows)
    buaa = {}

    for i in range(row_num):
        row = team_rows[i]
        team_name = row.find_all('td')[1].text
        solved_problem_num = row.find_all('td')[3].text
        if solved_problem_num.endswith('AK'):
            solved_problem_num = solved_problem_num[:-2]
        solved_problem_num = int(solved_problem_num)
        
        buaa[i] = team_name
        # print(team_name, solved_problem_num)

    rank_rows = rank_table.find_all('tr')[1:]
    problem_num = len(rank_rows[0].find_all('td'))

    for i in range(row_num):
        row = rank_rows[i]
        team = buaa[i][:-1]
        pass_list = []
        pid = 0
        for grid in row.find_all('td'):
            status = grid.text.strip()
            wrong_tries = 0
            pass_time = -1

            if ':' in status:
                time_str = status[:8]
                hour, minute, second = list(map(int, time_str.split(':')))
                pass_time = hour * 60 + minute
            if '(' in status:
                wrong_tries = -int(status[:-1].split('(')[1])

            pass_list.append((pid, pass_time, wrong_tries))
            pid += 1

        if team in team_name_nowcoder:
            team = team_name_nowcoder[team]
        else:
            continue
        rank_list.append(team)
        statuses[team] = pass_list

    contest = {'title': contest_name, 'date': str(contest_date), 'num': problem_num, 'statuses': statuses,
               'ranklist': rank_list}
    print((json.dumps(contest)))
