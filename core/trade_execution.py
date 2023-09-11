# core/trade_execution.py

def execute_trade(condition, trading_data):
    """
    Execute a trade based on the provided condition and trading data.
    :param condition: The condition to check before executing the trade.
    :param trading_data: The trading data for analysis.
    :return: Trade execution status (Success/Failure)
    """
    if condition(trading_data):
        return "Success"
    else:
        return "Failure"
