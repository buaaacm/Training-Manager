# coding=utf-8
import json
from datetime import date
from bs4 import BeautifulSoup
from src.constants import *

statuses = {}
rank_list = []

team_name_codeforces = {
  'Nonsense Time': '趣味时光',
  'temporary': '未定群名',
  'Knocked out by AI': '打不赢电脑',
  'Butter_Fly': '无限大の梦',
  'fishing': '某人征婚',
  'Alchemist': '试炼者',
  'Chinese Hamburger': '肉夹馍',
  'CE_ACM Life From Zero': 'CE：从爆零开始的ACM生活',
  '404_name_not_found': '很抱歉，该队名已被删除',
  'freshmanAirProPlus': '萌新求带',
  '403 Forbidden': '根据相关法规，队名不予显示',
  'ACmonster': 'AC 怪',
  'We Gathered': '我裂开了',
  '将来我一定比你聪明比你强': '将来我一定比你聪明比你强',  

  '大吉大利，今晚吃 mian();': '*大吉大利，今晚吃 mian();',
  'running_chicken': '*running_chicken',
}

def parse_codeforces(contest_name, contest_date=date.today()):
    f = open('board/codeforces_board.html', 'r')
    html = ''.join(f.readlines())
    soup = BeautifulSoup(html, "html.parser")

    problem_num = len(soup.find_all('th')) - 4

    for row in soup.find_all('tr')[1:-1]:
        info = row.find_all('td')
        team = info[1].text.strip().split(':')[0]
        if team not in team_name_codeforces:
            continue
        team = team_name_codeforces[team]

        pass_list = []  # .append((pid, pass_time, submit))
        pid = 0

        for detail in info[4:]:
            status = detail.text.strip()
            if ':' not in status:
                if '-' in status:
                    tries = -int(status)
                else:
                    tries = 0
                pass_list.append((pid, -1, tries))
            else:
                w, t = status.split('\n')
                h, m = list(map(int, t.split(':')))
                time = h * 60 + m
                if len(w) == 1: # +
                    tries = 0
                else:
                    tries = int(w[1:])
                pass_list.append((pid, time, tries))
            pid += 1
        rank_list.append(team)
        statuses[team] = pass_list

    contest = {'title': contest_name, 'date': str(contest_date), 'num': problem_num, 'statuses': statuses,
               'ranklist': rank_list}
    print((json.dumps(contest)))