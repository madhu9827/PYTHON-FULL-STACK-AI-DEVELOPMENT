enames=["madhu","lali","srinithi"]
for ename in enames:
    print(ename)

#enames=["madhu","lali","srinithi"]
enames={"madhu","lali","srinithi"}
i=0
while i<=len(enames)-1:
    print(enames[i])  #TypeError: 'set' object is not subscriptable
    i=i+1    