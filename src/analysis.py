import pandas as pd
import numpy as np

def calculate_moving_average(data, window=20):
    """
    Calculate simple moving average for the given data.
    
    :param data: DataFrame containing stock prices
    :param window: Number of days for the moving average
    :return: DataFrame with moving average
    """
    data['SMA'] = data['Close'].rolling(window=window).mean()
    return data

def calculate_exponential_moving_average(data, span=20):
    """
    Calculate exponential moving average for the given data.
    
    :param data: DataFrame containing stock prices
    :param span: Span for EMA calculation
    :return: DataFrame with EMA
    """
    data['EMA'] = data['Close'].ewm(span=span, adjust=False).mean()
    return data

def calculate_RSI(data, window=14):
    """
    Calculate the Relative Strength Index (RSI) for given data.
    
    :param data: DataFrame containing stock prices
    :param window: Window length for RSI calculation
    :return: DataFrame with RSI
    """
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).fillna(0)
    loss = (-delta.where(delta < 0, 0)).fillna(0)
    
    avg_gain = gain.rolling(window=window).mean()
    avg_loss = loss.rolling(window=window).mean()
    
    rs = avg_gain / avg_loss
    data['RSI'] = 100 - (100 / (1 + rs))
    return data

def calculate_bollinger_bands(data, window=20):
    """
    Calculate Bollinger Bands for the given data.
    
    :param data: DataFrame containing stock prices
    :param window: Number of days for moving average
    :return: DataFrame with Bollinger Bands (upper and lower)
    """
    sma = data['Close'].rolling(window=window).mean()
    std_dev = data['Close'].rolling(window=window).std()
    data['Bollinger_Upper'] = sma + (std_dev * 2)
    data['Bollinger_Lower'] = sma - (std_dev * 2)
    return data
