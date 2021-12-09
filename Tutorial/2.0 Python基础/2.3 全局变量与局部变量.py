
# coding: utf-8

# # StudyQuant
# 作者 ： Rudy
# 
# ## 局部变量
# 当你在函数定义内声明变量的时候，它们与函数外具有相同名称的其他变量没有任何关系，即
# 变量名称对于函数来说是 局部 的。这称为变量的 作用域 。所有变量的作用域是它们被定义的
# 块，从它们的名称被定义的那点开始。
# 
# **只能在申明的函数内部访问**

# In[11]:


def func(x):
    print ('x is', x)
    x = 2
    print ('Changed local x to', x)
    
x = 50
func(x)


print ('x is still', x)


# ## 全局变量
# 
# **在整个程序范围内访问**
# 
# **在函数外的变量，未申明GLOBAL的变量都被默认为 全局变量**
# 
# 

# ## 使用global语句
# 如果你想要为一个定义在函数外的变量赋值，那么你就得告诉Python这个变量名不是局部的，
# 而是 全局 的。我们使用global语句完成这一功能。没有global语句，是不可能为定义在函数外
# 的变量赋值的。
# 
# 
# 你可以使用定义在函数外的变量的值（假设在函数内没有同名的变量）。然而，我并不鼓励你
# 这样做，并且你应该尽量避免这样做，因为这使得程序的读者会不清楚这个变量是在哪里定义
# 的。**使用global语句可以清楚地表明变量是在外面的块定义的。**

# In[17]:


def func():
    global x
#     print ('x is', x)
    x = 2
    print ('Changed local x to', x)
    


# In[19]:


x = 50
func()
x


# In[20]:


def func():
#     global x
#     print ('x is', x)
    x = 20
    print ('Changed local x to', x)


# In[21]:


x = 50
func()


# In[22]:


print ('x is still', x)


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
