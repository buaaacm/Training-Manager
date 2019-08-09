# coding=utf-8
import json
from datetime import date
from bs4 import BeautifulSoup
from src.constants import *

statuses = {}
rank_list = []


def parse_jisuanke(contest_name, contest_date=date.today()):
    f = open('board_html/jisuanke_board.html', 'r')
    html = f.readline()
    soup = BeautifulSoup(html, "html.parser")

    problem_num = len((soup.find('tr')).find_all('th')) - 6

    for row in soup.find_all('tr')[1:]:
        info = row.find_all('td')
        team = info[2].text
        if "(" in team:
            team = team.split('(')[0][:-1]
        if team not in id_to_team_name_xian:
            continue

        pass_list = []  # .append((pid, pass_time, submit))
        pid = 0
        for detail in info[6:]:
            status = detail.text
            time, tries = status.split('(')
            tries = tries[:-1]
            # print time, tries
            if time != '--':
                pass_list.append((pid, int(time), int(tries) - 1))
            else:
                pass_list.append((pid, -1, int(tries)))

        rank_list.append(id_to_team_name_xian[team])
        statuses[id_to_team_name_xian[team]] = pass_list

    contest = {'title': contest_name, 'date': str(contest_date), 'num': problem_num, 'statuses': statuses,
               'ranklist': rank_list}
    print((json.dumps(contest)))