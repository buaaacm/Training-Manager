from util.login import login


if __name__ == '__main__':
    session = login()
    name, english_name = '', ''
    with open('../data/core/team2021.csv', 'r', encoding='utf-8') as fpin:
        lines = fpin.readlines()

    length = len(lines)
    print(length)
    for i in range(0, length, 3):
        name, english_name, member1 = lines[i].split(',')
        _, _, member2 = lines[i + 1].split(',')
        _, _, member3 = lines[i + 2].split(',')
        data = {
            'name': name,
            'english_name': english_name,
            'year': 2021,
            'member1': member1.strip(),
            'member2': member2.strip(),
            'member3': member3.strip(),
        }
        print(data)
        r = session.post(f'http://127.0.0.1:8000/team/', data=data)
        print(r.text)
        print(r.status_code)
