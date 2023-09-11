# core/main.py

from indicators import graph_marker
from config import settings
from core import time_frame, lot_size, trade_execution
from utils import helper_functions

def main():
    """
    Main function to execute the EA.
    """
    trading_data = [100, 101, 99, 105, 98, 110]
    marked_points = graph_marker.mark_graph(trading_data)
    average_price = helper_functions.calculate_average(trading_data)
    condition = lambda data: data[-1] > average_price if data else False
    trade_status = trade_execution.execute_trade(condition, trading_data)
    print(f"Trade Execution Status: {trade_status}")

if __name__ == "__main__":
    main()
