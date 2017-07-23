#coding=utf-8

from constants import *
from datetime import date


def render_detail(detail):
    html = '<td>'
    if detail == '@':
        # Haven't tried this problem
        pass
    elif ':' in detail:
        # Accepted
        html += '<span class="accepted">'
        if '-' not in detail:
            # Accepted with one submit
            html += '+</span><br>%s</br>' % detail
        else:
            time = detail[:8]
            tries = detail[14:-1]
            html += '+%s</span><br>%s</br>' % (tries, time)
    else:
        # Haven't passed this problem
        html += '<span class="failed">'
        html += '%s</span>' % detail[1:-1]
    html += '</td>'
    return html


def print_row(rank, name, problem, penalty, details):
    html = u'<tr>'
    html += '<td>%d</td>' % rank
    html += '<td>%s</td>' % name
    html += '<td>%s</td>' % problem
    html += '<td><b>%s</b></td>' % penalty
    for detail in details:
        html += render_detail(detail)
    html += '</tr>'
    return html


def print_table(file_name):
    rank = 0
    table = ''
    problem_num = 0
    header = '<tr><th>#</th><th>Who</th><th>=</th><th>Penalty</th>'

    f = open('board_html/%s.html' % file_name, "r")
    for s in f:
        try:
            t = s.decode('utf-8')
        except UnicodeDecodeError:
            # Some characters can't be parsed by unicode.
            t = s.decode('gbk')

        if "pr" in t and BUAA in t:
            rank += 1
            items = t.split(',')
            team_name = items[2][1:-1]
            problem_solved = str(items[3])
            penalty = str(items[4])[1:-1]
            details = map(str, items[5].split(' '))[:-1]
            details[0] = details[0][1:]
            problem_num = len(details)
            table += print_row(rank, team_name, problem_solved, penalty, details)
    f.close()

    for i in range(problem_num):
        header += '<th><a href="">%s</a></th>' % chr(ord('A') + i)
    header += '</tr>'
    return '<table><caption>Standings</caption><tbody>' + header + table + '</tbody></table>'


def print_scoreboard(contest_name, file_name, date=date.today()):
    html = '<!DOCTYPE html><html><head><meta content="text/html; charset=UTF-8">'
    html += '<title>%s</title>' % contest_name
    html += '<link rel="stylesheet" type="text/css" href="style.css"></head>'
    html += '<body><h1>%s</h1>' % contest_name
    html += '<p>%s</p>' % date
    html += print_table(file_name)
    html += '</body></html>'
    f = open('board/%s.html' % file_name, 'w')
    f.write(html)
    f.close()

print_scoreboard('2015 Multi-University Training Contest 1', '01')
print_scoreboard('2015 Multi-University Training Contest 2', '02')
print_scoreboard('2015 Multi-University Training Contest 3', '03')
print_scoreboard('2015 Multi-University Training Contest 4', '04')