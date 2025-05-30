import pynance as pn

def calculate_financial_metrics(ticker):
    stock = pn.Stock(ticker)
    hist = stock.history()
    
    metrics = {
        'last_close': hist['close'].iloc[-1],
        'average_volume': hist['volume'].mean(),
        'max_high': hist['high'].max(),
        'min_low': hist['low'].min()
    }
    return metrics