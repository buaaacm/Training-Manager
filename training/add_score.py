from util.login import login
import json
from datetime import datetime
import requests


if __name__ == '__main__':
    session = login()
    team_name = [
        '苍响',
        '试炼者',
        '我不知道.png',
        '仰望星空',
        '未闻WA',
        '从爆零开始的ACM生活',
        '将来我一定比你聪明比你强',
        '大吉大利，今晚吃 mian();',
        '奔跑的小菜鸡',
        '铲车人',
        '辉夜大小姐想让我AC',
        '火锅队',
        '合法字符串',
        '路人队伍的养成方法',
        '我们不会起名',
        '地址过低',
        '周末早上请不要训练',
        '普通攻击是WA而且触发TLE还能RE的弟弟你喜欢吗',
        '从前往后做',
        '神奈川冲浪里',  # 20
    ]
    team_map = {id + 1: name for id, name in enumerate(team_name)}
    contest_rating = [
        ['07-12', 2, 16, 11, 1, 10, 6, 12, 7, 15, 19, 5, 4, 8, 14, 3, 20, 9, 13, 17, 18],
        ['07-13', 1, 9, 4, 2, 11, 3, 16, 8, 10, 12, 6, 19, 7, 5, 17, 13, 20, 15, 18, 14],
        ['07-18', 1, 9, 11, 12, 2, 19, 5, 10, 3, 4, 8, 7, 16, 6, 15, 13, 20, 17, 18, 14],
        ['07-20', 1, 3, 9, 2, 8, 6, 12, 11, 7, 4, 19, 5, 10, 16, 15, 20, 13, 17, 14, 18],
        ['07-23', 2, 8, 3, 11, 6, 7, 10, 4, 16, 9, 5, 13, 19, 15, 14, 12, 17],  #, 18, 1, 20],
        # last three should get 0 points, but team 18 got 1 point
        ['07-25', 1, 4, 9, 2, 16, 5, 8, 3, 11, 13, 19, 12, 20, 10, 17, 7, 15, 6, 18, 14],
        ['07-27', 4, 1, 3, 2, 10, 6, 9, 5, 7, 11, 16, 8, 12, 19, 13, 15, 14, 17, 20, 18],
        ['08-01', 1, 4, 16, 2, 12, 19, 8, 9, 11, 13, 3, 7, 5, 10, 6, 20, 15, 17, 14],  #, 18],
        # team 18 absent again
        ['08-03', 4, 1, 3, 12, 11, 6, 9, 2, 10, 16, 5, 13, 8, 7, 20, 19, 17, 14, 15],  #, 18],
        # team 18 absent again and again
        ['08-06', 1, 3, 8, 2, 10, 11, 16, 7, 4, 9, 6, 5, 19, 12, 20, 13, 17, 14],  # 18, 15],
        # team 18 and team 15 absent
        ['08-08', 1, 4, 8, 3, 2, 6, 11, 13, 12, 16, 10, 5, 9, 7, 20, 19, 15, 14, 17],  #, 18],
        # team 18 absent again and again
        ['08-10', 9, 1, 11, 3, 4, 2, 13, 6, 7, 16, 8, 10, 19, 5, 12, 17, 14, 15, 20],  #, 18],
        # team 18 absent again and again
    ]
    for contest in contest_rating:
        contest_info = session.get('http://127.0.0.1:8000/training/contest/get_problem',
                                   params={'date': '2020-' + contest[0]}).json()
        contest_id = contest_info[0]['id']
        ranklist = list(map(lambda id: team_map[id], contest[1:]))
        data = {
            'contest': contest_id,
            'ranklist': str(ranklist),
        }
        print(data)
        r = session.post('http://127.0.0.1:8000/training/score_record/add_score_record/', data=data)
        print(r.text)
