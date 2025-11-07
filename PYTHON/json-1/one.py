import json
emp_str='''
[{"eid":101,"avail":true},
{"eid":102,"avail":false},
{"eid":103,"avail":true}
]
'''
employees=json.loads(emp_str)
print(type(employees))
print(employees[0])
print(employees[1])