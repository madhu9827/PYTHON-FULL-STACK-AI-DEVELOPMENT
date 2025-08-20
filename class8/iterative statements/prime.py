n=int(input("enter number:"))   #prime number
if n<=1:
  not Prime
else:
  for i in range(2,n):
    if n%i==0:
      print("not prime")
      break
  else:
    print("prime")