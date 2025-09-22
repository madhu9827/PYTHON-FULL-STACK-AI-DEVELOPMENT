try:
    fp=input("enter the file name:")
    fp1=open("default.txt",'r')
    print(fp1.read())
    fp1.close()
except FileNotFoundError:
    print("file not found")
finally:
    print("file operation finished")