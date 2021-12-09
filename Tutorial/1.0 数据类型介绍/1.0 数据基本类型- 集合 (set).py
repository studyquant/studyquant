
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

# 按F9,它会运行当前的代码行
# ctrl + enter
# shift + shift
# In[61]:


a = 10
type(a)


# In[62]:


a.bit_length()  #获得表现int 对象所需的位数


# In[63]:


a = 100000


# In[64]:


print(a)


# In[65]:


googol = 10 ** 100
googol


# In[66]:


1 + 4


# In[67]:


1 / 4


# In[68]:


type(1 / 4)


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

# In[59]:


1 / 4


# In[12]:


type (1. / 4)


# In[13]:


b = 0.35
type(b)


# In[14]:


b + 0.1


# In[15]:


c = 0.5
c.as_integer_ratio()


# In[16]:


b.as_integer_ratio()


# ### Strings

# 而'Hello, World!' 是一个字符串，之所以这
# 么称呼是因为它包含一“串”字母。因为被引号包围，读者（以及解释器）可以将它们识
# 别为字符串。

# In[48]:


t = 'StudyQuant offers Python Courses'


# In[49]:


t.capitalize()


# In[50]:


t.split()


# In[70]:


t.upper()


# In[72]:


t.find('studyquant')


# In[52]:


t.find('Python')


# In[53]:


t.replace(' ', '|')


# In[54]:


'http://www.python.org'.strip('htp:/')


# ## Basic Data Structures

# ### Tuples

# - Python的元组与列表类似，不同之处在于元组的元素不能修改。
# 
# - 元组使用小括号，列表使用方括号。
# 
# - 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。

# In[95]:


t = (1, 2.5, 'data')
type(t)


# In[96]:


t = 1, 2.5, 'data'
type(t)


# In[82]:


t[2]


# In[97]:


type(t[2])


# In[98]:


t.count('data')  # 对象位置


# In[99]:


t.index(1)  #对象的位置索引值


# In[91]:


# 以下修改元组元素操作是非法的。
#　t[0] = 100


# In[92]:


t2 = (2,3)


# In[100]:


# 创建一个新的元组
tup3 = t + t2
print (tup3)


# ### Lists

# 序列是Python中最基本的数据结构。序列中的每个元素都分配一个数字 - 它的位置，或索引，第一个索引是0，第二个索引是1，依此类推。
# 
# Python有6个序列的内置类型，但最常见的是列表和元组。
# 
# 序列都可以进行的操作包括索引，切片，加，乘，检查成员。
# 
# 此外，Python已经内置确定序列的长度以及确定最大和最小的元素的方法。
# 
# 列表是最常用的Python数据类型，它可以作为一个方括号内的逗号分隔值出现。
# 
# 列表的数据项不需要具有相同的类型
# 
# 创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可

# In[177]:


l = [1, 2.5, 'data']
l[2]


# In[179]:


t


# In[180]:


l = list(t)
l


# In[181]:


type(l)


# In[182]:


l.append([4, 3])  # append list at the end
l


# In[183]:


l.extend([1.0, 1.5, 2.0])  # append elements of list
l


# In[184]:


l.insert(1, 'insert')  # insert object before index position
l


# In[185]:


l.remove('data')  # remove first occurence of object
l


# In[186]:


p = l.pop(3)  # removes and returns object at index
print (l, p)


# In[187]:


l.pop(0)


# In[188]:


l


# In[189]:


l[2:4]  # 3rd to 4th element


# In[190]:


l.append('Google')   ## 使用 append() 添加元素


# 删除列表元素

# In[191]:


del l[2]


# #列表元素个数

# In[192]:


len(l) #


# In[204]:


price = []


# In[205]:


for i in range(10):
    price.append(i)


# In[206]:


price 


# # 布尔表达式

# 布尔表达式的结果要么是真(true），要么为假（false）。下面的例子是使用== 运算符，比
# 较两个操作数，如果相等则结果为True, 否则为False:

# In[10]:


True


# In[11]:


False


# In[12]:


5 == 5


# In[13]:


5 == 10


# In[14]:


a = 5 


# In[15]:


b = 10 


# In[16]:


a > b


# In[17]:


a < b


# In[18]:


a = 10


# In[21]:


a >= b


# In[22]:


a <= b


# In[23]:


if a == b:
    print ('相等')


# ### Dicts 字典

# 字典是另一种可变容器模型，且可存储任意类型对象。
# 
# 字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 , 分割，整个字典包括在花括号 {} 中 

# In[1]:


d = {
     'Name' : 'Rudy',
     'Country' : 'China',
     'Profession' : 'Quant',
     'Age' : 29
     }
type(d)


# In[2]:


print (d['Name'], d['Age'])


# In[3]:


d.keys()


# In[4]:


d.values()


# In[5]:


d.items()


# In[6]:


birthday = True
if birthday is True:
    d['Age'] += 1
print (d['Age'])


# In[7]:


d


# In[8]:


for key in d.keys():
    print (key)


# In[9]:


for key in d.values():
    print (key)


# ### Sets

# <img src="http://www.iplaypy.com/uploads/allimg/131215/2-131215203406215.jpg" alt="StudyQuant" width="60%" align="middle" border="0"><br>
# 

# In[3]:


s = set(['u', 'd', 'ud', 'du', 'd', 'du'])
s


# In[4]:


t = set(['d', 'dd', 'uu', 'u'])


# In[5]:


s.union(t)  # all of s and t


# In[6]:


s.intersection(t)  # both in s and t


# In[7]:


s.difference(t)  # in s but not t


# In[8]:


t.difference(s)  # in t but not s


# In[10]:


s.symmetric_difference(t)  # in either one but not both


# In[12]:


s.add("set")


# In[13]:


s


# In[15]:


s.remove('du')


# In[16]:


s


# In[17]:


t & s # 交集


# In[18]:


t|s  # 合集


# In[19]:


t -s   #相对补几，差集

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
# *   [课程](https://appcop3i2898823.h5.xiaoeknow.com/homepage)
# - [量化投资与数据分析实战](http://study.163.com/course/introduction/1004855008.htm?share=2&shareId=400000000342001)
# - [量化投资与数字货币实战](https://appcop3i2898823.h5.xiaoeknow.com/homepage)
# *   [知乎](https://zhuanlan.zhihu.com/studyquant)
# *   [简书](https://www.jianshu.com/u/495eda774816)
# *   [公众号](https://mp.weixin.qq.com/s__biz=MzU5NzU5NjIwMQ==&mid=100000028&idx=1&sn=2f8c053849f296455ec85406e80b2a2d&chksm=7e50405a4927c94c18ba438e0c309a7d13883621ddf02904266026556e9994ad1c3f8558327d&mpshare=1&scene=1&srcid=0810AEevB9zID4Ywzl1icPfA#rd)
#
