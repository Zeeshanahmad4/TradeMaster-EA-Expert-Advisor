# utils/helper_functions.py

def calculate_average(trading_data):
    """
    Calculate the average of the trading data.
    """
    return sum(trading_data) / len(trading_data) if trading_data else 0
