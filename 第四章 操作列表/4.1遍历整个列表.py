cars=['Mercedes-Benz','Aud','Volkswagen','Porsche','Ford','Tesla','Chevrolet','Cadillac','Rolls-Royce','Aston Martin','Ferrari','Lamborghini','Maserati','Citroën','Renault']
for car in cars:
#for 临时变量 in 列表名：
    print (car)#结果为输出列表中的每一个元素

for car in cars:#将名为cars的列表中每一个单个元素赋给临时变量car，同一词汇的单复形式有助于一眼看出目前是哪一个列表被循环
    print ( f'\"I think {car} is very good.\"' )
    print ( f'\"But it\'s not realistic for me to buy a {car}\"\n' )
    #上述结果为每一个元素都被输出了相同格式的两句话
print ('Because I\'m just a student')#该行语句仅被输出了一遍
#可见，在for循环下缩进的每一行语句都会被循环执行，直到循环结束才会执行之后未缩进的语句，且该语句仅执行一次。


