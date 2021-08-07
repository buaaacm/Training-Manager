from util.login import login
import json


if __name__ == '__main__':
    session = login()
    with open('week_report.csv', 'r', encoding='utf-8') as fpin:
        lines = fpin.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].split(',')
    for i in range(1, len(lines[0])):
        data = {line[0]: int(line[i]) for line in lines}
        print(data)
        param = {
        'team_score': json.dumps(data),
        'source': 'week_report',
        'identifier': f'2020_week{i}',
        }
        print(param)
        r = session.post('http://127.0.0.1:8000/score_record/add_score_record/',data=param)
        print(r.text)
