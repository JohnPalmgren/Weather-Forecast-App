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


def time_intervals(items):
    
    times = ['21:00','18:00', '15:00', '12:00', '9:00', '6:00', '3:00', '00:00']
    selection = times[:items]
    
    return selection[::-1]
    


def user_input(inp): #incorporate and expand
    
    inp = inp.title()
    
    return inp
    



