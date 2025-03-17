#该例子中，列表均使用c0,a1,d2,b3,f4,h5,e6,g7

#使用sort()对列表进行以字母顺序的永久排列
letters=['c0','a1','d2','b3','f4','h5','e6','g7']
letters.sort()
#列表名.sort()
print(letters)#结果为['a1', 'b3', 'c0', 'd2', 'e6', 'f4', 'g7', 'h5']，以首字母顺序排序

#向sort()传递参数reverse=True，对列表进行以字母顺序的永久反序排列
letters=['c0','a1','d2','b3','f4','h5','e6','g7']
letters.sort(reverse=True)
#列表名.sort(reverse=True)
print(letters)#结果为['h5', 'g7', 'f4', 'e6', 'd2', 'c0', 'b3', 'a1']，以首字母顺序的反序排序

#使用sorted()对列表进行临时排列
letters=['c0','a1','d2','b3','f4','h5','e6','g7']
print(sorted(letters))#结果为['a1', 'b3', 'c0', 'd2', 'e6', 'f4', 'g7', 'h5']，以首字母顺序排序
#sorted(列表名)，因为是临时排序，所以单独使用没有意义，得搭配print或者再将其新建列表
print(letters)#结果为['c0', 'a1', 'd2', 'b3', 'f4', 'h5', 'e6', 'g7']，因为只是临时排列，所以对原列表没有影响

#向sorted()传递参数reverse=True,对列表进行以字母顺序的临时反序排列
letters=['c0','a1','d2','b3','f4','h5','e6','g7']
print (sorted(letters,reverse=True))#结果为['h5', 'g7', 'f4', 'e6', 'd2', 'c0', 'b3', 'a1']，以首字母顺序的反序排序
#sort(列表名,reverse=True),使用方法和sprted()一致
print(letters)#结果为['c0', 'a1', 'd2', 'b3', 'f4', 'h5', 'e6', 'g7']，因为只是临时排列，所以对原列表没有影响


#使用reverse()对列表进行以原始顺序的倒序排列
letters=['c0','a1','d2','b3','f4','h5','e6','g7']
letters.reverse()
#列表名.reverse()
print(letters)#['g7', 'e6', 'h5', 'f4', 'b3', 'd2', 'a1', 'c0']，以原始顺序的倒序排列
letters.reverse()
print(letters)#['c0', 'a1', 'd2', 'b3', 'f4', 'h5', 'e6', 'g7']，由于只是按原序的倒序排列，那么倒序的倒序就能复原

#使用len()对列表进行长度测量（元素计数）
letters=['c0','a1','d2','b3','f4','h5','e6','g7']
print (len(letters))#结果为8，可见与索引的计数不同，是从1开始，而非从0
#len(列表名)，与sorted()类似，得搭配print或者再将其新建变量
