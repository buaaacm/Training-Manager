# coding=utf-8
import json
import time
from datetime import date
from src.constants import *
from bs4 import BeautifulSoup

# Saving time and penalty of all problems
statuses = {}

rank_list = []


class Competitor:
    def __init__(self, rank, name, problem, penalty, details):
        self.rank = rank
        self.name = name
        self.problem = problem
        self.penalty = penalty
        self.details = details


def time_passed(pass_time):
    # transform hh:mm:ss to minute
    h, m, s = pass_time.split(':')
    t = int(m) + int(h) * 60
    return t


def render_detail(pid, detail, first_solved_time, pass_list):
    html = ''
    first_solve = False
    pass_time, submit = -1, 0
    if detail == '@':
        pass
    elif ':' in detail:
        # Accepted
        html += '<span class="accepted">'
        if '-' not in detail:
            # Accepted with one submit
            if detail == first_solved_time:
                first_solve = True
            html += '+</span><br>%s</br>' % detail
            pass_time, submit = time_passed(detail), 0
        else:
            pass_time = detail[:8]
            if pass_time == first_solved_time:
                first_solve = True
            tries = detail[14:-1]
            html += '+%s</span><br>%s</br>' % (tries, pass_time)
            pass_time, submit = time_passed(pass_time), int(tries)
    else:
        # Haven't passed this problem
        html += '<span class="failed">'
        html += '%s</span>' % detail[1:-1]
        submit = -int(detail[1:-1])

    pass_list.append((pid, pass_time, submit))
    if first_solve:
        html = '<td style="background:lightgreen">' + html + '</td>'
    else:
        html = '<td>' + html + '</td>'
    return html


def print_row(rank, name, problem, penalty, details, first_solved_time):
    team_name = id_to_team_name_2017[name] if \
        name in id_to_team_name_2017 else name
    hour, minute, second = map(int, penalty.split(':'))
    html = u'<tr>'
    html += '<td>%d</td>' % rank
    html += '<td>%s</td>' % team_name
    html += '<td>%s</td>' % problem
    html += '<td>%d</td>' % (hour * 60 + minute)
    pass_list = []
    for detail, first, pid in zip(details, first_solved_time,
                                  range(len(details))):
        html += render_detail(pid, detail, first, pass_list)
    statuses[team_name] = pass_list
    rank_list.append(team_name)
    html += '</tr>'
    print "Log: ", team_name, problem, penalty
    return html


def print_table(contest_id, problem_num, competitors, problem_name,
                first_solved_time):
    table = ''
    header = '<tr><th>#</th><th>Who</th><th>=</th><th>Penalty</th>'

    for competitor in competitors:
        table += print_row(competitor.rank, competitor.name, competitor.problem,
                           competitor.penalty, competitor.details,
                           first_solved_time)

    for i in range(problem_num):
        header += '<th><a href="http://acm.hdu.edu.cn/contests/contest_show' \
                  'problem.php?pid=10%02d&cid=%d"' % (i + 1, contest_id)
        if problem_name is not None:
            header += ' title="%s"' % problem_name[i]
        header += '>%s</a></th>' % chr(ord('A') + i)
    header += '</tr>'

    return '<table><caption>Standings</caption><tbody>' + header + table + \
           '</tbody></table>'


def print_chart(length=300):
    changed_time = [0, length]
    for team in rank_list:
        for status in statuses[team]:
            if 0 <= status[1] <= length:
                changed_time.append(status[1])
        print("data.addColumn('number', '%s');" % team)
        print("data.addColumn({type:'string', role:'annotation'});")
    changed_time = sorted(set(changed_time))

    data = []
    for stamp in changed_time:
        score = {}
        for team in rank_list:
            solved, penalty = 0, 0
            for status in statuses[team]:
                if 0 <= status[1] <= stamp:
                    solved += 1
                    penalty += status[1] + status[2] * 20
            score[team] = (solved, -penalty)
        row = [stamp]

        for team in rank_list:
            rank = 1
            for key in score.keys():
                if score[key] > score[team]:
                    rank += 1
            row.append(-rank)

            solved_this_stamp = ''
            for status in statuses[team]:
                if status[1] == stamp:
                    solved_this_stamp += chr(ord('A') + status[0])
            if solved_this_stamp == '':
                row.append(None)
            else:
                row.append(solved_this_stamp)

        data.append(row)
    for row in data:
        print(json.dumps(row) + ",")


def print_scoreboard(contest_id, contest_name, file_name, problem_name=None,
                     contest_date=date.today()):
    try:
        f = open('board_html/%s.html' % file_name, "r")
    except IOError:
        return

    competitors = []
    rank = 0
    problem_num = 0
    for s in f:
        try:
            t = s.decode('utf-8')
        except UnicodeDecodeError:
            # Some characters can't be parsed by unicode.
            t = s.decode('gbk')

        if 'pr(' in t and BUAA in t:
            rank += 1
            items = t.split(',')
            team_name = items[2][1:-1]
            problem_solved = str(items[3])
            penalty = str(items[4])[1:-1]
            details = map(str, items[5].split(' '))[:-1]
            details[0] = details[0][1:]
            problem_num = len(details)
            competitors.append(Competitor(rank, team_name, problem_solved,
                                          penalty, details))
    f.close()

    first_solved_time = ['99:59:59'] * problem_num
    for competitor in competitors:
        for i in range(problem_num):
            if ':' in competitor.details[i]:
                solved_time = competitor.details[i]
                if '<' in solved_time:
                    solved_time = solved_time.split('<')[0]
                first_solved_time[i] = min(first_solved_time[i], solved_time)

    html = '<!DOCTYPE html><html><head><meta content="text/html;' \
           ' charset=UTF-8">'
    html += '<title>%s</title>' % contest_name
    html += '<link rel="stylesheet" type="text/css" href="style.css"></head>'
    html += '<body><h1>%s</h1>' % contest_name
    html += '<p>%s</p>' % contest_date
    html += print_table(contest_id, problem_num, competitors, problem_name,
                        first_solved_time)
    html += '<p class="copyright">Generated by <a href="https://github.com/' \
            'buaaacm/Training-Manager">Training Manager</a> at %s.</p>' \
            % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    html += '</body></html>'
    f = open('board/%s.html' % file_name, 'w')
    html = BeautifulSoup(html, 'html.parser').prettify()
    f.write(html.encode('utf-8'))
    f.close()

    print_chart()

    contest = {'title': contest_name, 'date': str(contest_date), 'num': problem_num, 'statuses': statuses,
               'ranklist': rank_list}
    print(json.dumps(contest))