import time

def tabs():
    """Return a list of the next 5 days starting with today"""
    
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
            'Sunday']
    
    tabs = []    
    count = time.gmtime()[6]
    for i in range(5):
        tabs.append(days[count])
        count += 1
        if count == 7:
            count = 0
        
    return tabs


def time_intervals(n):
    """Return a list of length n in reverse order.
    items(int): Number of timeslots to be returned.
    """
    
    times = ['21:00','18:00', '15:00', '12:00', '9:00', '6:00', '3:00', '00:00']
    selection = times[:n]
    
    return selection[::-1]
    