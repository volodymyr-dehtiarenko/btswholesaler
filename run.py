import json
import requests

URL_PRODUCTS = 'https://api.btswholesaler.com/v1/api/getListProducts'
URL_SANDBOX  = 'https://apidev.btswholesaler.com/v1/api/getListProducts'
TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsInN1YiI6OTc2MzU2LCJpYXQiOjE2NzcxODM5MDZ9.CZk2L11F2LdqSO5Ww8ALKJjJcINQWpVN4t9Q4EjY-NA"



class ApiBTS():
    """ Connection to ApiBTS products"""

    def api_conn():
        head = {'Authorization': "Bearer {}".format(TOKEN)}
        connect = requests.get(URL_PRODUCTS, headers=head)
        if connect.status_code == 200:
            print("Connection to BTS API - OK!", connect)


    def api_productCRUD():
        pass

    def item_adding():
        pass

if __name__ == '__main__':
    ApiBTS.api_conn()
    
    









    # def run_api():
    #     product_info = requests.get(url_product, headers=head)
    #     if product_info.status_code == 200:
    #         for prod in product_info:
    #             print(prod)
    






  