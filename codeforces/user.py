import json
import requests
from util.login import login


def basic(handle, session):
    r = requests.get(f'http://codeforces.com/api/user.info?handles={handle}')
    result = json.loads(r.text)['result'][0]
    print(result)
    assert handle == result['handle']
    data = {
        'handle': handle,
        'rating': result.get('rating', 0),
        'max_rating': result.get('maxRating', 0),
    }
    print(data)
    if 'rank' in result:
        data['rank'] = result['rank']
    if 'maxRank' in result:
        data['max_rank'] = result['maxRank']
    print(data)
    r = session.post('http://127.0.0.1:8000/codeforces/user/', data=data)
    print(r.text)
    user_id = session.get('http://127.0.0.1:8000/codeforces/user/get_user/', params={'handle': handle}).json()['id']
    r = session.patch(f'http://127.0.0.1:8000/codeforces/user/{user_id}/', data=data)
    print(r.text)


def compete_history(handle, session):
    r = requests.get(f'http://codeforces.com/api/user.rating?handle={handle}')
    result = r.json()['result']
    if not result:
        return
    print(result)
    user_id = session.get('http://127.0.0.1:8000/codeforces/user/get_user/', params={'handle': handle}).json()['id']
    for item in result:
        data = {
            'user': user_id,
            'contest': item['contestId'],
            'rank': item['rank'],
            'old_rating': item['oldRating'],
            'new_rating': item['newRating'],
        }
        print(data)
        r = session.post('http://127.0.0.1:8000/codeforces/rating/', data=data)
        print(r.text)


if __name__ == '__main__':
    cf_handles = [
        'Hanabi2333',
        '2sozx',
        'JJLeo',
        'Bazoka13',
        '5095187020216',
        'Hany01',
        'one1one1',
        'seeeagull',
        'Saisyc',
        'PurpleWonder',
        '200815147',
        'CalvinJin',
        'Serval',
        'jxm2001',
        'lgwza',
        'xrbxbn',
        'iuiou',
        'QuantumBolt',
        'wangxiaoge',
        'Eriri_Sawamura',
        'shakugan_no_shanatan_',
        'Atlantis592',
        'HKvv',
        'qwertyczx',
        'godel_bach',
        'lvmaomao',
        '_Shinobu',
        'fallqs',
        'FarmerThy',
        'wzy2001wzy',
        'YUKI_LELOUCH',
        'Potassium_',
        'tyakennikku',
        'qxforever',
        'MisakaTao',
        'aspirine',
        'L_RUA',
        'BH18376359',
        'buttersky',
        'start_',
        'infinity0',
        'LaiAng8086',
        'cacu',
        'rancy',
        'fixed_lxy',
        'ANJHZ',
        'pantw',
        'withinlover',
        'Devil_G',
        'zekrom_dream',
        'Zinn',
        'gaoxiangyi',
        'zhn_666__',
        'JeryDeak',
        'DovahkiinGA',
        'fks20011206',
        'cxccxc',
        'quanshr',
        'Phinney',
        'Appleuiy',
    ]
    session = login()
    for handle in cf_handles:
        basic(handle, session)
        # compete_history(handle, session)
