from stock import Stock
from backtest import BackTester


def main():
    start_date = [2015, 1, 1]
    stock = Stock("TQQQ", start_date)
    starting_balance = 1000000
    back_tester = BackTester(starting_balance, stock, start_date)
    print(stock)
    return 0


if __name__ == "__main__":
    main()
