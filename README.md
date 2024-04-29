# Sprint_7

Не работает запуск тестов через pytest, как результ - не запустить Allure.
Что-то не так с названиями модулей? 

Почему при запуке тестов через терминал ошибки?

pytest tests\test_create_courer.py --alluredir=allure_results 



Hint: make sure your test modules/packages have valid Python names.
Traceback:
..\AppData\Local\Programs\Python\Python311\Lib\importlib\__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
tests\test_create_courer.py:2: in <module>
    import data
E   ModuleNotFoundError: No module named 'data'


pytest tests\test_create_courer.py --alluredir=allure_results 



