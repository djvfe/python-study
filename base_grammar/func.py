h='hello'
def hello(user) : 
    print('hello,',user)
    print(h,',',user)

hello('jerry')
u='dd'
hello(u)

print('----------------------------------------------')
def hello2(user) :
    global h#函数内定义的全局变量，在函数外可以调用赋值
    print(h,user)

h='hhhhhhhhh'
hello2('jjjjjjj')
print(h)

print('----------------------------------------------')

def say(msg,user='jerry',time=1) :#默认参数值的用法
    for i in range(0,time) :
        print(msg,',',user,i+1)
say('hello')
say('hello','j',10)
say('hello',time=5)#关键参数的用法，time由调用处指定，user使用函数默认定义
