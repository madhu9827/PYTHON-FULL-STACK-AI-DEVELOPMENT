nums = [10, 20, 30, 40]
try:
    index=int(input("enter the index:"))
    print("enter at index",index,"is",nums[index])
except IndexError:
    print("index is invalid")
finally:
    print("index check finished")

