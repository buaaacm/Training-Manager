from util.login import login
import json
import os
import requests
from datetime import datetime


def crawl():
    session = login()
    r = requests.get('http://codeforces.com/api/contest.list')
    r = json.loads(r.text)
    r = r['result']
    print(r[0])
    for contest in r:
        id = contest['id']
        if id <= 140:
            continue
            params = {
                'contest_id': contest['id'],
                'name': contest['name'],
                'type': contest['type'],
                'start_time': contest['startTimeSeconds'],
                'duration_time_second': contest['durationSeconds'],
                'division': 'Unknown',
                'division_comment': 'Too old.',
            }
            # r = requests.get('http://127.0.0.1:8000/codeforces/update_contest', params=params)
            # print(r.text)
        elif id <= 581:
            continue
            print(id, contest['name'], end=' ')
            path = os.path.join('rating_change', f'{id}.json')
            # if not os.path.isfile(path):
            #     result = requests.get(f'http://codeforces.com/api/contest.ratingChanges?contestId={id}')
            #     with open(path, 'w') as fpout:
            #         fpout.write(result.text)
            params = {
                'contest_id': contest['id'],
                'name': contest['name'],
                'type': contest['type'],
                'start_time': contest['startTimeSeconds'],
                'duration_time_second': contest['durationSeconds'],
            }
            with open(path, 'r') as fpin:
                result = json.load(fpin)
                unrated_message = 'Rating changes are unavailable for this contest'
                if result['status'] == 'FAILED' and unrated_message in result['comment']:
                    params['division'] = 'Unknown'
                    params['division_comment'] = unrated_message + '.'
                else:
                    bound = 1700
                    rating_change = result['result']
                    old_ratings = [change['oldRating'] for change in rating_change]
                    if len(old_ratings) == 0:
                        params['division'] = 'Unknown'
                        params['division_comment'] = 'Technically unrated?'
                    else:
                        params['division_comment'] = 'No comment.'
                        min_rating = min(old_ratings)
                        max_rating = max(old_ratings)
                        if bound - 10 <= max_rating < bound:
                            params['division'] = 'Div. 2'
                        elif max_rating < bound - 10:
                            params['division'] = 'Unknown'
                            params['division_comment'] = 'Unknown error.'
                        elif min_rating < bound:
                            params['division'] = 'Div. 1 + 2'
                        else:
                            params['division'] = 'Div. 1'
            # r = requests.get('http://127.0.0.1:8000/codeforces/update_contest', params=params)
            # print(r.text)
        elif id <= 976:
            continue
            print(id, contest['name'], end=' ')
            path = os.path.join('rating_change', f'{id}.json')
            # if not os.path.isfile(path):
            #     result = requests.get(f'http://codeforces.com/api/contest.ratingChanges?contestId={id}')
            #     with open(path, 'w') as fpout:
            #         fpout.write(result.text)
            params = {
                'contest_id': contest['id'],
                'name': contest['name'],
                'type': contest['type'],
                'start_time': contest['startTimeSeconds'],
                'duration_time_second': contest['durationSeconds'],
            }
            with open(path, 'r') as fpin:
                result = json.load(fpin)
                unrated_message = 'Rating changes are unavailable for this contest'
                if result['status'] == 'FAILED':
                    if unrated_message in result['comment']:
                        params['division'] = 'Unknown'
                        params['division_comment'] = unrated_message + '.'
                    else:
                        params['division'] = 'Unknown'
                        params['division_comment'] = result['comment']
                else:
                    bound = 1900
                    rating_change = result['result']
                    old_ratings = [change['oldRating'] for change in rating_change]
                    if len(old_ratings) == 0:
                        params['division'] = 'Unknown'
                        params['division_comment'] = 'Technically unrated?'
                    else:
                        params['division_comment'] = 'No comment.'
                        min_rating = min(old_ratings)
                        max_rating = max(old_ratings)
                        if bound - 10 <= max_rating < bound:
                            params['division'] = 'Div. 2'
                        elif max_rating < bound - 10:
                            params['division'] = 'Unknown'
                            params['division_comment'] = 'Unknown error.'
                        elif min_rating < bound:
                            params['division'] = 'Div. 1 + 2'
                        else:
                            params['division'] = 'Div. 1'
            r = requests.get('http://127.0.0.1:8000/codeforces/update_contest', params=params)
            print(r.text)
        elif id <= 1351:
            continue
            print(id, contest['name'], end=' ')
            path = os.path.join('rating_change', f'{id}.json')
            # if not os.path.isfile(path):
            #     result = requests.get(f'http://codeforces.com/api/contest.ratingChanges?contestId={id}')
            #     with open(path, 'w') as fpout:
            #         fpout.write(result.text)
            params = {
                'contest_id': contest['id'],
                'name': contest['name'],
                'type': contest['type'],
                'start_time': contest['startTimeSeconds'],
                'duration_time_second': contest['durationSeconds'],
            }
            with open(path, 'r') as fpin:
                result = json.load(fpin)
                unrated_message = 'Rating changes are unavailable for this contest'
                if result['status'] == 'FAILED':
                    if unrated_message in result['comment']:
                        params['division'] = 'Unknown'
                        params['division_comment'] = unrated_message + '.'
                    else:
                        params['division'] = 'Unknown'
                        params['division_comment'] = result['comment']
                else:
                    bound1 = 1900
                    bound2 = 2100
                    bound3 = 1600
                    rating_change = result['result']
                    old_ratings = [change['oldRating'] for change in rating_change]
                    if len(old_ratings) == 0:
                        params['division'] = 'Unknown'
                        params['division_comment'] = 'Technically unrated?'
                    else:
                        params['division_comment'] = 'No comment.'
                        min_rating = min(old_ratings)
                        max_rating = max(old_ratings)
                        if bound1 - 10 <= max_rating < bound1 or bound2 - 10 <= max_rating < bound2:
                            params['division'] = 'Div. 2'
                        elif bound3 - 10 <= max_rating < bound3:
                            params['division'] = 'Div. 3'
                        elif max_rating < bound3 - 10:
                            params['division'] = 'Unknown'
                            params['division_comment'] = 'Unknown error.'
                        elif min_rating < bound3:
                            params['division'] = 'Div. 1 + 2'
                        else:
                            params['division'] = 'Div. 1'
            r = requests.get('http://127.0.0.1:8000/codeforces/update_contest', params=params)
            print(r.text)
        else:
            print(id, contest['name'], end=' ')
            path = os.path.join('../data/codeforces/rating_change', f'{id}.json')
            if not os.path.isfile(path):
                result = requests.get(f'http://codeforces.com/api/contest.ratingChanges?contestId={id}')
                with open(path, 'w') as fpout:
                    fpout.write(result.text)
            params = {
                'id': contest['id'],
                'name': contest['name'],
                'type': contest['type'],
                'start_time': datetime.fromtimestamp(contest['startTimeSeconds']).strftime('%Y-%m-%dT%H:%M:%S+08:00'),
                'duration_time_second': contest['durationSeconds'],
            }
            with open(path, 'r') as fpin:
                result = json.load(fpin)
                unrated_message = 'Rating changes are unavailable for this contest'
                if result['status'] == 'FAILED':
                    if unrated_message in result['comment']:
                        params['division'] = 'Unknown'
                        params['division_comment'] = unrated_message + '.'
                    else:
                        params['division'] = 'Unknown'
                        params['division_comment'] = result['comment']
                else:
                    bound1 = 1900
                    bound2 = 2100
                    bound3 = 1600
                    bound4 = 1400
                    rating_change = result['result']
                    old_ratings = [change['oldRating'] for change in rating_change]
                    if len(old_ratings) == 0:
                        params['division'] = 'Unknown'
                        params['division_comment'] = 'Technically unrated?'
                    else:
                        params['division_comment'] = 'No comment.'
                        min_rating = min(old_ratings)
                        max_rating = max(old_ratings)
                        if bound1 - 10 <= max_rating < bound1 or bound2 - 10 <= max_rating < bound2:
                            params['division'] = 'Div. 2'
                        elif bound3 - 10 <= max_rating < bound3:
                            params['division'] = 'Div. 3'
                        elif bound4 - 10 <= max_rating < bound4:
                            params['division'] = 'Div. 4'
                        elif max_rating < bound4 - 10:
                            params['division'] = 'Unknown'
                            params['division_comment'] = 'Unknown error.'
                        elif min_rating < bound4:
                            params['division'] = 'Div. 1 + 2'
                        else:
                            params['division'] = 'Div. 1'
            print(params)
            r = session.post('http://127.0.0.1:8000/codeforces/contest/', data=params)
            print(r.text)


if __name__ == '__main__':
    crawl()
