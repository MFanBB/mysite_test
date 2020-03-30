import json

json_str = {"name":"lisi","age":27}
# json解析并按key排序
json_str = json.dumps(json_str)
# 将 JSON 对象转换为 Python 字典
params_json = json.loads(json_str)

items = params_json.items()
for key, value in items:
    print(str(key) + '=' + str(value))