# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 21:37:51 2019

@author: admin
"""
"""
#你已经学习了如何在你的程序中定义一次函数而重用代码。如果你想要在其他程序中重用很多
#函数，那么你该如何编写程序呢？你可能已经猜到了，答案是使用模块。模块基本上就是一个
#包含了所有你定义的函数和变量的文件
"""


import sys




"""
如果你想要直接输入argv变量到你的程序中（避免在每次使用它时打sys.），那么你可以使用
from sys import argv语句。如果你想要输入所有sys模块使用的名字，那么你可以使用from sys
import *语句。这对于所有模块都适用。一般说来，应该避免使用from..import而使用import语
句，因为这样可以使你的程序更加易读，也可以避免名称的冲突。
"""


from math import log



from math import *



#模块的__name__



# 创建自己的模块


def sayhi():
    print('hello world')


version = '1.0'



if __name__ == '__main__':
    print ('This program is being run by itself')
    sys.path
    
    for i in sys.argv:
        print (i)
        
    print ('----------------------')
#    print (sys.argv[0])
#    print (sys.argv[1])
#    print (sys.argv[2])
    log(1)
    
    
else:
    print ('I am being imported from another module')
    








