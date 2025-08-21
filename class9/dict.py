emp={ 
    'eid':101,
    'ename':'lalitha',
    'esal':45000,
    'email':"lali@gmail.com",
    'email':"lali123@gmail.com"
    }
print(emp['esal'])
print(emp['ename'])
emp['ename']="srinithi"
print(emp)
emp['avail']=True
print(emp)
del emp['esal']
print(emp)