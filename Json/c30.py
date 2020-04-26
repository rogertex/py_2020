import json

# json object=python dictionary , json array=python list

json_str = '[{"name":"qiyue","age":18},{"name":"qiyue","age":18}]'
student = json.loads(json_str)
print(type(student))
print(student)
# print(student['name'])
# print(student['age'])
#反序列化json->python, 序列化 python->json