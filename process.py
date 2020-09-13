import time

import api # for testing
APIkey = '940b74af-8410-4516-9326-e39b07de8cdd'
interface = api.API(APIkey)
site_id = interface.get_site_id_from_user_input('London')
dic = interface.get_data_from_api(site_id)


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


def split_lists(lists, items):
    
    new_list = []
    for num in range(items):
        for lst in lists:
            new_list.append(lst[num])

    return new_list

def time_intervals(items):
    
    times = ['00:00','21:00','18:00', '15:00', '12:00', '9:00', '6:00', '3:00']
    selection = times[:items]
    
    return selection[::-1]
    

def user_input(inp):
    
    inp = inp.title()
    
    return inp
    

