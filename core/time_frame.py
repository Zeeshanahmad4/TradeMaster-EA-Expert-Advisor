# core/time_frame.py

CURRENT_TIME_FRAME = "M15"  # default time frame

def switch_time_frame(new_time_frame):
    """
    Switch to a new time frame for analysis.
    :param new_time_frame: The time frame to switch to.
    :return: None
    """
    global CURRENT_TIME_FRAME
    CURRENT_TIME_FRAME = new_time_frame
