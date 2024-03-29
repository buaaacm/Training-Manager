import requests
import json
from time import sleep
from util.login import login


if __name__ == '__main__':
    session = login()
    users = members = [
        { 'name': "刘其帅", 'major': "" },
        { 'name': "焦航", 'major': "" },
        { 'name': "李子星", 'major': "" },
        { 'name': "刘永罡", 'major': "" },
        { 'name': "常达", 'major': "" },
        { 'name': "逄望舒", 'major': "" },
        { 'name': "赵洋磊", 'major': "" },
        { 'name': "李宇杰", 'major': "" },
        { 'name': "徐俣", 'major': "" },
        { 'name': "宋恒", 'major': "" },
        { 'name': "赖景愚", 'major': "" },
        { 'name': "李论", 'major': "" },
        { 'name': "王珂龙", 'major': "" },
        { 'name': "方志文", 'major': "" },
        { 'name': "谢舒翼", 'major': "" },
        { 'name': "郭浩泉", 'major': "" },
        { 'name': "任斐", 'major': "" },
        { 'name': "盛斌", 'major': "" },
        { 'name': "张嘉琳", 'major': "" },
        { 'name': "乔衎", 'major': "" },
        { 'name': "邹佳辰", 'major': "" },
        { 'name': "邓梁栋", 'major': "" },
        { 'name': "王冉", 'major': "" },
        { 'name': "孙睿", 'major': "" },
        { 'name': "崔超", 'major': "" },
        { 'name': "郭信谊", 'major': "" },
        { 'name': "刘建云", 'major': "" },
        { 'name': "关育新", 'major': "" },
        { 'name': "闫晟东", 'major': "" },
        { 'name': "洪婉玲", 'major': "" },
        { 'name': "王跃", 'major': "" },
        { 'name': "陈嘉晖", 'major': "" },
        { 'name': "谢科", 'major': "" },
        { 'name': "管清文", 'major': "" },
        { 'name': "杨晓", 'major': "" },
        { 'name': "叶博", 'major': "" },
        { 'name': "李明康", 'major': "" },
        { 'name': "曾立", 'major': "" },
        { 'name': "杨博洋", 'major': "" },
        { 'name': "郭子晨", 'major': "" },
        { 'name': "王晓宇", 'major': "" },
        { 'name': "倪亦帅", 'major': "" },
        { 'name': "柳奇涛", 'major': "" },
        { 'name': "于野", 'major': "" },
        { 'name': "阎骥洲", 'major': "" },
        { 'name': "吴昊天", 'major': "" },
        { 'name': "章烨钦", 'major': "" },
        { 'name': "邓宣颖", 'major': "" },
        { 'name': "高维", 'major': "" },
        { 'name': "刘维同", 'major': "" },
        { 'name': "孙萌", 'major': "" },
        { 'name': "简讯", 'major': "" },
        { 'name': "彭龙", 'major': "" },
        { 'name': "董适", 'major': "" },
        { 'name': "肖文聪", 'major': "" },
        { 'name': "王安然", 'major': "" },
        { 'name': "刘思学", 'major': "" },
        { 'name': "卢超", 'major': "" },
        { 'name': "朱耿良", 'major': "" },
        { 'name': "李鑫慧", 'major': "" },
        { 'name': "鲁海浩", 'major': "" },
        { 'name': "姜睿昶", 'major': "" },
        { 'name': "谭传奇", 'major': "" },
        { 'name': "栾贝迪", 'major': "" },
        { 'name': "夏正林", 'major': "" },
        { 'name': "袁政", 'major': "" },
        { 'name': "黎健成", 'major': "" },
        { 'name': "杨思宇", 'major': "" },
        { 'name': "周帅", 'major': "" },
        { 'name': "李业树", 'major': "" },
        { 'name': "余铠", 'major': "" },
        { 'name': "陈志兴", 'major': "" },
        { 'name': "王剑锋", 'major': "" },
        { 'name': "李森栋", 'major': "" },
        { 'name': "？", 'major': "" },
        { 'name': "刘毅博", 'major': "" },
        { 'name': "李珎", 'major': "" },
        { 'name': "梁明阳", 'major': "" },
        { 'name': "徐少峰", 'major': "" },
        { 'name': "赵轩昂", 'major': "" },
        { 'name': "李炎", 'major': "" },
        { 'name': "王昌宝", 'major': "" },
        { 'name': "李明星", 'major': "" },
        { 'name': "孟春雷", 'major': "" },
        { 'name': "董宣毅", 'major': "" },
        { 'name': "金胜莺", 'major': "" },
        { 'name': "赵海宇", 'major': "" },
        { 'name': "赵东方", 'major': "" },
        { 'name': "李周洋", 'major': "" },
        { 'name': "李睿霖", 'major': "" },
        { 'name': "刘垚鹏", 'major': "" },
        { 'name': "骈扬", 'major': "" },
        { 'name': "董舒印", 'major': "" },
        { 'name': "付成真", 'major': "" },
        { 'name': "朱峰达", 'major': "" },
        { 'name': "林泉沛", 'major': "" },
        { 'name': "李沛伦", 'major': "" },
        { 'name': "张沛", 'major': "" },
        { 'name': "唐靖哲", 'major': "" },
        { 'name': "邓博洋", 'major': "" },
        { 'name': "田茂清", 'major': "" },
        { 'name': "张奥", 'major': "" },
        { 'name': "刘保证", 'major': "" },
        { 'name': "何玥", 'major': "" },
        { 'name': "冯炜韬", 'major': "" },
        { 'name': "杨子琛", 'major': "" },
        { 'name': "黄鑫", 'major': "" },
        { 'name': "李奕君", 'major': "" },
        { 'name': "史雨轩", 'major': "" },
        { 'name': "李晨豪", 'major': "" },
        { 'name': "户建坤", 'major': "" },
        { 'name': "史烨轩", 'major': "" },
        { 'name': "林子义", 'major': "" },
        { 'name': "黄宏鸣", 'major': "" },
        { 'name': "李搏", 'major': "" },
        { 'name': "刘子渊", 'major': "" },
        { 'name': "钟金成", 'major': "" },
        { 'name': "胡智昊", 'major': "" },
        { 'name': "蒋泳波", 'major': "" },
        { 'name': "高威", 'major': "" },
        { 'name': "朱福", 'major': "" },
        { 'name': "张乾宇", 'major': "" },
        { 'name': "张明远", 'major': "" },
        { 'name': "贺牧天", 'major': "" },
        { 'name': "金代圣", 'major': "" },
        { 'name': "朱瑾", 'major': "" },
        { 'name': "谢瑶瑶", 'major': "" },
        { 'name': "李何贝子", 'major': "" },
        { 'name': "王柏润", 'major': "" },
        { 'name': "伍俊洁", 'major': "" },
        { 'name': "钟梓皓", 'major': "" },
        { 'name': "邓一兴", 'major': "" },
        { 'name': "黄浩东", 'major': "" },
        { 'name': "张少昂", 'major': "" },
        { 'name': "姜圣虎", 'major': "" },
        { 'name': "沈中海", 'major': "" },
        { 'name': "杜昊", 'major': "" },
        { 'name': "赵立晨", 'major': "" },
        { 'name': "王嘉翼", 'major': "" },
        { 'name': "周环宇", 'major': "" },
        { 'name': "何铭睿", 'major': "" },
        { 'name': "向宏毅", 'major': "" },
        { 'name': "郭镕昊", 'major': "" },
        { 'name': "王意如", 'major': "" },
        { 'name': "彭毛小民", 'major': "" },
        { 'name': "张凯杰", 'major': "" },
        { 'name': "郑耀彦", 'major': "" },
        { 'name': "肖思炀", 'major': "" },
        { 'name': "丁元杰", 'major': "" },
        { 'name': "廖纪童", 'major': "" },
        { 'name': "杨开元", 'major': "" },
        { 'name': "林昱同", 'major': "" },
        { 'name': "陈铭煊", 'major': "" },
        { 'name': "龙鹏宇", 'major': "" },
        { 'name': "阙子烝", 'major': "" },
        { 'name': "孙保成", 'major': "" },
        { 'name': "邹增禹", 'major': "" },
        { 'name': "王廉杰", 'major': "" },
        { 'name': "牟钰", 'major': "" },
        { 'name': "冯玮琪", 'major': "" },
        { 'name': "马广林", 'major': "" },
        { 'name': "李元恺", 'major': "" },
        { 'name': "袁熙", 'major': "" },
        { 'name': "姜维翰", 'major': "" },
        { 'name': "康时嘉", 'major': "" },
        { 'name': "田柯宇", 'major': "" },
        { 'name': "周海涛", 'major': "" },
        { 'name': "赵婉如", 'major': "" },
        { 'name': "黄云依", 'major': "" },
        { 'name': "常荣熇", 'major': "" },
    ]
    for user in users:
        data = {
            'name': user['name']
        }
        print(data)
        r = session.post('http://127.0.0.1:8000/participant/', data=data)
        print(r.json())
