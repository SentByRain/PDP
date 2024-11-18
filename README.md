# PDP

## backend

1. Установить Docker Desktop
2. Установка Docker compose (если не ставится с Docker Desktop)
3. Запуск контейнеров с сервером, postgress и pgadmin
   Запустить Docker Desktop, затем выполнить команды:

```sh
cd backend
docker-compose up --build
```

4. Swager будет доступен по адресу http://localhost:8000/docs или http://0.0.0.0:8000/docs

5. Для того, чтобы завершить работу ввести команду

```sh
docker-compose down --volumes
```
