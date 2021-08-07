import json
from util.login import login


if __name__ == '__main__':
    session = login()
    with open('contest.json', 'r') as fpin:
        contests = json.load(fpin)['2019']
        for key, value in contests.items():
            obj = {
                'title': value['title'],
                'date': value['date'],
                'num': value['num'],
                'statuses': value['statuses'],
                'ranklist': value['ranklist'],
            }
            if 'time' in value:
                obj['time'] = value['time']
            print(obj)
            data = {
                'start_time': obj['date'] + ' 12:00:00',
                'duration_time_second': '5:00:00',
                'type': 'onsite',
                'board': json.dumps(obj),
            }
            print(data)
            r = session.post('http://127.0.0.1:8000/training/contest/', data=data)
            print(r.text)
