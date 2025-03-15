#支付串就是一系列字符，用引号括起来表示，引号可以是单引号也可以是双引号
name="eric"
sentence1="hello?"
sentence2="is evrything ok?"
sentence3="but noone answer!"
#对文本的各个字符串部分进行变量的赋值。
print(f'\"{sentence1.title()}\"{name.title()} says,\"{sentence2.title()}?\"\n\t\"{sentence3.title()}\"')
#f字符串的运用——f"{变量}"=输出该变量所代表的值，title（）是首字母大写，\n是换行，\t是添加制表符，\‘、\“是添加单、双引号。
word=f'\"{sentence1.title()}\"{name.title()} says,\"{sentence2.title()}?\"\n\t\"{sentence3.title()}\"'
#也可以对一段代码赋值给变量。
print(f'{word.lower()}\n{word.upper()}')
#lowwer（）为全小写、upper（）为全大写。
sentence4="   wtf python   "
#该句子前后有空格
print(f'{sentence4}!\n{sentence4.rstrip()}!\n{sentence4.lstrip()}!\n{sentence4.strip()}!')
#rstrip()是字符串尾端删掉空格，lstrip()是字符串开头删掉空格，strip()是字符串首尾删掉空格。

#输出结果为：
#"Hello?"Eric says,"Is Evrything Ok??"
#        "But Noone Answer!"            
#"hello?"eric says,"is evrything ok??"
#        "but noone answer!"            （全小写）
#"HELLO?"ERIC SAYS,"IS EVRYTHING OK??"
#        "BUT NOONE ANSWER!"            （全大写）
#   wtf python   !
#   wtf python!                         （去尾空格）
#wtf python   !                         （去头空格）
#wtf python!                            （去头尾空额）