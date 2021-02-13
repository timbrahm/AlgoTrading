import datetime as dt

from stock import Stock


class BackTester:
    def __init__(self, start_balance: int, stock: Stock, start_date: list, end_date=None):
        self.balance: int = start_balance
        self.stock: Stock = stock
        self.start_date: dt.datetime = dt.datetime(start_date[0], start_date[1], start_date[2])
        if end_date is None:
            self.end_date: dt.datetime = dt.datetime.now()
        else:
            self.end_date: dt.datetime = dt.datetime(end_date[0], end_date[1], end_date[2])
