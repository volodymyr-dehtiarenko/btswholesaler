import json
import requests

URL_PRODUCTS = 'https://api.btswholesaler.com/v1/api/getListProducts'
URL_SANDBOX  = 'https://apidev.btswholesaler.com/v1/api/getListProducts'
TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsInN1YiI6OTc2MzU2LCJpYXQiOjE2NzcxODM5MDZ9.CZk2L11F2LdqSO5Ww8ALKJjJcINQWpVN4t9Q4EjY-NA"


def api_connect():
    head = {'Authorization': "Bearer {}".format(TOKEN)}
    _connect = requests.get(URL_PRODUCTS, headers=head)
    if _connect.status_code == 200:
        print("Connection to BTS API - OK!", _connect)
    return _connect


def api_productCRUD(**kwargs):
    for item in api_connect():
        # data = json.loads(item)
        print(json.loads(item))



if __name__ == '__main__':
    #api_connect()
    api_productCRUD()

    
    









    # def run_api():
    #     product_info = requests.get(url_product, headers=head)
    #     if product_info.status_code == 200:
    #         for prod in product_info:
    #             print(prod)
    






  