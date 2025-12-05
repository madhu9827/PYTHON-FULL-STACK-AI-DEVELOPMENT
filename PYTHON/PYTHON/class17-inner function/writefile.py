# read data.txt and write data into new file
fp=open('one.txt','r')
fp1=open('wish.txt','w')
data=fp.read()
fp1.write(data)
print("new file created")

fp.close()
fp1.close()