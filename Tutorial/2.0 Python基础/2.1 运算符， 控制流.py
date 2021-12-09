
# coding: utf-8

# 
# # StudyQuant
# 作者 ： Rudy
# 
# ## 运算符

# ## 简介

# 你编写的大多数语句（逻辑行）都包含表达式。一个简单的表达式例子如2 + 3。一个表达式可以分解为运算符和操作数。
# 
# 
# 运算符 的功能是完成某件事，它们由如+这样的符号或者其他特定的关键字表示。运算符需要
# 数据来进行运算，这样的数据被称为 操作数 。

# In[3]:


2 + 3


# In[4]:


3 * 5


# ![image.png](https://upload-images.jianshu.io/upload_images/16017709-f0b55f556208d078.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
# ![image.png](https://upload-images.jianshu.io/upload_images/16017709-7f8964a396750cc2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
# 

# ## 运算符优先级

# 如果你有一个如2 + 3 * 4那样的表达式，是先做加法呢，还是先做乘法？我们的中学数学告诉
# 我们应当先做乘法——这意味着乘法运算符的优先级高于加法运算符。
# 

# 下面这个表给出Python的运算符优先级，从最低的优先级（最松散地结合）到最高的优先级
# （最紧密地结合）。这意味着在一个表达式中，Python会首先计算表中较下面的运算符，然后
# 在计算列在表上部的运算符。
# 
# 

# 下面这张表（与Python参考手册中的那个表一模一样）已经顾及了完整的需要。事实上，我建
# 议你使用圆括号来分组运算符和操作数，以便能够明确地指出运算的先后顺序，使程序尽可能
# 地易读。例如，2 + (3 * 4)显然比2 + 3 * 4清晰。与此同时，圆括号也应该正确使用，而不应该
# 用得过滥（比如2 + (3 + 4)）。

# In[2]:


2 + (3 * 4)    #更清晰


# In[3]:


2 + 3 * 4


# ![image.png](https://upload-images.jianshu.io/upload_images/16017709-c291c93fe3e918f1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
# 

# ## 控制流
# 在到目前为止我们所见到的程序中，总是有一系列的语句，Python 忠实地按照它
# 们的顺序执行它们。如果你想要改变语句流的执行顺序，该怎么办呢？例如，你想要
# 让程序做一些决定，根据不同的情况做不同的事情，例如根据时间打印“早上好”或
# 者“晚上好”。你可能已经猜到了，这是通过控制流语句实现的。在Python 中有三种
# 控制流语句——if、for 和while 。

# ## Python 条件语句
# 
# Python条件语句是通过一条或多条语句的执行结果（True或者False）来决定执行的代码块。
# 
# 可以通过下图来简单了解条件语句的执行过程:
# ![image.png](http://www.runoob.com/wp-content/uploads/2013/11/if-condition.jpg)

# if 语句用来检验一个条件，如果条件为真，我们运行一块语句（称为if-块），否
# 则我们处理另外一块语句（称为else-块）。else 子句是可选的。

# In[9]:


if True:
    pass
    print('good')
    abc = 5 * 3
    print(abc)


# In[11]:


flag = False
name = 'Rudy'
if name == 'python':        # 判断变量否为'python'
    flag = True              # 条件成立时设置标志为真
    print ('welcome boss')    # 并输出欢迎信息
else:
    print (name)              # 条件不成立时输出变量名称


# ## while 语句
# 
# 只要在一个条件为真的情况下， while 语句允许你重复执行一块语句。while 语
# 句是所谓循环语句的一个例子。while 语句有一个可选的else 从句。

# In[12]:


import time
b = 0

while b<10:
    b += 1
    print(b)
    time.sleep(1)
else:
    print(b)
    
    
    
    


# ## for 循环
# 
# for..in 是另外一个循环语句，它在一序列的对象上迭代，即逐一使用序列中的每
# 个项目。
# 
# 如何工作: 
# 
# 在这个程序中，我们打印了一个序列的数。我们使用内建的range 函数生成这个数的序列
# 
# 
# 我们所做的只是提供两个数， range 返回一个序列的数。这个序列从第一个数开始到第二个数为止。例如， range(1,5) 给出序列[1, 2, 3, 4]。默认地， range 的步长为1。
# 
# 如果我们为range 提供第三个数，那么它将成为步长。例如，range(1,5,2) 给出[1,3]。记住，range 向上延伸到第二个数，即它不包含第二个数。

# In[13]:


range(10)   #前闭后开


# In[14]:


for i in range(10):
    print (i)


#  range([start,] stop[, step])

# In[18]:


list(range(1,5,2) )


# ## break 语句
# 
# break 语句是用来终止循环语句的，即哪怕循环条件没有变为False 或序列还没有
# 被完全迭代结束，也停止执行循环语句。
# 一个重要的注释是，如果你从for 或while 循环中终止，任何对应的循环else 块
# 将不执行。

# In[20]:


for i in range(10):
    print (i)
    if i == 8:
        break
        
        
        


# ## continue 语句
# continue 语句被用来告诉Python 跳过当前循环块中的剩余语句，然后继续进行下
# 一轮循环。

# In[25]:


for i in range(15):
    if i % 5 == 0:
        continue
    else:
        print (i)


# 我们已经学习了如何使用三种控制流语句——if、while和for以及与它们相关的break和continue
# 语句。它们是Python中最常用的部分，`熟悉这些控制流是应当掌握的基本技能。

# 
# ## 更多量化学习资源
# 
# <img src="https://upload-images.jianshu.io/upload_images/10681489-129dda5fc09f706c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240" alt="StudyQuant" width="60%" align="middle" border="0"><br>
# 
# 扫上方二维码，关注公众账号 量化投资学院 ，获取下列免费资源
# - 回复**“热点研报”**，获取近年热点券商金融工程研究报告
# - 回复**“Python3”**，获取Python免费学习教程
# - 回复**“quant教材与面试经验”**， 获取 quant教材与面试经验 资料
# *   [更多福利请点击此链接](https://www.jianshu.com/p/2ffb29f1a1aa)
# 
# 
# ## 关注StudyQuant
# *   [课程](http://study.163.com/provider/400000000342001/index.htm?share=2&shareId=400000000342001)
# - [量化投资与数据分析实战](http://study.163.com/course/introduction/1004855008.htm?share=2&shareId=400000000342001)
# - [量化投资与数字货币实战](http://study.163.com/course/courseMain.htm?courseId=1005630014&share=2&shareId=400000000342001#/courseDetail?tab=1)
# *   [简书](https://www.jianshu.com/u/495eda774816)
# *   [公众号](https://mp.weixin.qq.com/s__biz=MzU5NzU5NjIwMQ==&mid=100000028&idx=1&sn=2f8c053849f296455ec85406e80b2a2d&chksm=7e50405a4927c94c18ba438e0c309a7d13883621ddf02904266026556e9994ad1c3f8558327d&mpshare=1&scene=1&srcid=0810AEevB9zID4Ywzl1icPfA#rd)
# 
