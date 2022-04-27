def hanuoi(n,a,b,c):
    if n>0:
        hanuoi(n-1,a,c,b)
        print("从%s移动到%s"%(a,c))
        hanuoi(n-1,b,a,c)

hanuoi(4,"A","B","C")