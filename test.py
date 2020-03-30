#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import json

def get_token(file):
    json_str = json.dumps(file)
    data = json.loads(json_str)
    result = [(item.get('userToken', 'NA')) for item in data['userList']]
    print(result)
    return str(result)


    
file = {
    "lastRequestTimestamp": 1585193289149,
    "userList": [
        {
            "avatar": "https://images2.bestjlb.com/jlbapp/5e09875981b2214e548f2eb09aac0e48/2020/03/v2jlbossdc065bfb255d75a55c5ffaa2e77cb098(1080x1080).jpeg",
            "nick": "15168310004jiaz",
            "userToken": "FDni4CiqgDoUS+cQeCcAnw==",
            "friendTag": 0,
            "userTags": 0,
            "status": 0
        },
        {
            "groupId": 33583,
            "remarkName": "19988880001九抖",
            "avatar": "https://images2.bestjlb.com/jlbapp/5e09875981b2214e548f2eb09aac0e48/2020/01/v2jlboss7dccadf7570c54f1c57a3ec965477443(720x720).jpeg",
            "nick": "19988880001",
            "userToken": "iiq+Ajk7gKbO/RkgTCjF+A==",
            "friendTag": 0,
            "userTags": 1,
            "status": 1
        },
        {
            "groupId": 33583,
            "avatar": "https://media.bestjlb.com/20180410162336.png",
            "nick": "19977770004改名",
            "userToken": "bFgMZgbiciAPvwvs5L2dTA==",
            "friendTag": 0,
            "userTags": 1,
            "status": 1
        }
    ],
    "groupList": [
        {
            "isDefault": 1,
            "groupId": 33583,
            "name": "好友",
            "id": 33583,
            "isDel": 0,
            "status": 1
        }
    ]
}

get_token(file)

#print("{'receiveUserTokens':"+ get_token(file) + '}')
# json_str = json.dumps(file)
# data = json.loads(json_str)

# new = []
# for user in data['userList']:
#     new.append({
#         user.get('userToken')
#     })
# print (len(new))


