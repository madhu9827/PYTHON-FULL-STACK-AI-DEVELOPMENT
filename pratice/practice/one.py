# nums = [1, 2, 3, 1, 1,3,2,2,3]
# count=0
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if(nums[i]==nums[j]):
#             count+=1
# print(count)
candies=[2, 3, 5, 1, 3]
extra=3
max=max(candies)
cand=[]
for i in candies:
    if(i+extra)>=max:
        cand.append(True)
    else:
        cand.append(False)
print(cand)
di={}
for i in range(len(candies)):
    di[candies[i]] = cand[i]

print(di)
