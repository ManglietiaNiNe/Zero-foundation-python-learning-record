games=['1st destiny 2','2nd fallout 4','3st persona 5 royal','4th doom eternal','5th monster hunter:world','6th battlefield 5']
#列表用方括号[]表示，元素间用逗号隔开，元素之间可以没有任何关系，列表的命名最好使用复数表示

print(games)
#结果为['1st destiny 2', '2nd fallout 4', '3st persona 5 royal', '4th doom eternal', '5th monster hunter:world', '6th battlefield 5']
#直接print列表，结果为等号后全部内容，由此可见列表为一种特殊形式的变量，并非被赋予单个的值，而是赋予一系列的元素

print(games[0])                #结果为1st destiny 2
print(games[0].title())        #结果为1St Destiny 2
#为了访问列表中的单个元素，需要指出该元素的索引，按序从0开始编号，而非1开始。与变量使用方法一致，可以加上title()等让输出的字符串更美观简洁

print(games[2])                #结果为3st persona 5 royal
#由于列表的排序是从0开始 ，所以第三个元素的索引为2
print(games[-1])               #结果为6th battlefield 5
#一种特殊的表示方法，如果要引用列表的最后一个元素，可以直接使用索引-1
print(games[-3],'\t',games[3]) #结果为4th doom eternal         4th doom eternal
#以此类推，索引-3就是倒数第三个，同时该元素也是正数第四个（索引为3）

games=['destiny 2','fallout 4','persona 5 royal','doom eternal','monster hunter:world','battlefield 5']
sntence=f"Whice game I'd like to play in saturday afternoon is {games[3].title()}."
#由于与变量使用方法一致，所以不仅可以加上title()等，也可以使用f字符串，在其他字符串中引用单个元素
print(sntence)
#结果为Whice game I'd like to play in saturday afternoon is Doom Eternal.当索引取0就是destiny2，以此类推