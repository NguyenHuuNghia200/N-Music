nums=[2,7,11,15]
target=9
rtype=[]
x= nums
print(type(x))
for i in x:
    if target-i >= 0:
        if rtype.count(target - i) == 0:
            rtype.append(nums.index(i))
        if rtype.count(target-i)==0:
            rtype.append(nums.index(target-i))


print(rtype)