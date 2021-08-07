import requests
import bs4


def login():
    s = requests.Session()
    r = s.get('http://127.0.0.1:8000/api-auth/login/')
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    csrfmiddlewaretoken = soup.find(type='hidden')['value']
    data = {
        'username': 'zzh',
        'password': '642524Zzh!',
        'csrfmiddlewaretoken': csrfmiddlewaretoken,
    }
    r = s.post('http://127.0.0.1:8000/api-auth/login/', data=data)
    s.headers['X-CSRFTOKEN'] = s.cookies.get('csrftoken')
    return s


if __name__ == '__main__':
    login()
