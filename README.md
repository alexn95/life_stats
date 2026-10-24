# Life Stats

Минимальный каркас: FastAPI + Vue 3 (JavaScript, Vite).

## Структура

```text
backend/app/
  main.py          # приложение FastAPI
  api/routes.py    # маршруты API
frontend/
  src/App.vue      # стартовая страница и проверка API
  src/api.js       # HTTP-запросы
  vite.config.js   # прокси /api на FastAPI
main.py            # запуск backend из корня проекта или PyCharm
requirements.txt
```

## Запуск

Требуются Python 3.10+ и Node.js 20.19+ (для Node 22 — 22.12+).
Все команды ниже выполняются из корня проекта, если не указано иначе.

Backend, первый терминал (macOS/Linux):

```bash
python3 -m venv .venv  # только если окружение ещё не создано
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

Frontend, второй терминал:

```bash
cd frontend
npm ci
npm run dev
```

- Приложение: http://127.0.0.1:5173
- Swagger: http://127.0.0.1:8000/docs
- Проверка API: http://127.0.0.1:8000/api/health → `{"status":"ok"}`

Vite перенаправляет запросы `/api` к backend на порт 8000.
При запуске обоих серверов на странице появляется «API подключён».

## Сборка frontend

```bash
cd frontend
npm run build
```

Результат — `frontend/dist`. В production веб-сервер должен раздавать эту
папку и перенаправлять `/api` в FastAPI; прокси Vite используется только в разработке.

База данных, авторизация и предметные сущности пока не добавлены.
