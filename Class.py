class Houseitem():
    def __init__(self,name,area) -> None:
        self.name=name
        self.area=area
    def __str__(self) -> str:
        return "%s占地%.2f"%(self.name,self.area)

Bed=Houseitem("席梦思",4)
Chest=Houseitem("衣柜",2)
Table=Houseitem("餐桌",3)

class House():
    def __init__(self,house_type,area) -> None:
        self.house_type=house_type
        self.area=area
        self.free_area=area
        self.itemlist=[]
    def __str__(self) -> str:
        return ("户型：%s\n 总面积: %.2f 剩余:%.2f\n 家具：%s"
         %(self.house_type,self.area,self.free_area,self.itemlist))
    def add_item(self,item):
        print("要添加%s" %item)
        if (item.area>self.free_area):
            print("没有空闲地方了，添加失败")
            return 
        self.free_area-=item.area
        self.itemlist.append(item.name)

my_home=House("两室一厅", 60)
print(my_home)
my_home.add_item(Bed)
print(my_home)
my_home.add_item(Chest)
my_home.add_item(Table)
print(my_home)