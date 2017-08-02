# coding=utf-8
import urllib
import urllib2
import cookielib


def parse(contest_id):
    base_url = "http://acm.hdu.edu.cn/contests/client_ranklist.php?cid=%d" % \
             contest_id

    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(
        urllib2.HTTPCookieProcessor(cookie))

    opener.addheaders = [
      ('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'),
      ('Proxy-Connection', 'keep-alive')]
    urllib2.install_opener(opener)

    post_param = {
      'username': 'team080',
      'userpass': '******',
    }

    request = urllib2.Request(base_url, urllib.urlencode(post_param))
    response = opener.open(request)
    print(response.read())
