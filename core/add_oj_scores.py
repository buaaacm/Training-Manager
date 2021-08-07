from util.login import login
import json


if __name__ == '__main__':
    session = login()
    teams = [
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
        '神奈川冲浪里',
    ]
    r = session.get('http://api.buaaacm.com:8008/statistic/atcoder/rating/', params={
        'team[]': teams,
        'begin_time': '2020-07-10T00:00:00+08:00',
        'end_time': '2020-09-04T00:00:00+08:00',
    })
    team_rating = sorted(r.json().items(), key=lambda x: x[1], reverse=True)
    print(team_rating)
    score_distribution = [100, 75, 60, 45, 35, 25, 20, 15, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    data = dict()
    cur_rank = 0
    for i in range(len(team_rating)):
        name = team_rating[i][0]
        rating = team_rating[i][1]
        if i > 0 and rating < team_rating[i - 1][1]:
            cur_rank = i
        data[name] = score_distribution[cur_rank] if cur_rank < len(score_distribution) else 0
        if rating == 0:
            data[name] = 0
    print(data)
    # r = session.post('http://127.0.0.1:8000/score_record/add_score_record/',data={
    #     'team_score': json.dumps(data),
    #     'source': 'topcoder',
    #     'identifier': '2020_rating',
    # })
    # print(r.text)
