import requests
import json
from util.login import login


if __name__ == '__main__':
    session = login()
    regions = {
        "2019": [
            { 'type': 1, 'region': "银川赛区（宁夏理工学院）", 'honor': [[102, 4], [103, 4], [104, 5], [105, 5]] },
            { 'type': 1, 'region': "南京赛区（南京航空航天大学）", 'honor': [[95, 4], [96, 4], [99, 6]] },
            { 'type': 1, 'region': "徐州赛区（中国矿业大学）", 'honor': [[101, 4], [102, 4], [103, 5]] },
            { 'type': 1, 'region': "南昌赛区（江西师范大学）", 'honor': [[97, 4], [96, 5], [98, 5]] },
            { 'type': 1, 'region': "沈阳赛区（东北大学）", 'honor': [[100, 5], [99, 6]] },
            { 'type': 1, 'region': "上海赛区（上海大学）", 'honor': [[95, 4], [97, 4], [98, 5]] },
            { 'type': 1, 'region': "EC-Final（西北工业大学）", 'honor': [[97, 4], [95, 5], [100, 5], [102, 5], [96, 6]] },
            { 'type': 2, 'region': "CCPC秦皇岛赛区（东北大学秦皇岛分校）", 'honor': [[99, 5]] },
            { 'type': 2, 'region': "CCPC哈尔滨赛区（东北林业大学）", 'honor': [[97, 4], [96, 5]] },
            { 'type': 2, 'region': "CCPC厦门赛区（厦门理工学院）", 'honor': [[95, 4], [98, 5], [106, 6]] },
            { 'type': 2, 'region': "CCPC-Final（中国传媒大学）", 'honor': [[95, 5]] },
        ],
        "2018": [
            { 'type': 0, 'region': "波尔图，葡萄牙", 'honor': [[86, -21]] },
            { 'type': 1, 'region': "南京赛区（南京航空航天大学）", 'honor': [[90, 4], [89, 5], [88, 5]] },
            { 'type': 1, 'region': "沈阳赛区（东北大学）", 'honor': [[87, 4], [86, 4]] },
            { 'type': 1, 'region': "徐州赛区（中国矿业大学）", 'honor': [[90, 4], [89, 5], [91, 5]] },
            { 'type': 1, 'region': "青岛赛区（中国石油大学）", 'honor': [[86, 4], [91, 5]] },
            { 'type': 1, 'region': "北京赛区（北京大学）", 'honor': [[92, 5], [93, 6]] },
            { 'type': 1, 'region': "焦作赛区（河南理工大学）", 'honor': [[87, 4], [92, 5], [88, 6], [93, 6]] },
            { 'type': 1, 'region': "EC-Final（西北工业大学）", 'honor': [[87, 4], [86, 4], [89, 4], [90, 4], [92, 5]] },
            { 'type': 2, 'region': "CCPC吉林赛区（北华大学）", 'honor': [[94, 4], [91, 4]] },
            { 'type': 2, 'region': "CCPC秦皇岛赛区（东北大学秦皇岛分校）", 'honor': [[89, 4], [88, 4]] },
            { 'type': 2, 'region': "CCPC桂林赛区（桂林电子科技大学）", 'honor': [[86, 4], [87, 4]] },
            { 'type': 2, 'region': "CCPC-Final（哈尔滨工业大学深圳）", 'honor': [[86, 5], [94, 6]] },
        ],
        "2017": [
            { 'type': 0, 'region': "北京，中国", 'honor': [[74, -14]] },
            { 'type': 1, 'region': "沈阳赛区（东北大学）", 'honor': [[74, 2], [75, 4]] },
            { 'type': 1, 'region': "西安赛区（西北工业大学）", 'honor': [[74, 4], [76, 4], [77, 4]] },
            { 'type': 1, 'region': "青岛赛区（中国石油大学）", 'honor': [[77, 4], [78, 6]] },
            { 'type': 1, 'region': "北京赛区（北京大学）", 'honor': [[79, 5], [80, 5], [81, 6]] },
            { 'type': 1, 'region': "香港赛区（香港科技大学）", 'honor': [[76, 5]] },
            { 'type': 1, 'region': "南宁赛区（广西大学）", 'honor': [[75, 4], [78, 4], [82, 4], [83, 6]] },
            { 'type': 1, 'region': "乌鲁木齐赛区（新疆大学）", 'honor': [[84, 5]] },
            { 'type': 1, 'region': "ECL-Final（上海大学）", 'honor': [[74, 3], [75, 5], [77, 5], [82, 5]] },
            { 'type': 2, 'region': "CCPC哈尔滨赛区（哈尔滨理工大学）", 'honor': [[77, 4], [76, 4]] },
            { 'type': 2, 'region': "CCPC秦皇岛赛区（东北大学秦皇岛分校）", 'honor': [[78, 4], [79, 5], [83, 6]] },
            { 'type': 2, 'region': "CCPC杭州赛区（浙江理工大学）", 'honor': [[74, 4], [75, 5], [82, 5]] },
            { 'type': 2, 'region': "CCPC-Final（哈尔滨工业大学）", 'honor': [[74, 4]] },
        ],
        "2016": [
            { 'type': 0, 'region': "拉皮德城，美国", 'honor': [[65, -56]] },
            { 'type': 1, 'region': "大连赛区（大连海事大学）", 'honor': [[65, 2], [66, 4], [67, 6]] },
            { 'type': 1, 'region': "沈阳赛区（东北大学）", 'honor': [[68, 5], [69, 5], [70, 6]] },
            { 'type': 1, 'region': "香港赛区（香港中文大学）", 'honor': [[71, 6], [85, 7]] },
            { 'type': 1, 'region': "青岛赛区（中国石油大学）", 'honor': [[65, 4], [69, 5], [66, 6]] },
            { 'type': 1, 'region': "北京赛区（北京大学）", 'honor': [[72, 5], [70, 6], [73, 7]] },
            { 'type': 1, 'region': "China-Final（上海大学)", 'honor': [[65, 4], [70, 5], [72, 5], [66, 5]] },
            { 'type': 2, 'region': "CCPC长春赛区（吉林大学）", 'honor': [[65, 4], [66, 6]] },
            { 'type': 2, 'region': "CCPC合肥赛区（安徽大学）", 'honor': [[72, 5], [69, 5]] },
            { 'type': 2, 'region': "CCPC杭州赛区（杭州电子科技大学）", 'honor': [[70, 4], [67, 4], [73, 5]] },
            { 'type': 2, 'region': "CCPC-Final（宁波理工学院）", 'honor': [[65, 5], [66, 5]] },
        ],
        "2015": [
            { 'type': 0, 'region': "普吉，泰国", 'honor': [[59, -14]] },
            { 'type': 1, 'region': "长春赛区（东北师范大学）", 'honor': [[56, 5], [57, 6], [58, 6]] },
            { 'type': 1, 'region': "沈阳赛区（东北大学）", 'honor': [[59, 1], [60, 5]] },
            { 'type': 1, 'region': "合肥赛区（中国科学技术大学）", 'honor': [[56, 5], [61, 5]] },
            { 'type': 1, 'region': "北京赛区（北京大学）", 'honor': [[62, 6], [63, 6]] },
            { 'type': 1, 'region': "上海赛区（华东理工大学）", 'honor': [[63, 5], [64, 5]] },
            { 'type': 1, 'region': "EC-Final（上海大学）", 'honor': [[59, 3], [61, 4], [56, 4], [63, 6]] },
            { 'type': 2, 'region': "CCPC南阳赛区（南阳理工学院）", 'honor': [[59, 2], [60, 5], [62, 5]] },
        ],
        "2014": [
            { 'type': 0, 'region': "马拉喀什，摩洛哥", 'honor': [[50, -28]] },
            { 'type': 1, 'region': "牡丹江赛区（牡丹江师范学院）", 'honor': [[48, 4], [49, 5]] },
            { 'type': 1, 'region': "鞍山赛区（辽宁科技大学）", 'honor': [[50, 3], [51, 5], [52, 6]] },
            { 'type': 1, 'region': "西安赛区（西北工业大学）", 'honor': [[52, 5], [51, 5], [53, 6], [54, 6]] },
            { 'type': 1, 'region': "北京赛区（北京师范大学）", 'honor': [[50, 4], [48, 5], [54, 7]] },
            { 'type': 1, 'region': "广州赛区（华南理工大学）", 'honor': [[49, 5], [55, 6]] },
            { 'type': 1, 'region': "上海赛区（上海大学）", 'honor': [[55, 6], [53, 6]] },
        ],
        "2013": [
            { 'type': 1, 'region': "成都赛区（电子科技大学）", 'honor': [[41, 5], [42, 7]] },
            { 'type': 1, 'region': "杭州赛区（浙江工业大学）", 'honor': [[43, 5], [44, 5]] },
            { 'type': 1, 'region': "南京赛区（南京理工大学）", 'honor': [[45, 4], [44, 5]] },
            { 'type': 1, 'region': "长沙赛区（湖南大学）", 'honor': [[45, 5], [46, 6], [43, 6]] },
            { 'type': 1, 'region': "长春赛区（吉林大学）", 'honor': [[47, 6], [46, 6]] },
        ],
        "2012": [
            { 'type': 0, 'region': "圣彼得堡，俄罗斯", 'honor': [[35, -27]] },
            { 'type': 1, 'region': "长春赛区（东北师范大学）", 'honor': [[35, 5], [36, 6], [37, 6]] },
            { 'type': 1, 'region': "天津赛区（天津理工大学）", 'honor': [[35, 4], [38, 5], [37, 5]] },
            { 'type': 1, 'region': "金华赛区（浙江师范大学）", 'honor': [[39, 5], [40, 6]] },
            { 'type': 1, 'region': "杭州赛区（浙江理工大学）", 'honor': [[38, 6], [36, 6]] },
            { 'type': 1, 'region': "成都赛区（成都东软学院）", 'honor': [[40, 6]] },
        ],
        "2011": [
            { 'type': 1, 'region': "大连赛区（大连理工大学）", 'honor': [[30, 5], [31, 6]] },
            { 'type': 1, 'region': "上海赛区（复旦大学）", 'honor': [[30, 5]] },
            { 'type': 1, 'region': "北京赛区（北京邮电大学）", 'honor': [[32, 6], [33, 6]] },
            { 'type': 1, 'region': "成都赛区（成都东软学院）", 'honor': [[34, 5], [31, 6]] },
            { 'type': 1, 'region': "福州赛区（福建师范大学）", 'honor': [[34, 5]] },
        ],
        "2010": [
            { 'type': 1, 'region': "哈尔滨赛区（哈尔滨工程大学）", 'honor': [[24, 7], [25, 7]] },
            { 'type': 1, 'region': "天津赛区（天津大学）", 'honor': [[26, 5], [27, 5]] },
            { 'type': 1, 'region': "杭州赛区（浙江理工大学）", 'honor': [[25, 6], [27, 7]] },
            { 'type': 1, 'region': "成都赛区（四川大学）", 'honor': [[28, 7], [29, 7]] },
            { 'type': 1, 'region': "福州赛区（福州大学）", 'honor': [[26, 5]] },
        ],
        "2009": [
            { 'type': 1, 'region': "合肥赛区（中国科学技术大学）", 'honor': [[18, 6], [19, 7]] },
            { 'type': 1, 'region': "宁波赛区（浙江大学宁波理工学院）", 'honor': [[20, 6]] },
            { 'type': 1, 'region': "上海赛区（东华大学）", 'honor': [[21, 5], [22, 5]] },
            { 'type': 1, 'region': "武汉赛区（武汉大学）", 'honor': [[18, 5], [23, 6]] },
            { 'type': 1, 'region': "哈尔滨赛区（哈尔滨工业大学）", 'honor': [[21, 5], [19, 6]] },
        ],
        "2008": [
            { 'type': 1, 'region': "哈尔滨赛区（哈尔滨工程大学）", 'honor': [[13, 5]] },
            { 'type': 1, 'region': "北京赛区（北京交通大学）", 'honor': [[14, 6], [15, 6]] },
            { 'type': 1, 'region': "合肥赛区（中国科技大学）", 'honor': [[16, 4], [17, 6]] },
            { 'type': 1, 'region': "杭州赛区（杭州电子科技大学）", 'honor': [[17, 5]] },
            { 'type': 1, 'region': "成都赛区（西南民族大学）", 'honor': [[16, 5]] },
        ],
        "2007": [
            { 'type': 1, 'region': "南京赛区（南京航空航天大学）", 'honor': [[4, 5], [5, 6], [6, 7]] },
            { 'type': 1, 'region': "长春赛区（吉林大学）", 'honor': [[7, 6], [8, 6], [9, 6]] },
            { 'type': 1, 'region': "成都赛区（西华大学）", 'honor': [[10, 5], [11, 5], [12, 5]] },
        ],
        "2006": [
            { 'type': 1, 'region': "北京赛区（清华大学）", 'honor': [[1, 4]] },
            { 'type': 1, 'region': "西安赛区（西安电子科技大学）", 'honor': [[2, 6]] },
            { 'type': 1, 'region': "上海赛区（上海大学）", 'honor': [[3, 7]] },
        ],
        "2005": [
            { 'type': 1, 'region': "北京赛区（北京大学）", 'honor': [[0, 6]] },
        ],
    }
    for year, contests in regions.items():
        for contest in contests:
            region = contest['region']
            contest_type = {
                0: 'World-Finals',
                1: 'ICPC',
                2: 'CCPC'
            }[contest['type']]
            data = {
                'region': region,
                'type': contest_type,
                'year': year
            }
            print(data)
            r = session.post('http://127.0.0.1:8000/contest/', data=data)
            print(json.loads(r.text))
