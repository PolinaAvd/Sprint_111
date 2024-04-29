from pages.list_of_orders import ListOfOrders
import allure


class TestListOfOrders(ListOfOrders):

    @allure.description('В тело ответа возвращается список заказов')
    def test_list_of_orders_consist_lists(self):
        response = self.get_orders()
        assert type(response) == dict and "orders" in response



