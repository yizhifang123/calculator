import yfinance as yf

msft = yf.Ticker("MSFT")

# get stock info
print(msft.info)

# get historical market data
hist = msft.history(period="max")

# show actions (dividends, splits)
print(msft.actions)

# show dividends
print(msft.dividends)

# show splits
print(msft.splits)

# show financials
print(msft.financials)
print(msft.quarterly_financials)

stock = yf.Ticker('1155.KL')

# show major holders
print(stock.major_holders)

# show institutional holders
print(stock.institutional_holders)

# show balance heet
print(msft.balance_sheet)
print(msft.quarterly_balance_sheet)

# show cashflow
print(msft.cashflow)
print(msft.quarterly_cashflow)

# show earnings
print(msft.earnings)
print(msft.quarterly_earnings)

# show sustainability
print(msft.sustainability)

# show analysts recommendations
print(msft.recommendations)

# show next event (earnings, etc)
print(msft.calendar)

# show ISIN code - *experimental*
# ISIN = International Securities Identification Number
print(msft.isin)

# show options expirations
print(msft.options)

# get option chain for specific expiration
print(opt = msft.option_chain('YYYY-MM-DD'))
# data available via: opt.calls, opt.puts
