import matplotlib.pyplot as plt

def plot_indicators(df):
    plt.figure(figsize=(14,10))

    plt.subplot(3, 1, 1)
    plt.plot(df['Close'], label='Close')
    plt.plot(df['SMA_20'], label='SMA 20')
    plt.title('Close Price and SMA 20')
    plt.legend()

    plt.subplot(3, 1, 2)
    plt.plot(df['RSI_14'], label='RSI 14', color='orange')
    plt.axhline(70, color='red', linestyle='--')
    plt.axhline(30, color='green', linestyle='--')
    plt.title('RSI')
    plt.legend()

    plt.subplot(3, 1, 3)
    plt.plot(df['MACD'], label='MACD')
    plt.plot(df['MACD_Signal'], label='Signal')
    plt.bar(df.index, df['MACD_Hist'], label='Histogram', alpha=0.3)
    plt.title('MACD')
    plt.legend()

    plt.tight_layout()
    plt.show()