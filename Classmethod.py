''' from unicodedata import name


class tool:
    count=0
    def __init__(self,name) -> None:
        self.name=name
        tool.count+=1
    @classmethod
    def  show_tool_count(cls):
        print("工具对象的数量%d " % cls.count)

tool1=tool("斧头")
tool1.show_tool_count()
tool2=tool("榔头")
tool.show_tool_count()
tool2.show_tool_count()


class dog:
    @staticmethod
    def run():
        print("小狗要跑")
dog.run()
 '''

class game():
    top_score=0
    def __init__(self,name,score):
        self.name=name
        self.score=score
        if score>game.top_score:
            game.top_score=score
    @staticmethod
    def show_help():
        print("需要什么样的帮助")
    @classmethod
    def show_top_score(cls):
        print("当前历史最高分为%d" %cls.top_score)
    def start_game(self):
        print("%s开始游戏了..." % self.name)
    def show_result(self):
        print("%s的分数是%d" %(self.name,self.score))

game.show_help()
game.show_top_score()
xiaoming=game("小明",99)
xiaoming.start_game()
xiaoming.show_result()

xiaowang=game("小王",50)
xiaowang.start_game()
xiaowang.show_result()
game.show_top_score()