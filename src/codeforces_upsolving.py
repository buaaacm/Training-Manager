from login import login
from datetime import datetime
from util.cf_token import get

counter = {}
added = set()
session1 = login()
total_updated = 0

user_id_codeforces = {
    '2sozx': 153,
    'Bazoka13': 153,
    'JJLeo': 153,
    '5095187020216': 154,
    'Hany01': 154,
    'one1one1': 154,
    'seeeagull': 155,
    'Saisyc': 155,
    'PurpleWonder': 155,
    '200815147': 156,
    'CalvinJin': 156,
    'Serval': 156,
    'jxm2001': 157,
    'lgwza': 157,
    'xrbxbn': 157,
    'iuiou': 158,
    'QuantumBolt': 158,
    'wangxiaoge': 158,
    'Eriri_Sawamura': 159,
    'shakugan_no_shanatan_': 159,
    'Atlantis592': 159,
    'HKvv': 160,
    'qwertyczx': 160,
    'godel_bach': 160,
    'lvmaomao': 161,
    '_Shinobu': 161,
    'fallqs': 161,
    'YUKI_LELOUCH': 162,
    'wzy2001wzy': 162,
    'FarmerThy': 162,
    'Potassium_': 163,
    'qxforever': 163,
    'tyakennikku': 163,
    'L_RUA': 164,
    'aspirine': 164,
    'MisakaTao': 164,
    'BH18376359': 165,
    'buttersky': 165,
    'start_': 165,
    'infinity0': 166,
    'LaiAng8086': 166,
    'cacu': 166,
    'rancy': 167,
    'fixed_lxy': 167,
    'ANJHZ': 167,
    'Devil_G': 168,
    'withinlover': 168,
    'Hanabi2333': 168,
    'pantw': 168,
    'zekrom_dream': 169,
    'Zinn': 169,
    'gaoxiangyi': 169,
    'JeryDeak': 170,
    'zhn_666__': 170,
    'DovahkiinGA': 170,
    'Phinney': 171,
    'Appleuiy': 171,
    'fks20011206': 172,
    'cxccxc': 172,
    'quanshr': 172
}

contest_problem_id = {
    337661: 672,
    338475: 704,
    339356: 738,
}


def get_status(contest_id, problem_num):
    session, submissions = get('http://codeforces.com/api/contest.status', params={
        'contestId': contest_id,
        'from': 1,
        # 'count': 100,
    })
    submissions = submissions['result']
    team_solved = dict()
    for submission in submissions:
        if submission['verdict'] != 'OK':
            continue
        # print(submission)
        submit_time = datetime.fromtimestamp(submission['creationTimeSeconds'])
        members = submission['author']['members']
        for member in members:
            handle = member['handle']
            if handle not in user_id_codeforces:
                print(f'{handle} not found')
        team_id = [user_id_codeforces.get(member['handle'], '') for member in members]
        for tid in team_id:
            if tid != team_id[0]:
                raise RuntimeError('Cheating?')
        team_id = team_id[0]
        if not team_id:
            continue
        submit_time = submit_time.strftime('%Y-%m-%dT%H:%M:%S+08:00')
        problem_index = ord(submission['problem']['index']) - ord('A')
        problem_id = contest_problem_id[contest_id] + problem_index
        data = {
            'team': team_id,
            'problem': problem_id,
            'submission_time': submit_time,
        }
        # print(data)
        solved = team_solved.setdefault(team_id, [None for i in range(problem_num)])
        if solved[problem_index] is None or solved[problem_index]['submission_time'] > data['submission_time']:
            solved[problem_index] = data
        else:
            print(f"error {submission['userName']}")
        if team_id not in counter:
            counter[team_id] = 0
    for tid, detail in team_solved.items():
        for id in detail:
            if id is not None:
                counter[tid] += 1
                if (id['problem'], id['team']) in added:
                    print(f'{id} has been added')
                    continue
                print(id)
                r = session1.post('http://127.0.0.1:8000/training/upsolving_submission/', data=id)
                print(r.text)
                print(r.status_code)
                global total_updated
                total_updated += 1
    return team_solved


if __name__ == '__main__':
    r = session1.get('http://127.0.0.1:8000/training/upsolving_submission/')
    result = r.json()
    for sub in result:
        added.add((sub['problem'], sub['team']))
    contest_list = [337661, 338475, 339356]

    for contest_id in contest_list:
        print("### {0}".format(contest_id))
        print(get_status(contest_id, 100))
    print(counter)
    print(f'{total_updated} added this time')
