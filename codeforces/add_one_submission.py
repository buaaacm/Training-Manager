import json
import requests
from datetime import datetime


def submission(handle, item):
    r = requests.get(f'http://127.0.0.1:8000/codeforces/user/get_user/?handle={handle}')
    user_id = json.loads(r.text)['id']
    print('user id', user_id)

    problem = item['problem']
    author = item['author']
    problem_id = problem['id']
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
    r = requests.post(f'http://127.0.0.1:8000/codeforces/submission/', data=data)
    print(r.text)


if __name__ == '__main__':
    with open('strange_submissions/strange_submission9.json', 'r') as fpin:
        submissions = json.load(fpin)
        for submission_ in submissions:
            submission('lgwza', submission_)
