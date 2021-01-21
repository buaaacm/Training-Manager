# coding=utf-8
import json
from datetime import date

from bs4 import BeautifulSoup

team_name_nowcoder = {
    'IntrepidSword': '苍响',
    'Alchemist': '试炼者',
    '我不知道.png': '我不知道.png',
    'Looking_up_at_the_starry_sky': '仰望星空',
    '未闻WA': '未闻WA',
    'CE：从爆零开始的ACM生活': '从爆零开始的ACM生活',
    '将来我一定比你聪明比你强!': '将来我一定比你聪明比你强',
    '大吉大利，晚上吃mian();': '大吉大利，今晚吃 mian();',
    'running_chicken': '奔跑的小菜鸡',
    '铲车人': '铲车人',
    '辉夜大小姐想让我AC': '辉夜大小姐想让我AC',
    'hotpot': '火锅队',
    'Legal_string': '合法字符串',
    '路人队伍的养成方法': '路人队伍的养成方法',
    '我们不会起名': '我们不会起名',
    '^^^TOOLOW^^^': '地址过低',
    '周末早上请不要训练': '周末早上请不要训练',
    'BigBros': '普通攻击是WA而且触发TLE还能RE的弟弟你喜欢吗',
    '从前往后做': '从前往后做',
    '神奈川冲浪里': '神奈川冲浪里',
}

team_id_nowcoder = {
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

statuses = {}
rank_list = []


def parse_team_name_nowcoder(contest_name, contest_date=date.today()):
    # rank-main class
    f = open('board/nowcoder_board.html', 'r', encoding='utf-8')
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
                hour, minute, _ = list(map(int, time_str.split(':')))
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

    print(rank_list)
    print(', '.join(map(str, [team_id_nowcoder[team] for team in rank_list])))
