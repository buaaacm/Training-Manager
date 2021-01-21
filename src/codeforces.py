# coding=utf-8
import json
from datetime import date
from bs4 import BeautifulSoup
from src.constants import *

statuses = {}
rank_list = []

team_name_codeforces = {
    'Retired': '苍响',
    'Alchemist': '试炼者',
    'I dont know.png': '我不知道.png',
    'Looking_up_at_the_starry_sky': '仰望星空',
    'TLE on test 233': '未闻WA',
    'CE_ACM Life From Zero': '从爆零开始的ACM生活',
    'wangzai milk': '将来我一定比你聪明比你强',
    '大吉大利，今晚吃 mian();': '大吉大利，今晚吃 mian();',
    'running_chicken': '奔跑的小菜鸡',
    'Die_Java': '铲车人',
    'Big Small Sister HY wants me AC': '辉夜大小姐想让我AC',
    'hotpot': '火锅队',
    'Legal string': '合法字符串',
    'ways to become passerby': '路人队伍的养成方法',
    'namespace': '我们不会起名',
    '^^^TOO LOW^^^': '地址过低',
    'no_morning_training': '周末早上请不要训练',
    '???': '普通攻击是WA而且触发TLE还能RE的弟弟你喜欢吗',
    'FamerWzyYuki': '从前往后做',
    'The Great Wave off Kanagawa': '神奈川冲浪里',
}

team_id_codeforces = {
    '苍响': 1,
    '试炼者': 2,
    '我不知道.png': 3,
    '仰望星空': 4,
    '未闻WA': 5,
    '从爆零开始的ACM生活': 6,
    '将来我一定比你聪明比你强': 7,
    '大吉大利，今晚吃 mian();': 8,
    '奔跑的小菜鸡': 9,
    '铲车人': 10,
    '辉夜大小姐想让我AC': 11,
    '火锅队': 12,
    '合法字符串': 13,
    '路人队伍的养成方法': 14,
    '我们不会起名': 15,
    '地址过低': 16,
    '周末早上请不要训练': 17,
    '普通攻击是WA而且触发TLE还能RE的弟弟你喜欢吗': 18,
    '从前往后做': 19,
    '神奈川冲浪里': 20,
}

def parse_codeforces(contest_name, contest_date=date.today()):
    f = open('board/codeforces_board.html', 'r', encoding='utf-8')
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
    print(rank_list)
