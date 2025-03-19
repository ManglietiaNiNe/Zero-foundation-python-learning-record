for value in range (1,5):        #rangge(1,5)指从1开始，生成数列到5的前一位结束（直到后一位数5前结束）。
    print (value)                #结果为1，2，3，4，没有5，这是编程语言中常见的差一行为，如果要输出1-5，则为range（1，6）。同样的，假如使用range()结果不理想，可以考虑将指定值+1或-1（玄学是吧，笑死）
                                 #其实因为是for循环，意味着没有必要一定使用value做变量名，但是考虑到教程中都以value做变量名，此处也一并继承，但是实际编程时要根据情况选择变量名

for value in range (6):
    print (value)                #结果是0，1，2，3，4，5，也就是指定一个参数时，默认从0开始到指定数的前一个符合条件的数结束
    
numbers=list(range(2,101,4))     #可以用list()直接生成列表
print(numbers)                   #使用range时还可以指定步长，比如该例就是，从2开始到104前为止，每次加4

squares=[]                       #创建了一个新的空列表
for value in range(1,11):        #用for语句将每一个1到10的数循环赋给value变量
    square=value**2              #将value变量进行平方计算（**）后赋给square变量
    squares.append(square)       #将生成的square变量的值添加到squares的列表末尾
print(squares)                   #在for循环结束后，才会将列表打印出来

squares=[]                       #创建了一个新的空列表
for value in range(1,11):        #用for语句将每一个1到10的数循环赋给value变量
    squares.append(value**2)     #将value变量进行平方计算（**）后将生成的值添加到squares的列表末尾
print(squares)                   #在这个例子里就去掉了临时变量square，直接将计算结果添加到列表中
                                 #首次编写代码时应保证清晰易读以及保证可以实现设想的功能（类似上个例子），而在审核时在考虑更高效的办法，对代码进行优化（如该例子）

digita=[1,5,2,4,2,6,8,6,7,0,9]   #其他几个对数字列表进行统计的函数
min(digita)
max(digita)
sum(digita)



#列表解析可以让原本用几行的代码，仅用一行就能运行，此处做了解或者尝试性练习，初学者编写代码时应先保证自己能够理解，而不是为了用而用
squares=[value**2 for value in range(1,11)]#没有冒号
print (squares)
#列表名=[临时变量的处理过程 for 临时变量 in range(传递参数)]

numbers=[(value//3)**2 for value in range(100,0,-7)]
print(numbers)                    #结果为[1089, 961, 784, 676, 576, 441, 361, 289, 196, 144, 100, 49, 25, 9, 0]