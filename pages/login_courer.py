from pages.main import Main
import requests
import data


class CourerLogIn():


    def courer_authorization_after_creation(self):
        response = Main()
        saved_data = response.register_new_courier_and_return_login_password()
        payload = {
            "login": saved_data[0],
            "password": saved_data[1]
        }
        response = requests.post(data.LOGIN_COURER_URL, data=payload)
        return response



