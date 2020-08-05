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
    
def split_data(data):
    pass
