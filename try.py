''' from logging import exception


try:
    num=int(input("请输入一个整数:"))
    print("-" *50)
    print(8/num)

except ValueError:
    print("请输入正确的整数：")

except Exception as result:
    print("未知错误%s" %result)


else:
    print("尝试成功")

finally:
    print("测试结束，无论是否有错") '''


''' def demo1():
    return int(input("输入整数:"))

def demo2():
    return demo1()
try :
    print(demo2())
except Exception as result:
    print("未知错误 %s " % result) '''

def password1():
    password=input("请输入密码: ")
    if len(password)>=8:
        return password
    print("主动抛出异常")
    #使用Exception创建异常对象
    ex=Exception("密码长度不够")
    #主动抛出异常
    raise ex
try:
    print(password1())
except Exception as result:
    print(result)