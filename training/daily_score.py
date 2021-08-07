import json

from util.login import login

if __name__ == '__main__':
    session = login()
    # contest_id = 14
    # ranklist = [
    #     '苍响', '我不知道.png', '大吉大利，今晚吃 mian();', '试炼者', '辉夜大小姐想让我AC', '奔跑的小菜鸡', '地址过低', '从爆零开始的ACM生活', '未闻WA', '仰望星空',
    #     '将来我一定比你聪明比你强', '火锅队', '合法字符串', '铲车人', '从前往后做', '周末早上请不要训练', '路人队伍的养成方法', '我们不会起名'
    # ]
    contest_id = 17
    ranklist = ['苍响', '火锅队', '合法字符串', '铲车人', '仰望星空', '从爆零开始的ACM生活', '试炼者', '我不知道.png', '将来我一定比你聪明比你强', '地址过低',
                '大吉大利，今晚吃 mian();', '辉夜大小姐想让我AC', '奔跑的小菜鸡', '从前往后做', '路人队伍的养成方法', '未闻WA']

    data = {
        'contest': contest_id,
        'ranklist': json.dumps(ranklist)
    }
    print(data)
    r = session.post('http://127.0.0.1:8000/training/score_record/add_score_record/', data=data)
    print(r.text)
