def findDisappearedNumbers(nums):
    n=len(nums)
    l=[0]*(n+1)
    l[0]=1
    for i in nums:
        l[i]+=1
    result=[]
    for i in range(len(l)):
        if l[i]==0:
            result.append(i)
    return result
nums=[1,2,4,3,1,3]
print(findDisappearedNumbers(nums))

    