import json
emp_str='''
[
    {"eid":101,"ename":"rg","avail":true},
    {"eid":102,"ename":"lali","avail":true},
    {"eid":103,"ename":"nithi","avail":false}
]
'''
emp=json.loads(emp_str)
print(emp)