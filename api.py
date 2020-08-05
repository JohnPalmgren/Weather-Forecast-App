#https://www.metoffice.gov.uk/services/data/datapoint/api-reference
import urllib.request
import json


APIkey = '940b74af-8410-4516-9326-e39b07de8cdd'


#http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/capabilities?res=3hourly&key=01234567-89ab-cdef-0123-456789abcde

class API():
    """Interact with the Met Office API"""
    
    def __init__(self,key):
        self.key = key
        self.sites = self.get_sites_from_api()

    def api_connect(self, resource):
    
        baseurl = f'http://datapoint.metoffice.gov.uk/public/data/{resource}key={self.key}'
        url = urllib.request.urlopen(baseurl)
        url_data = url.read().decode()
        data = json.loads(url_data)
        
        return data

    def get_sites_from_api(self):
        
        return self.api_connect('val/wxfcs/all/json/sitelist?')
    
    def get_site_id_from_user_input(self, user_input):
        
        locations = self.sites['Locations']['Location']
        
        for values in locations:
            if values['name'] == user_input:
                return (values['id'])
            
    def get_timestamp(self):
        
        timestamp = self.api_connect('val/wxfcs/all/json/capabilities?res=3hourly&')
        steps = timestamp['Resource']['TimeSteps']['TS']
        

        #return [time[11:16] for time in steps]
        return [time for time in steps]

    
    def get_data_from_api(self, site_id):
        
        try:
            data = self.api_connect(f'val/wxfcs/all/json/{site_id}?res=3hourly&')
            filtered = data['SiteRep']['DV']['Location']['Period']
            
            codes = [i['Rep'] for i in filtered]
            temp = []
            weather = []

            for day in codes:
                for hours in day:
                    temp.append(hours['T'])
                    weather.append(hours['W'])
                
            #return filtered       
            return [temp, weather]
        
        except:
            print('Place not known. Enter the name of a UK town or city')
            

APIkey = '940b74af-8410-4516-9326-e39b07de8cdd'
interface = API(APIkey)

site_id = interface.get_site_id_from_user_input('London')

print (interface.get_timestamp())
print (interface.get_data_from_api(site_id))

print (len(interface.get_timestamp()))
print (len(interface.get_data_from_api(site_id)[0]))
