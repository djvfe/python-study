goods_list = ['鞋子','洗衣粉','书包','电饭煲','沐浴露']

print(goods_list)
print(len(goods_list))#len求长度，对string也可以这么用

goods_list.append('笔记本')#列表可以append添加元素
print(goods_list)
goods_list.sort()
print(goods_list)

goods_list=goods_list+['电风扇']#列表也可以用加好直接拼接
print(goods_list)

print(goods_list[1:2])#列表也可以像字符一样切片

goods_list_xiezi = ['拖鞋','凉鞋','篮球鞋']
g=[goods_list,goods_list_xiezi]
print(g)
print('----------------------------')
#遍历列表
for i in range(0,len(goods_list_xiezi)) :
    print(goods_list_xiezi[i])
print('----------------------------')
#遍历列表的另一种方法，可以得到下标和元素
for i,v in enumerate(goods_list_xiezi) :
    print(i)
    print(v)
print('----------------------------')
#同时循环两个或更多的序列，可以使用 zip() 整体打包，如果两个列表不一样长，只能遍历到短的那个结算为止
for q,a in zip(goods_list,goods_list_xiezi) :
    print(q,a)
print('----------------------------')
