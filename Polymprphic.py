
from unicodedata import name


class dog:
    def __init__(self,name) -> None:
        self.name=name
    def game(self):
        print("%s蹦蹦跳跳的玩耍" % self.name)
class Xiaotianquan(dog):
    def __init__(self, name) -> None:
        self.name=name

    def game(self):
        print("%s飞到天上去玩耍"% self.name)

class Person:
    def __init__(self,name) -> None:
        self.name=name
    
    def game_with_dog(self,dog):
        print("%s和%s 玩游戏" % (self.name,dog.name))
        dog.game()

wangcai=dog("旺财")
xiaoming=Person("小明")
xiaoming.game_with_dog(wangcai)


laifu=Xiaotianquan("飞天来福")
xiaoming.game_with_dog(laifu)