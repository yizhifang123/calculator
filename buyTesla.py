import yfinance as yf

tsla_df = yf.download('TSLA')
# tsla_df['Close'].plot(title="TSLA's stock price")

prev = 0
numStock = 0
totalSpent = 0
totalRevenue = 0

for date, r in tsla_df.iterrows():
    price = r['Open']
    if prev == 0:
        prev = price
        continue
    if price < prev * 0.95:
        print(date)
        print("Buy 1000 dollar")
        numStock += 1000 / price
        totalSpent += 1000

    if price > prev and numStock > 0 and price > 1.4 * totalSpent / numStock:
        print(date)
        print('Sell {} dollar'.format(0.3 * numStock * price))
        numStock = numStock * 0.70
        totalRevenue += 0.3 * numStock * price - 0.3 * totalSpent
        totalSpent = totalSpent * 0.70

    prev = price

print(totalRevenue)
print(numStock)
print(totalSpent)