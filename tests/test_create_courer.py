import pytest
import data
from pages.create_courer import CreateCourer
import allure

class TestCreateCourer(CreateCourer):

    @allure.description('Курьер может быть создан')
    def test_creation_of_a_new_courer(self):
        response = self.courer_can_be_created()
        assert len(response) == 3

    @allure.description('Нельзя создать двух одинаковых курьеров')
    def test_creation_of_doubled_courer_impossible(self):
        response = self.creation_of_doubled_courer()
        assert response == 409

    @allure.description('Чтобы создать курьера, нужно передать в ручку все обязательные поля')
    @pytest.mark.parametrize('payload', [data.registration_no_data])
    def test_creation_of_the_courer_no_data_fail(self, payload):
        response = self.creation_of_the_courer_no_data(payload)
        assert response.status_code == 400

    @allure.description('Запрос возвращает правильный код ответа')
    def test_creation_of_a_new_courer_corect_code(self):
        response = self.creation_of_a_new_courer()
        assert response.status_code == 201

    @allure.description('Запрос возвращает правильный текст ответа')
    def test_creation_of_a_new_courer_corect_response(self):
        response = self.creation_of_a_new_courer()
        assert response.text == '{"ok":true}'

    @allure.description('Если нет логина, запрос возвращает ошибку')
    def test_creation_of_the_courer_no_login_fail(self):
        response = self.creation_of_the_courer_no_login()
        assert response == 400

    @allure.description('Если нет пароля, запрос возвращает ошибку')
    def test_creation_of_the_courer_no_password_fail(self):
        response = self.creation_of_the_courer_no_password()
        assert response == 400

    @allure.description('Если нет имени, запрос отрабатывает успешно - БАГ, по докумендации поле firstname е является опциоанальным')
    def test_creation_of_the_courer_no_firstname_success(self):
        response = self.creation_of_the_courer_no_firstname()
        assert response == 201

    @allure.description('Если создать пользователя с логином, который уже есть, возвращается ошибка')
    def test_creation_of_doubled_login_courer_fail(self):
        response = self.creation_of_doubled_login_courer()
        assert response == 409





