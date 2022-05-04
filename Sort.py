''' li=[31,41,534,51,3,13,41,55]
li2=[1,2,3,4,5,7,7,6,8]
def bubble_sort(li):
    for i in range(len(li)-1):
        exchange=False
        for j in range(len(li)-1-i):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
                exchange=True
        print(li)
        if not exchange:
            return 

print(li2)
bubble_sort(li2)

li=[31,41,534,51,3,13,41,55]
def select_sort1(li):
    new_li=[]
    for i in range (len(li)):
        min_val=min(li)
        new_li.append(min_val)
        li.remove(min_val)
    return new_li
print(select_sort1(li))

li=[31,41,534,51,3,13,41,55]
def select_sort2(li):
    print(li)
    for i in range (len(li)-1):
        for j in range(i+1,len(li)):
            if li[j]<li[i]:
                li[i],li[j]=li[j],li[i]
    return li
print(select_sort2(li)) '''

li=[31,41,534,51,3,13,41,55]
def insert_sort(li):
    for i in range(1,len(li)):
        tem=li[i]
        j=i-1
        while tem<li[j] and j>=0:
            li[j+1]=li[j]
            j-=1
        li[j+1]=tem
    return li

print(insert_sort(li))