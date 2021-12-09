"""
=========================================================
* Powered by StudyQuant 
* author: Rudy
* wechat:studyquant88
=========================================================
* Product Page: https://studyquant.com
* Copyright 2021 StudyQuant
* License (https://studyquant.com/)
* Coded by https://studyquant.com
=========================================================
* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
"""

"""
定投交易策略
每隔一段时间，下单
"""

from datetime import datetime
import time
# 模仿购买股票函数
def buy(symbol):
    print(f'buy 100 {symbol} shares, time:{datetime.now()}' )


if __name__ == "__main__":

    while True:
        time.sleep(5)
        buy(symbol = 'apple')


