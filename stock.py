import pandas as pd
import yfinance as yf
import datetime as dt

from pandas_datareader import data as pdr

from hiddenprint import HiddenPrints


yf.pdr_override()


class Stock:
    def __init__(self, stock: str, start_date: list, end_date=None):
        self.stock: str = stock
        self.start_date: dt.datetime = dt.datetime(start_date[0], start_date[1], start_date[2])
        if end_date is None:
            self.end_date: dt.datetime = dt.datetime.now()
        else:
            self.end_date: dt.datetime = dt.datetime(end_date[0], end_date[1], end_date[2])
        self.stock_df: pd.DataFrame = pd.DataFrame()

        self.get_data()

    def __str__(self):
        print("cols: {}".format(self.stock_df.columns.values))
        print(self.stock_df, end="")
        return ""

    def print_full(self):
        print(self.stock_df.to_string())

    def get_data(self):
        with HiddenPrints():
            self.stock_df = pdr.get_data_yahoo(self.stock, self.start_date, self.end_date)
