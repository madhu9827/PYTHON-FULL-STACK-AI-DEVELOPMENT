nums = [3, 6, 9, 12, 15, 18, 21]
new=[]
def  change_case(num):
    return num>10
new=filter(change_case,nums)
print(list(new))