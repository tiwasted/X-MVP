# Используйте официальный образ PostgreSQL как базовый
FROM postgres:latest

# Устанавливаем рабочую директорию в контейнере
WORKDIR /docker-entrypoint-initdb.d

# Копируйте дамп данных в папку инициализации
COPY all_data.sql /docker-entrypoint-initdb.d/
