fp1=open('abc.txt','r')
fp2=open('data.txt','w')

print(fp2.readable())  #true
print(fp2.writable())  #false
print(fp2.name)   #abc.txt
print(fp2.mode)   #r
print(fp2.closed) #false