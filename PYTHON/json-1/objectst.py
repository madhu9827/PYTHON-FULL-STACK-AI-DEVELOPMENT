import json
emp='{"eid":101,"ename":"madhu"}'
data=json.loads(emp)
print(data)
print(type(data)) 