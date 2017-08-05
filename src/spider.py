# coding=utf-8

import os
import requests
from bs4 import BeautifulSoup
from src import print_scoreboard


class HduModule(object):
    def __init__(self, contest_id):
        object.__init__(self)
        self.session = requests.Session()
        headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/'
                        '537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 '
                        'Safari/537.36'
        }
        self.session.headers.update(headers)
        self.contest_id = contest_id

    def login(self, username, password):
        url = 'http://acm.hdu.edu.cn/userloginex.php?action=login&cid=%d' % \
              self.contest_id
        data = {
          'username': username,
          'userpass': password,
          'login': 'Sign In',
        }
        headers = {
          'host': 'acm.hdu.edu.cn',
          'origin': 'http://acm.hdu.edu.cn',
          'referer': 'http://acm.hdu.edu.cn/'
        }
        self.session.post(url, data=data, headers=headers)

    def get_usercode(self, rid):
        url = 'http://acm.hdu.edu.cn/viewcode.php?rid=' + rid + '&cid=%d' % \
                                                                self.contest_id
        r = self.session.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        code = soup.find('textarea', id='usercode').text
        return code

    # def get_ac_list(self, page):
        # url = 'http://acm.hdu.edu.cn/contests/contest_status.php?cid=705&user
        # =&pid=&lang=&status=5&page=' + str(page)
        # res = self.session.get(url).text
        # parser = StatusPageParser()
        # parser.feed(res)
        # return parser.ac_list

    def save_file(self, filename, data):
        fp = open(filename, 'w')
        fp.write(data)
        fp.close()

    def get_all(self):
        for i in range(1, 50):
            ac_list = []  # self.get_ac_list(i)
            print(ac_list)
            for ac in ac_list:
                rid = ac['rid']
                lang = ac['lang']
                team = ac['team']
                pid = ac['pid']
                code = self.get_usercode(rid)
                if os.path.exists(pid) is False:
                    os.makedirs(pid)
                if lang == 'G++':
                    ext = '.cpp'
                elif lang == 'GCC':
                    ext = '.c'
                else:
                    ext = '.java'
                filename = pid + '/' + team + ext
                self.save_file(filename, code)

    def get_scoreboard(self):
        url = 'http://acm.hdu.edu.cn/contests/client_ranklist.php?cid=%d' % \
              self.contest_id
        r = self.session.get(url)
        return r.text

    def get_title_and_problem_list(self):
        url = 'http://acm.hdu.edu.cn/contests/contest_show.php?cid=%d' % \
              self.contest_id
        r = self.session.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        title = soup.findChild('h1').text
        if '- Team' in title:  # For unification, replace "- Team X" with "X"
            word = title.split(' ')
            title = ' '.join(word[:-3]) + ' ' + word[-1]
        print(title)
        table = soup.findChild('table')
        name_list = []
        for row in table.findChildren('tr'):
            name_list.append(row.findChildren('td')[-2].text)
        return title, name_list[1:]


def parse(contest_id, file_name):
    run = HduModule(contest_id)
    run.login('team080', '******')
    f = open('board_html/%s.html' % file_name, 'w')
    board = run.get_scoreboard()
    f.write(board.encode('utf-8'))
    f.close()
    title, problem_list = run.get_title_and_problem_list()
    print_scoreboard(contest_id, title, file_name, problem_name=problem_list)
