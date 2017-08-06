def get_sum(a,b) :
    return a+b

print(get_sum(3,4))


def get_max(a,b) :
    '''这是文档字符串
    可以使用__doc__获取到'''
    if a>b :
        return a
    else :
        return b
        

print('the max num is ',get_max(100,200))
print(get_max.__doc__)
