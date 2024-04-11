# Используйте официальный образ Python как базовый
FROM python:3.9

# Установите рабочую директорию в контейнере
WORKDIR /app

# Копируйте файл зависимостей первым, чтобы воспользоваться кэшированием Docker
COPY requirements.txt /app/

# Установка зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копируйте весь проект в рабочую директорию
COPY xmvp/ /app/

# Запускаем сервер разработки Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
