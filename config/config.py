import yaml


with open('/Users/zhongzihao/BUAAACMWebsite/Training-Manager/config/config.yaml', 'r') as fpin:
    info = yaml.load(fpin, yaml.SafeLoader)
BACKEND_USERNAME = info['BACKEND_USERNAME']
BACKEND_PASSWORD = info['BACKEND_PASSWORD']
CF_APIKEY = info['CF_APIKEY']
CF_SECRET = info['CF_SECRET']
