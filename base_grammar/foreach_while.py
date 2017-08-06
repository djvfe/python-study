i=5
while True :
    print(i)
    break

i=0
sumi = 0
while i<100 : 
    sumi = sumi+i
    i=i+1
    print(i)
print('sum:',sumi)#python中缩进很重要，如果这行缩进和上一行一样就将在循环while中

i=20
while True :
    a = int(input('please input a num'))#类型转换
    if a>i :
        print('higher')
    elif a==i :
        print('恭喜你猜对了')
        break
    else :
        print('lower')
