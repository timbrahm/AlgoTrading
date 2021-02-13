import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt

from pandas_datareader import data as pdr

MA = 50
SMA_STRING = "SMA_{}".format(MA)




def main():
    print("Please enter a stock ticker:")
    stock = input("> ")





    gains = 0
    gain_num = 0
    losses = 0
    loss_num = 0
    totalR = 1
    for pct in pct_change:
        if pct > 0:
            gains += pct
            gain_num += 1
        else:
            losses += pct
            loss_num += 1
        totalR = totalR * ((pct / 100) + 1)
    totalR = round((totalR - 1) * 100, 3)

    if gain_num > 0:
        avg_gain = gains / gain_num
        max_gain = max(pct_change)
    else:
        avg_gain = 0
        max_gain = None

    if loss_num > 0:
        avg_loss = losses / loss_num
        max_loss = min(pct_change)
        ratio = -avg_gain / avg_loss
    else:
        avg_loss = 0
        max_loss = None
        ratio = np.Inf

    if gain_num > 0 or loss_num > 0:
        batting_avg = gain_num / (gain_num + loss_num)
    else:
        batting_avg = 0

    print("\nResults for {} going back to {}".format(stock, stock_df.index[0]))
    print("Sample Size: {} trades".format(gain_num + loss_num))
    print("EMAs Used: {}".format(EMAS))
    print("Batting Average: {}".format(batting_avg))
    print("Number of Gains: {}".format(gain_num))
    print("Number of Losses: {}".format(loss_num))
    print("Gain / Loss Ratio: {}".format(ratio))
    print("Average Gain: {}".format(avg_gain))
    print("Average Loss: {}".format(avg_loss))
    print("Max Gain: {}".format(max_gain))
    print("Max Loss: {}".format(max_loss))
    print("Total Return {}%".format(totalR))

    return 0


if __name__ == "__main__":
    main()
