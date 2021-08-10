import json
from datetime import datetime

import requests

from util.login import login


def submission(handle, session):
    r = requests.get(f'http://codeforces.com/api/user.status?handle={handle}')
    result = json.loads(r.text)['result']
    print('sub. number', len(result))
    result = [item for item in result if item.get('contestId', 1000000) < 100000]
    print('filtered sub. number', len(result))
    result.sort(key=lambda p: p['id'])

    r = session.get(f'http://127.0.0.1:8000/codeforces/user/submission_count/?handle={handle}')
    exist_submission = int(r.text)
    print('sub. in database', exist_submission)
    if exist_submission == len(result):
        print('No update, finish')
        return
    start_index = max(0, exist_submission)
    result = result[start_index:]

    r = session.get(f'http://127.0.0.1:8000/codeforces/user/get_user/?handle={handle}')
    user_id = json.loads(r.text)['id']
    print('user id', user_id)

    print('--------- process start ---------')
    for item in result:
        if 'verdict' not in item:
            # probably in queue
            continue
        problem = item['problem']
        author = item['author']
        contest_id = problem.get('contestId')
        index = problem['index']
        name = problem['name']
        r = session.get(f'http://127.0.0.1:8000/codeforces/problem/get_problem/?contest={contest_id}&index={index}')
        problems = json.loads(r.text)
        if len(problems) == 0:
            r = session.get(f'http://127.0.0.1:8000/codeforces/problem/get_problem/?name={name}')
            problems = json.loads(r.text)
            if len(problems) != 1:
                global unsolved
                unsolved.append(item)
                continue
        problem_id = problems[0]['id']
        print(problem_id)
        submission_time = str(datetime.fromtimestamp(item['creationTimeSeconds'])) + '+08:00'

        data = {
            'id': item['id'],
            'user': user_id,
            'problem': problem_id,
            'creation_time': submission_time,
            'participant_type': author['participantType'],
            'ghost': author['ghost'],
            'programming_language': item['programmingLanguage'],
            'verdict': item['verdict'],
            'testset': item['testset'],
            'passed_test_count': item['passedTestCount'],
            'time_consumed_millis': item['timeConsumedMillis'],
            'memory_consumed_bytes': item['memoryConsumedBytes'],
        }
        print(data)
        r = session.post(f'http://127.0.0.1:8000/codeforces/submission/', data=data)
        print(r.text)
        global append_count
        if r.status_code == 201:
            append_count += 1
        elif r.status_code == 400:
            error = json.loads(r.text)
            if isinstance(error['id'], list) and len(error['id']) == 1 and \
                    error['id'][0] == '具有 id 的 submission 已存在。':
                data = {
                    'submission': item['id'],
                    'handle': handle,
                }
                r = session.post(f'http://127.0.0.1:8000/codeforces/submission/add_author/', data=data)
                print(r.text)
                if r.status_code != 200:
                    raise RuntimeError('WTF?')
                append_count += 1


if __name__ == '__main__':
    cf_handles = [
        'Toxel',
        'chielo',
        'Prime21',
        'Max.D.',
        'Hardict',
        'SANJIN',
        'Potassium_',
        'qxforever',
        'tyakennikku',
        'ws_zzyer',
        'Immortal.S',
        's_h_y',
        'TownYang',
        'Kevin00',
        'zhtjtcz',
        'lyuankai',
        'kipple',
        'holmium01',
        'infinity37',
        'Zars19',
        '_wzx27',
        'pantw',
        'Devil_G',
        'withinlover',
        'Random_chen',
        'rising0321',
        'selia',
        'FYH_SSGSS',
        'wxg',
        'Mychael',
        '2sozx',
        'Bazoka13',
        'JJLeo',
        'L_RUA',
        'aspirine',
        'MisakaTao',
        'qgjyf2001',
        'jxm2001',
        'lgwza',
        'Intouchables',
        'iuiou',
        'QuantumBolt',
        'great_designer',
        'kongyoubuaa',
        'BH18376359',
        'dragonylee',
        'cnMember',
        'hujin',
        'NoMansLand',
        'fayy',
        'duancheng',
        'JeryDeak',
        'Dr_nobody',
        'YUKI_LELOUCH',
        'wzy2001wzy',
        'FarmerThy',
        'airbust',
        'Kazamori',
        'Ket98',

        'qx4ever',
        'PotassiumWings',
    ]
    unsolved = list()
    append_count = 0
    session = login()
    for handle in cf_handles:
        try:
            submission(handle, session)
        except:
            pass
    print('append_count =', append_count)
    print('-------------- unsolved submission ------------------')
    print(json.dumps(unsolved))
