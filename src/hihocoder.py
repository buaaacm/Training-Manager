# coding=utf-8
import json
from datetime import date
from bs4 import BeautifulSoup
from src.constants import *

statuses = {}
rank_list = []


def parse_hihocoder(contest_name, contest_date=date.today()):
    f = open('board_html/hihocoder_board.html', 'r')
    html = ''.join(f.readlines())
    soup = BeautifulSoup(html, "html.parser")

    problem_num = len(soup.find('tr').find_all('td')) - 5

    for row in soup.find_all('tr')[1:]:
        info = row.find_all('td')

        school = info[1].text
        if school != u'北京航空航天大学':
            continue

        team = info[2].text
        if team not in id_to_team_name_beijing:
            continue

        pass_list = []  # .append((pid, pass_time, submit))
        pid = 0

        for detail in info[5:]:
            status = detail.text.strip()
            print status
            if ':' not in status:
                if '(' in status:
                    tries = -int(status[1:-1])
                else:
                    tries = 0
                pass_list.append((pid, -1, tries))
                # print(tries)
            else:
                if '(' in status:
                    sp = status.split('(')[0]
                    tries = int(status.split('(')[1][:-1])
                else:
                    sp = status
                    tries = 0
                h, m, s = map(int, sp.split(':'))
                time = h * 60 + m
                pass_list.append((pid, time, tries))
                # print(time, tries)
        rank_list.append(id_to_team_name_beijing[team])
        statuses[id_to_team_name_beijing[team]] = pass_list

    contest = {'title': contest_name, 'date': str(contest_date), 'num': problem_num, 'statuses': statuses,
               'ranklist': rank_list}
    print(json.dumps(contest))