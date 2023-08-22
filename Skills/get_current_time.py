""" 
Summary:
    Get the current date and time

Name:
    get_current_date_time

Args:
    None

Returns:
    Current date and time as a string in the format YYYY-MM-DD HH:MM:SS
"""

from datetime import datetime

def get_current_date_time() -> str:
    '''A tool that allows you to get the current date and time.
   
    '''
    # Get the current date and time
    current_date_time = datetime.now()

    # Format the date and time as a string
    date_time_str = current_date_time.strftime("%Y-%m-%d %H:%M:%S")

    return date_time_str

def get_date_time_skill() -> str:
    '''A skill that allows you to get the current date and time.
   
    '''
    date_time_str = get_current_date_time()
    return f"Current date and time is: {date_time_str}"
