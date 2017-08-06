t=('a','b','c')#定义元组，和列表类似，但是不可变长
print(t)
n_t = (t,'d')
print(n_t)
print(len(n_t))

age = 22
name = 'Swaroop'
#print语句可以使用跟着%符号的项目元组的字符串。这些字符串具备定制的功能。
#定制让输出满足某种特定的格式。定制可以是%s表示字符串或%d表示整数。元组必须按照相同的顺序来对应这些定制。
print('%s is %d years old' % (name, age))
print('Why is %s playing with that python?' % name)
