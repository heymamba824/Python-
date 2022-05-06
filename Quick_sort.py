def quick(li,left,right):
    tem=li[left]
    while left<right:
        while li[right]>=tem and left<right:
            right-=1
        li[left]=li[right]
        while li[left]<=tem and left<right:
            left+=1
        li[right]=li[left]
    li[left]=tem
    return left

li=[5,7,4,6,3,1,2,9,8,7]
quick(li,0,8)
print(li)

def quick_sort(li,left,right):
    if left<right:
        mid=quick(li,left,right)
        quick_sort(li,left,mid-1)
        quick_sort(li,mid+1,right)
    return li


print(quick_sort(li,0,9))