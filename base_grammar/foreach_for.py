sumi=0
for i in range(1,5) :
    print(i)
    sumi=sumi+i
else :
    print('累加成功',sumi)
    
print('----------------------------')
#range函数的第三个参数为步长，默认为1
for i in (range(1, 10, 2)):
    print(i)
print('----------------------------')
#翻转
for i in reversed(range(1, 10, 2)):
    print(i)
