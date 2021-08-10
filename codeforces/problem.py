import requests
import json
from time import sleep
from util.login import login


if __name__ == '__main__':
    session = login()
    r = requests.get('http://codeforces.com/api/problemset.problems')
    result = json.loads(r.text)['result']['problems']
    print(len(result))
    for problem in result:
        print(problem)
        data = {
            'contest': problem['contestId'],
            'index': problem['index'],
            'name': problem['name'],
            'type': problem['type'],
        }
        if 'rating' in problem:
            data['rating'] = problem['rating']
        if 'points' in problem:
            data['points'] = int(float(problem['points']))
        r = session.post(f'http://127.0.0.1:8000/codeforces/problem/', data=data)
        print(r.text)

        r = session.get(f'http://127.0.0.1:8000/codeforces/problem/get_problem/',
                        params={'contest': problem['contestId'], 'index': problem['index']})
        pk = r.json()[0]['id']
        r = session.patch(f'http://127.0.0.1:8000/codeforces/problem/{pk}/', data=data)
        print(r.text)
        sleep(0.5)
