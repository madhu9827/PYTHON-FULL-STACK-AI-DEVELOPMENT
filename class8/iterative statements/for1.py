n = int(input("Enter a number: "))  #sum of n natural numbers
total = 0

for i in range(1, n+1):   # this automatically assigns values to i
    total = total + i

print("Sum =", total)

#Multiplication Table
#Input a number and print its multiplication table (1–10).
n=int(input("enter number:"))
for i in range(1,11):
    print(n*i)


