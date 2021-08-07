from bs4 import BeautifulSoup


if __name__ == '__main__':
    # scores = {
    #     'A': 250,
    #     'B': 550,
    #     'C': 950,
    #     'D': 250,
    #     'E': 500,
    #     'F': 1000,
    #     'G': 250,
    #     'H': 600,
    #     'I': 1000,
    #     'J': 250,
    #     'K': 500,
    #     'L': 1000,
    #     'M': 250,
    #     'N': 600,
    #     'O': 900,
    #     'P': 300,
    #     'Q': 500,
    #     'R': 1000,
    #     'S': 250,
    #     'T': 500,
    #     'U': 1000,
    #     'V': 1000,
    #     'W': 1000,
    #     'X': 1000,
    #     'Y': 250,
    # }

    scores = {
        'A': 1000,
        'B': 500,
        'C': 1000,
        'D': 1000,
    }

    with open('board.html', 'r', encoding='utf-8') as fpin:
        soup = BeautifulSoup(fpin, parser='html.parser')
    team_score = dict()
    for row in soup.tbody.find_all('tr'):
        columns = row.find_all('td')
        team_name = columns[1].div.a.span.string
        print(team_name)
        columns = columns[4:]
        score = 0
        for i in range(len(columns)):
            tag = columns[i]['class']
            if 'prob' in tag and 'accepted' in tag:
                score += scores[chr(i + ord('A'))]
        team_score[team_name] = score
    print(team_score)
