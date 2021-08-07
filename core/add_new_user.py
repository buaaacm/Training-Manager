import requests
import json
from time import sleep
from util.login import login


if __name__ == '__main__':
    session = login()
    users = session.get('http://127.0.0.1:8000/participant/').json()
    print(users)
    with open('../data/core/handle2021.csv', 'r') as fpin:
        for line in fpin:
            name, sid, email, cf_handle = [item.strip() for item in line.split(',')]
            data = {
                'name': name,
                'student_id': sid,
                'email': email,
                'codeforces': cf_handle,
            }
            user_id = -1
            for user in users:
                if user['email'] == email:
                    user_id = user['id']
                    break
            print(data)
            r = session.patch(f'http://127.0.0.1:8000/participant/{user_id}/', data=data)
            print(r.text)
            print(r.status_code)
