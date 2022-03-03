from bs4 import BeautifulSoup
import re
import math
import os


ban = [
    '陈楚岩',
    '赵子涵',
    '张思淼',
    'jrt',
    '---',
    '姜华祖',
    '哦辉夜大小姐想让我AC',
    '吕双羽',
    'Withinlover',
    'buaa_陶虹宇_罚时第一名',
    '江周',
    '王智彪',
    '丁家玮',
    '余浩男',
    '王梓源',
    '范泽恒',
    '樊佳昊',
]

alias = {
    '刘怀远': '\zyf/后援队',
    '程泽轩': '程泽轩&张思淼&赵子涵',
    '姜雨竺': '全场最佳观众席',
    '潘誉夫': '等边三角形',
    '王子恒': '陈楚岩&王子恒&李成蹊',
    '高湘一': '水箭龟队',
    '水箭龟队（高湘一王梓源余浩男）': '水箭龟队',
    '路人队伍的养成方法': '\zyf/后援队',
    '2073李翔宇': '江周&李翔宇&姜华祖',
    '温佳昊': '温佳昊&吕诚鑫&韩一',

}


class Contestant:
    def __init__(self, name=''):
        self.name = name
        self.points = 0
        self.rank = 0
        self.rating = 1500
        self.delta = 0
        self.seed = 0
        self.need_rating = 0
        self.rating_history = dict()
        self.rank_history = dict()


def get_elo_win_probability(ra, rb):
    return 1.0 / (1 + 10 ** ((rb - ra) / 400))


def get_seed(contestants, contestant, rating):
    result = 1
    for other in contestants:
        if other == contestant:
            continue
        result += get_elo_win_probability(other.rating, rating)
    return result


def get_rating_to_rank(contestants, contestant, rank):
    left, right = 1, 8000
    while right - left > 1:
        mid = (left + right) // 2
        if get_seed(contestants, contestant, mid) < rank:
            right = mid
        else:
            left = mid
    return left


def reassign_ranks(contestants):
    contestants.sort(key=lambda c: c.points, reverse=True)
    for contestant in contestants:
        contestant.rank = 0
        contestant.delta = 0
    first = 0
    points = contestants[0].points
    for i in range(1, len(contestants)):
        if contestants[i].points < points:
            for j in range(first, i):
                contestants[j].rank = i
            first = i
            points = contestants[i].points
    rank = len(contestants)
    for i in range(first, rank):
        contestants[i].rank = rank


def process(contestants):
    if len(contestants) == 0:
        return
    reassign_ranks(contestants)
    for a in contestants:
        a.seed = 1
        for b in contestants:
            if a != b:
                a.seed += get_elo_win_probability(b.rating, a.rating)

    for contestant in contestants:
        mid_rank = (contestant.rank * contestant.seed) ** 0.5
        contestant.need_rating = get_rating_to_rank(contestants, contestant, mid_rank)
        contestant.delta = (contestant.need_rating - contestant.rating) // 2

    contestants.sort(key=lambda c: c.rating, reverse=True)
    sum = 0
    for c in contestants:
        sum += c.delta
    inc = -sum // len(contestants) - 1
    for contestant in contestants:
        contestant.delta += inc

    # sum = 0
    # zero_sum_count = min(int(4 * round(len(contestants) ** 0.5)), len(contestants))
    # for i in range(zero_sum_count):
    #     sum += contestants[i].delta
    # inc = min(max(-sum // zero_sum_count, -10), 0)
    # for contestant in contestants:
    #     contestant.delta += inc

    # todo: validate delta


def calc_rating(contestants, names, contest):
    contestant_present = list()
    for rk, name in enumerate(names):
        if name not in contestants:
            new_contestant = Contestant(name=name)
            contestants[name] = new_contestant
        score = -rk
        contestant_present.append(contestants[name])
        contestant_present[-1].rank_history[contest] = rk + 1
        contestant_present[-1].points = score

    process(contestant_present)
    for contestant in contestant_present:
        contestant.rating += contestant.delta
        # print(contestant.name, contestant.points, contestant.rating)
        contestant.rating_history[contest] = contestant.rating


if __name__ == '__main__':
    contestants = dict()
    contest_num = 5
    for contest_id in range(1, contest_num + 1):
        with open(f'2021 BUAA Spring Training {contest_id} - Virtual Judge.html', 'r') as fpin:
            board = BeautifulSoup(fpin, features='html.parser')
            tables = board.find_all('table')
            board = tables[2]
            lines = board.find_all('tr')[4:]
            names = list()
            for line in lines:
                name = line.find_all('td')[1].div.a.contents
                if len(name) < 2:
                    continue
                name = name[1].string[1:-1]
                if name in ban:
                    continue
                if name in alias:
                    name = alias[name]
                names.append(name)
            calc_rating(contestants, names, contest_id)
    with open('result.csv', 'w', encoding='gbk') as fpout:
        title = ['姓名']
        for contest_id in range(1, contest_num + 1):
            title.append(f'rating {contest_id}')
            title.append(f'rank {contest_id}')
        title.append('final rating')
        fpout.write(','.join(title) + '\n')
        for name, contestant in contestants.items():
            output = [name]
            last = 0
            for contest_id in range(1, contest_num + 1):
                output.append(str(contestant.rating_history.get(contest_id, '-')))
                output.append(str(contestant.rank_history.get(contest_id, '-')))
                if contest_id in contestant.rating_history:
                    last = contestant.rating_history[contest_id]
            output.append(str(last))
            fpout.write(','.join(output) + '\n')
