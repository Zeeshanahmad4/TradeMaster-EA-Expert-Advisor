# indicators/graph_marker.py

def mark_graph(trading_data):
    """
    Analyze the trading data and mark points of interest on the graph.
    :param trading_data: The trading data to be analyzed.
    :return: List of points (coordinates) to mark on the graph.
    """
    marked_points = []
    for i in range(1, len(trading_data)):
        if trading_data[i] - trading_data[i-1] > 1:  # Significant increase
            marked_points.append((i, trading_data[i]))
        elif trading_data[i-1] - trading_data[i] > 1:  # Significant decrease
            marked_points.append((i, trading_data[i]))
    return marked_points
