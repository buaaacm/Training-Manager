# coding=utf-8
import json
from datetime import date
from bs4 import BeautifulSoup

team_name_vjudge = {
  'nonsensetime': '趣味时光',
  'AccountNumber': '未定群名',
  'AwayWithCorrect': '打不赢电脑',
  'Butter_Fly': '无限大の梦',
  'woafrnraetns': '某人征婚',
  'BUAA_Alchemist': '试炼者',
  'Chinese_ham': '肉夹馍',
  'HolmiumJiang': 'CE：从爆零开始的ACM生活',
  'dragonylee': '很抱歉，该队名已被删除',
  'Potassium73': '萌新求带',
  'Kevin00': '根据相关法规，队名不予显示',
  'CoachXP': 'AC 怪',
  'hugegun': '我裂开了',
  '1937OvO': '将来我一定比你聪明比你强',
  
  'BUAA_mian': '*大吉大利，今晚吃 mian();',
  'yyxzhj': '*running_chicken',
}

statuses = {}
rank_list = []


def parse_vjudge(contest_name, contest_date=date.today()):
    f = open('board/vjudge_board.html', 'r')
    html = f.readline()
    soup = BeautifulSoup(html, "html.parser")
    problem_num = len((soup.find('tr')).find_all('th')) - 4

    for row in soup.find_all('tr')[1:]:
        info = row.find_all('td')
        team = info[1].text

        if "(" in team:
            team = team.split('(')[0][:-1]
        if team not in team_name_vjudge:
            continue

        pass_list = []  # .append((pid, pass_time, submit))
        pid = 0
        for detail in info[4:]:
            status = detail.text
            if len(status.strip()) == 0:
                pass_list.append((pid, -1, 0))
            elif ':' in status:
                if ' ' in status:
                    time, tries = status.split(' ')
                else:
                    time = status
                    tries = '(-0)'
                hour, minute, _ = list(map(int, time.split(':')))
                pass_list.append((pid, hour * 60 + minute, int(tries[2:-1])))
            else:
                pass_list.append((pid, -1, -int(status[2:-1])))

        rank_list.append(team_name_vjudge[team])
        statuses[team_name_vjudge[team]] = pass_list

    contest = {'title': contest_name, 'date': str(contest_date), 'num': problem_num, 'statuses': statuses,
               'ranklist': rank_list}
    print((json.dumps(contest)))