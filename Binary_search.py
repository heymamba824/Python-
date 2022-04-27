a=[1,123,34,13,41,13,31,1451,5,151,5,1,51,31]
a.sort()
print(a)
t=int(input("请输入你想要查找的数字"))


def binary_search(a,number):
    t=number
    left=0
    right=len(a)-1
    while(left<=right):
        mid=(left+right)//2
        if a[mid]==t:
            return mid
        elif t>a[mid]:
            left=mid+1
        else :
            right=mid-1
    return None

print(binary_search(a,t))