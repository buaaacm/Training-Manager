# coding=utf-8
import json
from datetime import date
from bs4 import BeautifulSoup

team_name_vjudge = {
  'team120': u'瞎搞',
  'blackamoor': u'黑人问号.jpg',
  'deticxe': u'水能载舟',
  'team109': u'CE使我快乐',
  'ResuscitatedHope': u'复苏',
  'sro_orz': u'我们吓成一团了',
  'Ascender': u'TAT',
  'team_include': u'头文件',
  'Life_is_Perfect': u'人生已经如此的艰难',
  'heynihao': u'我需要治疗',
  'buaa_terminator': u'终结者',
  'tan90': u'不存在的',
  'tvcr': u'tvcr',
  'TooFarTooClose': u'极值点',
}

statuses = {}
rank_list = []


def parse_vjudge(contest_name, contest_date=date.today()):
    f = open('board_html/vjudge_board.html', 'r')
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
                hour, minute, second = map(int, time.split(':'))
                pass_list.append((pid, hour * 60 + minute, int(tries[2:-1])))
            else:
                pass_list.append((pid, -1, int(status[2:-1])))

        rank_list.append(team_name_vjudge[team])
        statuses[team_name_vjudge[team]] = pass_list

    contest = {'title': contest_name, 'date': str(contest_date), 'num': problem_num, 'statuses': statuses,
               'ranklist': rank_list, 'time': 390}
    print(json.dumps(contest))