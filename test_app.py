import unittest
from app import app  # Импортируем ваше приложение


class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        #     Создаем тестовый клиент
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_world(self):
        # Отправляем GET-запрос к корневому URL
        response = self.app.get('/')
        # Проверяем, что статус-код ответа 200
        self.assertEqual(response.status_code, 200)
        # Проверяем, что текст ответа содержит "Hello, World!"
        self.assertIn(b'Hello, World!', response.data)


if __name__ == '__main__':
    unittest.main()
