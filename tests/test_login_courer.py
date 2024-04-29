from pages.login_courer import CourerLogIn
from unittest.mock import patch
import data
import pytest
import allure

class TestCourerLogIn(CourerLogIn):
    @allure.description('Курьер может авторизоваться и Для авторизации нужно передать все обязательные поля')
    @patch('pages.main.Main.register_new_courier_and_return_login_password', return_value = data.login_pass_correct)
    def test_courer_authorization_after_creation_success(self, mock_payload):
        response = self.courer_authorization_after_creation()
        assert response.status_code == 200

    @allure.description('Авторизация без логина или пароля')
    @patch('pages.main.Main.register_new_courier_and_return_login_password')
    @pytest.mark.parametrize('value', [data.login_no_login, data.login_no_pass])
    def test_authorization_no_login_or_pass_fail(self, mock_payload, value):
            mock_payload.return_value = value
            response = self.courer_authorization_after_creation()
            assert response.status_code == 400

    @allure.description('Система вернёт ошибку, если неправильно указать логин или пароль')
    @patch('pages.main.Main.register_new_courier_and_return_login_password')
    @pytest.mark.parametrize('value', [data.login_wrong_login, data.login_wrong_pass, data.login_wrong_login_and_pass])
    def test_courer_authorization_wrong_login_or_pass_fail(self, mock_payload, value):
        mock_payload.return_value = value
        response = self.courer_authorization_after_creation()
        assert response.text == data.ERROR_BY_LOGIN_PASS_NOT_EXIST

    @allure.description('Если какого-то поля нет, запрос возвращает ошибку')
    @patch('pages.main.Main.register_new_courier_and_return_login_password')
    @pytest.mark.parametrize('value', [data.login_no_login, data.login_no_pass])
    def test_authorization_no_login_or_pass_error_text_return(self, mock_payload, value):
            mock_payload.return_value = value
            response = self.courer_authorization_after_creation()
            assert response.text == data.ERROR_BY_LOGIN_PASS_NOT_ENTERED

    @allure.description('Если авторизоваться под несуществующим пользователем, запрос возвращает ошибку')
    @patch('pages.main.Main.register_new_courier_and_return_login_password', return_value = data.login_doesnt_exist)
    def test_authorization_authorization_with_login_doesnt_exist(self, mock_payload):
            response = self.courer_authorization_after_creation()
            assert response.text == data.ERROR_BY_LOGIN_PASS_NOT_EXIST

    @allure.description('Успешный запрос возвращает id')
    @patch('pages.main.Main.register_new_courier_and_return_login_password', return_value = data.login_pass_correct)
    def test_courer_authorization_id_returns(self, mock_payload):
        response = self.courer_authorization_after_creation()
        assert "id" in response.text
