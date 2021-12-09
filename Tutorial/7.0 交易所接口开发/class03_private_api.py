"""
=========================================================
* Powered by StudyQuant 
* author: Rudy
* wechat:82789754
=========================================================
* Product Page: https://studyquant.com
* Copyright 2021 StudyQuant
* License (https://studyquant.com/)
* Coded by https://studyquant.com
=========================================================
* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
"""
import time
import ccxt
import pandas as pd

# 如果下面代码，无法导入，就注释掉
from cryptoquant.config.config import binance_api_key, binance_secret_key

if __name__ == "__main__":
    # binance_api_key = ''
    # binance_secret_key = ''
    # 实例化对象
    exchange = ccxt.binance({
        'apiKey': binance_api_key,
        'secret': binance_secret_key,
        'timeout': 3000,
        'enableRateLimit': True,
    })

    # 获取K线
    # symbol = 'BTC/USDT'
    # kline_data = exchange.fetch_ohlcv(symbol, '1d')
    # print('kline_data',kline_data)
    # kline_df = pd.DataFrame(kline_data,columns=['time', 'open', 'high', 'low', 'close', 'volume'])
    # kline_df.index = pd.to_datetime(kline_df['time'], unit='ms')
    # kline_df.loc[:, 'localminute'] = kline_df['time'].apply(lambda x :time.localtime(int(x/1000)))
    # kline_df.loc[:, 'timestamp'] = kline_df['localminute'].apply(lambda x :time.strftime("%Y-%m-%d %H:%M:%S", x))

    # print(kline_df)
    # -----K线转换方法2-----------
    symbol = 'BTC/USDT'
    kline_data = exchange.fetch_ohlcv(symbol, '1d')
    kline_data_df = pd.DataFrame(kline_data, columns=['Datetime', 'Open', 'High', 'Low', 'Close', 'Vol'])
    print('kline_data', kline_data_df)
    kline_data_df['Datetime'] = kline_data_df['Datetime'].apply(exchange.iso8601)
    print(kline_data_df)
    # exchange.iso8601

    # 获取账户余额
    balance = exchange.fetch_balance()
    print(balance)
    usdt_info = balance['USDT']
    usdt_balance = usdt_info['free']
    print('get USDT info', usdt_balance)

    """
    fetchOpenOrders() – fetches a list of open orders.
    fetchClosedOrders() – fetches a list of closed (or canceled) orders.
    fetchOrders() – fetches a list of all orders (either open or closed/canceled).
    fetchMyTrades()
    """

    # 获取未成交订单
    open_orders = exchange.fetchOpenOrders(symbol=symbol)
    print('open_orders', open_orders)

    # 获取全部订单
    all_orders = exchange.fetchOrders(symbol=symbol)
    print('all_orders', all_orders)

    # 获取指定订单 # fetchOrder (id, symbol = undefined, params = {})
    order_id = '3672034332'
    order_info = exchange.fetchOrder(id=order_id, symbol=symbol)
    print('order_info', order_info)

    # 如何进行实盘交易

    # order_info = exchange.create_limit_buy_order(symbol, amount, pirce)
    # exchange.iso8601

    pass
