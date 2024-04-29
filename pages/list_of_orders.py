import requests
import data


class ListOfOrders:


    def get_orders(self):
        response = requests.get(data.GET_ORDER_URL)
        r = response.json()
        return r


