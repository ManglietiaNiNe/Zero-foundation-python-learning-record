#该例子中，列表均使用a、b、c、d、e、f。

#一、修改元素

#1、修改指定索引的元素
letters=['a','b','c','d','e','f']
letters[0]='z'
#列表名[欲修改元素的索引数]='修改后的值'
print(letters)#结果为['z', 'b', 'c', 'd', 'e', 'f']
#由上可见，仅索引为0的元素被修改，其他元素的值和索引数保持不变

#2、添加新元素到列表末尾——append()
letters=['a','b','c','d','e','f']
print(letters[-1])#结果为f
letters.append('g')
#列表名.append('欲添加的值')
print(letters)#结果为['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[-1])#结果为g
#由上可见，append()只会将值添加到列表末端，在之前的元素的值和索引数保持不变

#append()还有一种使用情况是，创建一个空列表，随后依据用户输入欲存储的值，通过向列表中添加元素来保存数据，如下
words=[]
words.append('w')
words.append('t')
words.append('f')
print(words)#结果为['w', 't', 'f']

#3、插入新元素到列表中——insert()
letters=['a','b','c','d','e','f']
print(letters[0],letters[2])#结果为a c，即未插入前第一个元素为a、第三个元素为c
letters.insert(2,'x')
#列表名.insert(期望插入的索引数，'将插入的值')
print(letters)#结果为['a', 'b', 'x', 'c', 'd', 'e', 'f']
print(letters[0],letters[2],letters[3])#结果为a x c，即插入新元素后，第一个元素仍为a，第三个元素变为了x，而c变成了第四个元素
#由上可见，insert()插入新元素到指定索引数后，该索引数前的元素的值和索引数保持不变，该索引数原本的元素及之后的元素，索引数加一（位置右移一位）


#二、删除元素

#1、完全删除指定索引对应的元素——del()
letters=['a','b','c','d','e','f']
del letters[2]
#del 列表名[欲删除元素的索引数]
print(letters)#结果为['a', 'b', 'd', 'e', 'f']
#由上可见，del()可以删除指定索引对应的元素，并且删去后没有办法再次引用该元素

#2、从列表取出指定索引对应的元素——pop()
#当pop()的括号内为空
letters=['a','b','c','d','e','f']
popped_letter=letters.pop()
#新建变量名=列表名.pop()
print(letters)#结果为['a', 'b', 'c', 'd', 'e']
print(popped_letter)#结果为f
#对当pop()的括号内为空的情况，可以这样理解：将列表视为一个栈，pop()为弹出栈顶元素

#当pop()的括号内为指定索引数
letters=['a','b','c','d','e','f']
score=letters.pop(2)
#新建变量名=列表名.pop('欲取出元素的索引数')
print(letters)#结果为c
sentence=f'\"your test score is \'{score.title()}\'\"'#取出的元素因为被赋给了新建变量，所以可以直接使用新建变量，如引用到f字符串中
#相比于直接赋一个值给变量然后使用，这种方法的意义在于，可以通过修改pop语句的取出元素的索引数，来改变新建变量的值，并且保证该值始终出自该列表
print(sentence)#结果为"your test score is 'C'"
#由上可见，当pop()的括号内为空时，默认取出列表末尾的元素，当pop()的括号内为指定索引数时，会取出该指定索引对应的元素。取出后会将该元素赋予一个新建变量，而非直接删除，并且取出后的列表中也不存在取出的元素

#3、从列表取出指定值对应的元素——remove()
letters=['a','b','c','b','d','e','f']#与之前的列表不同，该列表在索引为1和3有两个相同的元素b
letters.remove('b')
#列表名.remove('欲删除的指定值')
print(letters)#结果为['a','c','b','d','e','f'],仅删除了索引为1的b
#由上可见，del()适用于，在不知道欲删除元素的索引数，但是知道该元素的值，可以根据该值删除该元素；当列表中有多个相同值的元素时，仅会删去从头开始（从左）的第一个符合条件的元素，若要删除剩余符合条件的元素，可使用循环完成（第七章）


#ps：一种使用被del()或者remove()删去元素的方法，即在删去前将被删值赋给一个新建变量，在删除后该变量的值不受影响。#
# 感觉这种方法对于del()语句来说，类似写完程序后临时找补，否则直接pop()即可；而对于remove()语句来说，实用性较高，在要取出元素但是不知道该元素的索引时，可以到达和pop()语句类似的效果

letters=['a','b','c','d','e','f']
level=letters[1]
del letters[1]
print(letters)
sentence=f'\"your skill level is \'{level.title()}\'\"'
print(sentence)

letters=['a','b','c','d','e','f']
level='b'
letters.remove('b')
print(letters)
sentence=f'\"your skill level is \'{level.title()}\'\"'
print(sentence)
