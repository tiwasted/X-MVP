# Используйте официальный образ PostgreSQL как базовый
FROM postgres:latest

# Копируйте дамп данных в папку инициализации
COPY alldata.sql /docker-entrypoint-initdb.d/
