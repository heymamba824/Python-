''' class A:
    def __init__(self) -> None:
        self.num1=100
        self.__num2=00
    def __test(self):
            print("私有方法%d %d" %(self.num1,self.__num2))
    def test(self):
        print("父类的公用方法%d" % self.__num2)
        self.__test()

class B(A):
    def demo(self):
        self.test()
b=B()
b.demo()
 '''
from cgi import test


''' class A:
    def test(self):
        print("A的test 方法")
    def demo(self):
        print("A的demo方法")
class B:
    def demo(self):
        print("B的demo方法")
    def test(self):
        print("B的test 方法")
    
class C(A,B):
    pass
#子类优先运行先出现的同名方法
son=C()
son.test()
son.demo() '''


li=[1,2,3]
print(dir(li))