import requests
from datetime import datetime
import random
import hashlib
from config.config import *


def rand():
    ch = random.randint(0, 61)
    if ch < 26:
        return chr(ch + ord('a'))
    if ch < 52:
        return chr(ch - 26 + ord('A'))
    return chr(ch - 52 + ord('0'))


def get(url, params):
    rand_str = ''.join([rand() for _ in range(6)])
    params['apiKey'] = f'{CF_APIKEY}'
    params['time'] = int(datetime.now().timestamp())
    param = sorted(params.items())
    param = '&'.join([f'{p[0]}={p[1]}' for p in param])
    method = url.split('/')[-1]
    secret_str = f'{rand_str}/{method}?{param}#{CF_SECRET}'
    print(secret_str)
    sha = hashlib.sha512(secret_str.encode('utf-8')).hexdigest()
    params['apiSig'] = rand_str + sha
    print(params)
    session = requests.Session()
    r = session.get(url, params=params)
    return session, r.json()

