# Filename : var.py

#整数
i = 5
print(i)
i = i + 1
print(i)

#浮点数
i = 1.1
print(i)

#python的弱语言特性，可以随时改变变量的类型
i = 'change i to a string '
print(i)


s = 'hello'#单引号
print(s)
s = "hello"#双引号
print(s)

#三引号为多行字符串
s = '''This is a "multi-line" string.
This is the second line.'''
print(s)

s = '\''#斜杠用于转义
print(s)
#r或R开头的字符串表示自然字符串，后面的斜杠不转义
s = r'\n'
print(s)

s = '这是一个行\
连接符的例子'
print(s)

#斜杠在这里是行连接符，可以把一行中太长的代码分为多行不影响实际意义
#强烈建议坚持在每个物理行只写一句逻辑行。仅仅当逻辑行太长的时候，在多于一个物理行写一个逻辑行
#有一种暗示的假设，可以使你不需要使用反斜杠。这种情况出现在逻辑行中使用了圆括号、方括号或波形括号的时候。这被称为暗示的行连接
i = \
55
print(i)

#同一层次的语句必须有相同的缩进。每一组这样的语句称为一个块,错误的缩进会引发错误
print('value is',i)
print('value is',i)
