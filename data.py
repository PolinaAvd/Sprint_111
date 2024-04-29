import allure

CREATE_COURER_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/courier'
LOGIN_COURER_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/courier/login'
CREATE_ORDER_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'
GET_ORDER_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/orders'

ERROR_BY_LOGIN_PASS_NOT_EXIST = '{"code":404,"message":"Учетная запись не найдена"}'
ERROR_BY_LOGIN_PASS_NOT_ENTERED = '{"code":400,"message":"Недостаточно данных для входа"}'

login_pass_correct = ['Courercreated454', '6666556565656']
login_no_login = ['', '6666556565656']
login_no_pass = ['Courercreated454', '']
login_wrong_login = ['Courercreated45', '6666556565656']
login_wrong_pass = ['Courercreated454', '666']
login_wrong_login_and_pass = ['Courercreated45', '666']
login_doesnt_exist = ['C', '666']
registration_no_data = {
            "login": '',
            "password": '',
            "firstName": ''
        }

order_param_black = {
    "firstName": "Narutou",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2025-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
    ]
}

order_param_grey = {
    "firstName": "Narutou",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2025-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "GREY"
    ]
}

order_param_black_and_grey = {
    "firstName": "Narutou",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2025-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK", "GREY"
    ]
}

order_param_no_color = {
    "firstName": "Narutou",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2025-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
    ]
}