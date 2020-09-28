# import api

# APIkey = '940b74af-8410-4516-9326-e39b07de8cdd'
# interface = api.API(APIkey)


# def api_data(user_input):
#     """Return a list of date, temperature list and weather code list for five days.
#     user_input(str): Name of a location in the UK.     
#     """
    
#     siteid = interface.get_site_id_from_user_input(user_input)
#     api_data = interface.get_data_from_api(siteid)
#     data = split_lists(api_data, 5)
    
#     return data


# def split_lists(lists, items):
#     """Create a new list from a collection of lists where the nth item in each
#     list becomes a new list.
#     lists(list)
#     items(int): Number of elements in the lists.
#     """
    
#     new_list = []
#     for num in range(items):
#         for lst in lists:
#             new_list.append(lst[num])

#     return new_list
