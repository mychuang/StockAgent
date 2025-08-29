import yfinance as yf

def get_stock_data(symbol: str, period: str = "6mo"): #抓取近半年日線數據
    df = yf.download(symbol, period=period, auto_adjust=False)
    if df.empty:
        raise ValueError("No data found for symbol: " + symbol)
    return df