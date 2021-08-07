from util.login import login
import json


if __name__ == '__main__':
    session = login()
    teams = list(range(153, 173, 1))
    r = session.post('http://127.0.0.1:8000/statistic/update_rating_2021/', data={
        'team[]': teams,
        'begin_time': '2021-07-17T00:00:00+08:00',
        'end_time': '2021-08-14T00:00:00+08:00',
        'least_compete': 3,
    })
    print(r.text)
