# d=dict.fromkeys("zhuxiang")
# d['z']=99
# d.update({'h':100,'x':1})
# d.update(g=100)
# print(d)
# print(d.get('x',"这里没有x"))
# print(d.get('w',"这里没有w"))
# d.setdefault('w',88)
# print(d)

# key=d.keys()
# values=d.values()
# item=d.items()
# d.pop('z')
# print(key)
# print(values)
# print(item) 
# print('c' in d)
# print(list(reversed(d.values())))
# print(d["w"])
''' dic={"吕布":{"语文":70,"数学":80},"关羽":{"语文":99,"数学":100}}
print(dic["关羽"]['数学'])
dic={"吕布":[1,11,111],"关羽":{"语文":99,"数学":100}}
print(dic['吕布'][1])
d={'F':70, 'i':105,'h':99}
b={y:x for x,y in d.items()}
print(b) '''

#集合
''' s=set("FishC")
s.update([1,1],"23")
s.add(45)
print(s) '''

''' def myfunc(a,*b,**keyword):
    print(a,b,keyword)
myfunc(1,[1,2,],5,x="zhu",y="xiang") '''

from sunau import Au_read

print("test")
class Gun:
    def __init__(self,model) :
        self.model=model
        self.bullet=0
    def Add_Bullet(self,number):
        self.bullet+=number
    def Shoot(self):
        if self.bullet<=0:
            print("%s没有子弹了"% self.model)
            return
        self.bullet-=1
        print("%s biu biu biu还剩下%d子弹" %(self.model,self.bullet))
aK47=Gun("AK47") 
AK47.Shoot()
AK47.Add_Bullet(100)
AK47.Shoot()
class Solider:
    def __init__(self,name) -> None:
        self.name=name
        self.gun=None
    def Fire(self):
        if self.gun==None:
            print("%s士兵没有枪"%self.name)
            return 
        print("%s冲啊"%self.name)
        self.gun.Add_Bullet(50)
        self.gun.Shoot()
Heymamba=Solider("heymamba")
Heymamba.gun=AK47
Heymamba.Fire()