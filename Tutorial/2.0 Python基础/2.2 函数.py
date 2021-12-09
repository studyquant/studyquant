
# coding: utf-8

# ## 函数
# 
# 函数是重用的程序段。它们允许你给一块语句一个名称，然后你可以在你的程序的任何地方使用这个名称任意多次地运行这个语句块。这被称为 调用 函数。我们已经使用了许多内建的函数，比如len和range。
# 
# 函数通过def关键字定义。def关键字后跟一个函数的 标识符 名称，然后跟一对圆括号。圆括号之中可以包括一些变量名，该行以冒号结尾。接下来是一块语句，它们是函数体。
# 
# 下面这个例子将说明这事实上是十分简单的：
# 
# 函数名后面的空的小括号表明，函数不带有任何参数。
# 
# 
# 函数定义的第一行叫做函数头；其余的部分叫做函数体。函数头必须要以一个分号结尾，
# 
# 
# 函数体必须要有缩进。通常，缩进四个空格。函数体可以包含任意数量

# In[2]:


def print_name():
    print('Rudy')
    
print_name()
print_name()


# In[3]:

#CTRL+enter
def print_name(name):
    print(name)

    
print_name('nike')


# In[4]:


def check_int_type(data):
    if type(data) != int:
        raise TypeError('type error')
    print ("type correct")


# In[6]:


check_int_type('s')


# In[7]:


check_int_type(22)


# ## 默认参数值
# 对于一些函数，你可能希望它的一些参数是 可选 的，如果用户不想要为这些参数提供值的
# 话，这些参数就使用默认值。这个功能借助于默认参数值完成。你可以在函数定义的形参名后
# 加上赋值运算符（=）和默认值，从而给形参指定默认参数值。
# 
# 注意，默认参数值应该是一个参数。更加准确的说，默认参数值应该是不可变的——这会在后
# 面的章节中做详细解释。从现在开始，请记住这一点。

# In[15]:


def print_name(name, number = 2):
    print(name * number) 


# In[16]:


print_name("rudy",number = 1)


# In[20]:


def func(a, b=5, c=10):
    print ('a is', a, 'and b is', b, 'and c is', c)
    
func(5, b=5, c=10)


# In[21]:


func(5)


# In[23]:


func(5,6)


# In[24]:


func(5,c =20)


# ## return语句
# return语句用来从一个函数 返回 即跳出函数。我们也可选从函数 返回一个值 。

# In[25]:


def func(a, b=5, c=10):
    print ('a is', a, 'and b is', b, 'and c is', c)
    return a+b+c


func(5, b=5, c=10)


# ## DocStrings
# Python有一个很奇妙的特性，称为 文档字符串 ，它通常被简称为 docstrings 。DocStrings是一个
# 重要的工具，由于它帮助你的程序文档更加简单易懂，你应该尽量使用它。你甚至可以在程序
# 运行的时候，从函数恢复文档字符串！

# In[28]:


def func(a, b=5, c=10):
    """add all parameters"""

    print ('a is', a, 'and b is', b, 'and c is', c)
    return a+b+c


func.__doc__


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
