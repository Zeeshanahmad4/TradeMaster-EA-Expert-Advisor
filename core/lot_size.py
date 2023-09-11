# core/lot_size.py

from config import settings

def adjust_lot_size(new_lot_size):
    """
    Adjust the lot size for trading.
    :param new_lot_size: The new lot size to adjust to.
    :return: None
    """
    settings.LOT_SIZE = new_lot_size
