
# coding: utf-8

# 
# # StudyQuant
# 作者 ： Rudy

# # 基本数据类型

# Python 是一种动态类型语言，这意味着. Python 解择程序在运行时推知对象的类也C
# 等编译语言通常是静态类型语言，在这类语言，对象类型必须在编译之前与对象
# 绑定

# # Python有五个标准的数据类型：
# - Numbers（数字）
# - String（字符串）
# - List（列表）
# - Tuple（元组）
# - Dictionary（字典）
# 

# 四种不同的数类型：
# - int（整型）  0，1 等
# - long（长整型[也可以代表八进制和十六进制]）
# - float（浮点型） 3.6 等
# - complex（复数）  如  4+2j
# - Bool ： True, False
# - String : “hello, world”
# 

# # 一切都是对象

# ## Basic Data Types

# # int 整数

# In[28]:


a = 10
type(a)


# In[29]:


a.bit_length()  #获得表现int 对象所需的位数


# In[30]:


a = 100000


# In[31]:


print(a)


# In[8]:


googol = 10 ** 100
googol


# In[32]:


1 + 4


# In[33]:


1 / 4


# In[34]:


type(1 / 4)


# In[35]:


5*6


# In[36]:


10/2


# ## 数字的基本操作
# python中的数字都支持下面的操作：
# 
#     1、x + y：x加y；
#     2、x - y：x减y；
#     3、x * y：x和y的积；
#     4、x / y：x和y的商；
#     5、x // y：x和y的商的下限，即取整；
#     6、x % y：x/y的余；
#     7、abs(x)：x为整型和浮点型，返回x的绝对值；x为复数型，返回x的magnitude（注）；
#     8、int(x)：将x转换到整型；
#     9、float(x)：将x转换到浮点型；
#     10、complex(re, im)：得到实部为re，虚部为im的复数；
#     11、c.conjugate()：返回复数c的共轭复数；
#     12、divmod(x, y)：返回对(x // y, x % y)；
#     13、pow(x, y)：x的y次方；
#     14、x ** y：同pow(x, y)，x的y次方。
#     

# ### Floats

# In[43]:


1 / 4


# In[44]:


type (1. / 4)


# In[45]:


b = 0.35
type(b)


# ### Strings

# 而'Hello, World!' 是一个字符串，之所以这
# 么称呼是因为它包含一“串”字母。因为被引号包围，读者（以及解释器）可以将它们识
# 别为字符串。

# In[46]:


t = 'studyQuant offers Python Courses'


# In[47]:


t


# In[48]:


t.capitalize()


# In[49]:


t.split()


# In[50]:


t.upper()


# In[51]:


t.find('studyquant')


# In[52]:


t.find('Python')


# In[53]:


t[18]


# In[54]:


t.replace(' ', '|')


# In[58]:


'http://www.python.org'.strip('htp:/')


# 
## 更多量化学习资源
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
# *   [课程](https://appcop3i2898823.h5.xiaoeknow.com/homepage)
# - [量化投资与数据分析实战](http://study.163.com/course/introduction/1004855008.htm?share=2&shareId=400000000342001)
# - [量化投资与数字货币实战](https://appcop3i2898823.h5.xiaoeknow.com/homepage)
# *   [知乎](https://zhuanlan.zhihu.com/studyquant)
# *   [简书](https://www.jianshu.com/u/495eda774816)
# *   [公众号](https://mp.weixin.qq.com/s__biz=MzU5NzU5NjIwMQ==&mid=100000028&idx=1&sn=2f8c053849f296455ec85406e80b2a2d&chksm=7e50405a4927c94c18ba438e0c309a7d13883621ddf02904266026556e9994ad1c3f8558327d&mpshare=1&scene=1&srcid=0810AEevB9zID4Ywzl1icPfA#rd)
#
# #