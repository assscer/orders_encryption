# Python Test Task

Это тестовое задание для демонстрации функционала, включающего регистрацию, логин, управление заказами с кешированием и логированием. Проект использует FastAPI для создания REST API, SQLAlchemy для работы с базой данных, а также Redis для кеширования.

## Требования

Для запуска проекта вам нужно:

- Python 3.10+
- PostgreSQL
- Redis
- Установленные зависимости из `requirements.txt`

### Установка зависимостей

1. Клонируйте репозиторий:

```bash
git clone https://github.com/assscer/orders_encryption.git
cd python_test_task

pip install -r requirements.txt
```

### Настройка базы данных и Redis
- 1. Создайте базу данных в PostgreSQL:

   Откройте PostgreSQL и выполните:
   ```bash
   psql -U postgres
   CREATE DATABASE your_db_name;
   ```
- 2. Запустите Redis с использованием Docker:

Если у вас установлен Docker, используйте этот файл docker-compose.yml для запуска Redis:

    docker-compose up -d redis

- 3. Запуск приложения
Для запуска приложения выполните следующую команду:
```bash
uvicorn app.main:app --reload
```
- Сервер будет доступен по адресу http://127.0.0.1:8000.



### Тестирование
Для тестирования API используйте Postman или Swagger UI, который доступен по адресу: http://127.0.0.1:8000/docs.

Запросы для тестирования:

- POST /auth/register – создание нового пользователя.
- POST /auth/login – авторизация и получение токена.
- POST /orders/ – создание заказа.
- GET /orders/{order_id} – получение заказа.
- PUT /orders/{order_id} – обновление заказа.
- DELETE /orders/{order_id} – удаление заказа.
## Примечания

Все операции с заказами кешируются, чтобы ускорить повторяющиеся запросы.
Для работы с данными используется PostgreSQL, а Redis — для кеширования.