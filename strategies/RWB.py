import pandas as pd

from typing import List

from stock import Stock


class RedWhiteBlue:
    def __init__(self, ema_list: list = None):
        if ema_list is None:
            self.ema_list = [3, 5, 8, 10, 12, 15, 30, 35, 40, 45, 50, 60]
        else:
            self.ema_list: list = ema_list

        self.strat_data_list = []

    def start(self, stock: Stock):
        self.add_data(stock)
        self.run_rwb()

    def add_data(self, stock=None, strat_data=None, results=None):
        self.strat_data_list.append({
            "stock": stock,
            "strat_data": strat_data,
            "results": results
        })

    def update_data(self, stock, strat_data=None, results=None):
        data = 0
        for i in range(len(self.strat_data_list)):
            if self.strat_data_list[i]["stock"] == stock:
                data = i
        if strat_data:
            self.strat_data_list[data]["strat_data"] = strat_data
        if results:
            self.strat_data_list[data]["results"] = strat_data

    def run_rwb(self):
        for ema in self.ema_list:
            stock_df["EMA_{}".format(ema)] = round(stock_df.iloc[:, 4].ewm(span=ema, adjust=False).mean(), 3)
        # print(stock_df.tail())

        pos = False
        pct_change = []
        buy_price = 0
        sell_price = 0
        for date in stock_df.index:
            c_min = min([stock_df["EMA_{}".format(ema)][date] for ema in EMAS[0:6]])
            c_max = max([stock_df["EMA_{}".format(ema)][date] for ema in EMAS[6:]])

            close = stock_df["Adj Close"][date]

            if c_min > c_max:
                if not pos:
                    pos = True
                    buy_price = close
                    print(date)
                    print("Buying now at {}\n".format(buy_price))
            elif c_min < c_max:
                if pos:
                    pos = False
                    sell_price = close
                    print(date)
                    print("Selling now at {}\n".format(sell_price))
                    pct_change.append((sell_price / buy_price - 1) * 100)
            if date == stock_df.index[-1] and pos:
                pos = False
                sell_price = close
                print(date)
                print("Selling now at {}\n".format(sell_price))
                pct_change.append((sell_price / buy_price - 1) * 100)
        print(pct_change)
