# coding=utf-8
import json
from datetime import date
from bs4 import BeautifulSoup

team_name_nowcoder = {
  'team1': u'趣味时光',
  'team2': u'小黄鸡咕咕咕',
  'team3': u'啊，队友呢？！',
  'team4': u'比宇宙更远的地方',
  'team5': u'除了AC',
  'team6': u'从不刷题队',
  'team7': u'“”',
  'team8': u'梦中做自己',
  'team9': u'菜里别加鎕',
  'team10': u'点击输入队名',
  'team11': u'稽不择名',
  'team12': u'彩笔队',
  'team13': u'怪兽防卫团',
}

statuses = {}
rank_list = []


def parse_team_name_nowcoder(contest_name, contest_date=date.today()):
    f = open('board_html/nowcoder_board.html', 'r')
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
        # print team_name, solved_problem_num

    rank_rows = rank_table.find_all('tr')[1:]
    problem_num = len(rank_rows[0].find_all('td'))

    for i in range(row_num):
        if i not in buaa:
            continue
        row = rank_rows[i]
        team = buaa[i]
        pass_list = []
        pid = 0
        for grid in row.find_all('td'):
            status = grid.text.strip()
            wrong_tries = 0
            pass_time = -1

            if ':' in status:
                time_str = status[:8]
                hour, minute, second = map(int, time_str.split(':'))
                pass_time = hour * 60 + minute
            if '(' in status:
                wrong_tries = -int(status[:-1].split('(')[1])

            pass_list.append((pid, pass_time, wrong_tries))
            pid += 1

        if team in team_name_nowcoder:
            team = team_name_nowcoder[team]
        rank_list.append(team)
        statuses[team] = pass_list

    contest = {'title': contest_name, 'date': str(contest_date), 'num': problem_num, 'statuses': statuses,
               'ranklist': rank_list}
    print(json.dumps(contest))