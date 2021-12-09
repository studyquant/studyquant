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
import schedule
from datetime import datetime
import time
# 模仿购买股票函数
def buy(symbol):
    print(f'buy 100 {symbol} shares, time:{datetime.now()}' )


if __name__ == "__main__":
    symbol = "Apple"
    schedule.every(1).second.do(buy,symbol)
    schedule.every(10).minutes.do(buy,symbol)
    # schedule.every().monday.do(buy, symbol)

    while True:
        schedule.run_pending()
        time.sleep(1)


