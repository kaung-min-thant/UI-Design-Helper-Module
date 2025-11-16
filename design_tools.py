# 1. UI Check: Text Length
def is_text_fit(text):
    """
    Checks if the element text fits the maximum allowed length (e.g., for a button or title).
    Returns True if length is 15 characters or less.
    """
    MAX_LENGTH = 15
    return len(text) <= MAX_LENGTH 

# 2. UI Check: Responsive Sizing
def calculate_padding(screen_size, base_unit=8):
    """
    Calculates dynamic padding (in pixels) based on screen size using a fixed ratio.
    This simulates responsive design spacing.
    """
    if screen_size < 600:
        multiplier = 2 # 16px padding
    elif screen_size < 1200:
        multiplier = 3 # 24px padding
    else:
        multiplier = 4 # 32px padding
        
    return base_unit * multiplier
