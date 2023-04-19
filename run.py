from setting import TOKEN, URL_PRODUCTS
import json, requests, pickle
import simplejson
from datetime import date



class ApiIntegrate:
    """API Integration to database""" 

    # def __init__(self, apidata):
    #     self.apidata = apidata
        
    def api_connection():
        head = {'Authorization': "Bearer {}".format(TOKEN)}
        apidata = requests.get(URL_PRODUCTS, headers=head)
        if apidata.status_code == 200:
            print("Connection to BTS API - OK!")
        return apidata
    
    def data_download():
        today = date.today()
        file_name = date.isoformat(today)
        try:
            with open('product_'+ file_name +'.json', "wb") as fp:
                json.dump(apidata, fp)
                print("File is ready - OK!")
        except TypeError:
            print("Sorry file not writening - NO!")
        finally:
            print("test")
    
    
    def db_connection():
        pass

    
    
    def data_integration():
        pass

    
    
    def data_update():
        pass













  