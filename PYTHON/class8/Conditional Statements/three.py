num=22
if num%2==0:
    print("yes even it is number")
else:
    print("no it is odd number")



a=20
b=30
c=50
if a>=b and a>=c:
    print("a is largest")
elif b>=a and b>=c:
    print("b is largest")
else:
    print("c is largest")


marks=int(input("enter marks:"))
if marks>=90:
    print("A grade")
elif marks>=80:
    print("B grade")
elif marks>=70:
    print("c grade")
elif marks>=60:
    print("D grade")
else:
    print("fail")


year=int(input("enter year:"))
if year % 400==0:
    print("leap year")
elif year % 100==0:
    print("not a leap year")
elif year % 4==0:
    print("leap year")
else:
    print("not a leap year")