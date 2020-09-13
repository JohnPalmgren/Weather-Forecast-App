#https://www.metoffice.gov.uk/services/data/datapoint/api-reference
import urllib.request
import json


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
        
        return [time for time in steps]

    def get_data_from_api(self, site_id):
        
        #try:
        data = self.api_connect(f'val/wxfcs/all/json/{site_id}?res=3hourly&')
        filtered = data['SiteRep']['DV']['Location']['Period']
               
        codes = [data['Rep'] for data in filtered]
        dates = [data['value'] for data in filtered]
        temp = []
        weather = []
        
        for i in codes:
            temp_itr = [t['T'] for t in i]
            weather_itr = [w['W'] for w in i]
            temp.append(temp_itr)
            weather.append(weather_itr)
            
        #all_days = {dates[i] : [temp[i], weather[i]] for i in range(len(dates))}
            
        return [dates, temp, weather]
        
