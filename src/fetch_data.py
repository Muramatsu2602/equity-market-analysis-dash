import yfinance as yf

def fetch_stock_data(symbol, start_date, end_date):
    """
    Fetch historical stock data from Yahoo Finance.
    
    :param symbol: Stock symbol
    :param start_date: Start date in YYYY-MM-DD
    :param end_date: End date in YYYY-MM-DD
    :return: DataFrame with historical stock data
    """
    stock = yf.Ticker(symbol)
    data = stock.history(start=start_date, end=end_date)
    return data
