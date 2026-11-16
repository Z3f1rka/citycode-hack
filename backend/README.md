### 1. Установить зависимости
```bash
uv sync
```
### 2. Настроить окружение
```bash
cp .env.template .env
```

### 3. Применить миграции БД
```bash
uv run alembic upgrade head
```
### 4. Запустить сервер
```bash
uv run uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
http://localhost:8000/docs