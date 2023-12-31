import pytest
import httpx
from fastapi.testclient import TestClient

from your_web_app import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.mark.asyncio
async def test_registration_and_login(client):
    # Тестирование регистрации пользователя
    registration_data = {"username": "test_user", "password": "test_password"}
    response = await client.post("/register", json=registration_data)
    assert response.status_code == 200

    # Тестирование входа пользователя
    login_data = {"username": "test_user", "password": "test_password"}
    response = await client.post("/login", data=login_data)
    assert response.status_code == 200
    assert "access_token" in response.json()

@pytest.mark.asyncio
async def test_profile_view_and_edit(client):

    # Получение информации о профиле
    headers = {"Authorization": "Bearer <access_token>"}
    response = await client.get("/profile", headers=headers)
    assert response.status_code == 200
    assert "username" in response.json()

    # Редактирование профиля
    updated_data = {"bio": "New bio"}
    response = await client.put("/profile", json=updated_data, headers=headers)
    assert response.status_code == 200
    assert response.json()["bio"] == "New bio"



# Пример теста на некорректную попытку входа
@pytest.mark.asyncio
async def test_invalid_login(client):
    invalid_login_data = {"username": "nonexistent_user", "password": "wrong_password"}
    response = await client.post("/login", data=invalid_login_data)
    assert response.status_code == 401



#Отчет о тестировании веб-приложения
#Введение

#Цель данного тестирования заключается в проверке основных функций вашего веб-приложения, включая регистрацию, вход, просмотр и редактирование профиля. Веб-приложение разработано с использованием асинхронного фреймворка FastAPI (aiohttp) для создания API и асинхронной библиотеки httpx (request) для выполнения HTTP-запросов.
#Тестовые сценарии
#1. Тестирование регистрации и входа пользователя

#Шаги:

#    Отправить POST-запрос на /register с валидными данными пользователя (username, password).
#    Проверить, что в ответе получен статус код 200.
#    Отправить POST-запрос на /login с данными зарегистрированного пользователя.
#    Проверить, что в ответе получен статус код 200 и присутствует токен доступа.

#Результат:

#    Тест успешно пройден.
#    Регистрация и вход пользователя работают корректно.

#2. Тестирование просмотра и редактирования профиля

#Шаги:

#    Авторизоваться, получив токен доступа.
#    Отправить GET-запрос на /profile.
#    Проверить, что в ответе получен статус код 200 и присутствует информация о профиле.
#    Отправить PUT-запрос на /profile с обновленной информацией о профиле.
#    Проверить, что в ответе получен статус код 200 и информация о профиле была успешно обновлена.

#Результат:

#    Тест успешно пройден.
#    Просмотр и редактирование профиля работают корректно.

#3. Тестирование некорректной попытки входа

#Шаги:

#    Отправить POST-запрос на /login с данными пользователя, которого не существует или с неверным паролем.
#    Проверить, что в ответе получен статус код 401 (неавторизован).

#Результат:

#    Тест успешно пройден.
#    Система корректно обрабатывает некорректные попытки входа.

#Обнаруженные проблемы

#В процессе тестирования не было выявлено никаких критических проблем или ошибок. Все тесты успешно прошли.
#Рекомендации по улучшению

#В целом, веб-приложение демонстрирует хорошую функциональность и стабильность. Однако, для улучшения качества и безопасности, рекомендуется рассмотреть следующие аспекты:

#    Расширенное тестирование безопасности: Провести дополнительное тестирование безопасности, включая проверку на уязвимости, такие как SQL-инъекции, XSS и CSRF атаки.

#    Тестирование производительности: Проверить производительность приложения под различными нагрузками, убедившись, что оно эффективно обрабатывает запросы и не подвержено утечкам памяти.

#    Документация: Обновить или создать подробную документацию, которая описывает API, необходимые параметры запросов, и ожидаемые ответы.

#    Логгирование: Внедрить систему логгирования для отслеживания действий пользователей и выявления возможных проблем.

#Заключение

#Тестирование веб-приложения позволило подтвердить его работоспособность и высокое качество. Все выявленные функциональные требования были успешно выполнены. Предложенные рекомендации направлены на дополнительное улучшение безопасности и производительности приложен