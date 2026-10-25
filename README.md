# Life Stats

Минимальный каркас: FastAPI + Vue 3 (JavaScript, Vite).

## Структура

```text
backend/
  main.py          # запуск из backend: python main.py
  requirements.txt # зависимости backend
  app/
    main.py        # приложение FastAPI
    api/routes.py  # маршруты API
frontend/
  src/App.vue      # стартовая страница и проверка API
  src/api.js       # HTTP-запросы
  vite.config.js   # прокси /api на FastAPI
```

## Запуск

Требуются Python 3.10+ и Node.js 20.19+ (для Node 22 — 22.12+).
Откройте два терминала из корня проекта. Backend запускается из папки
`backend`, frontend — из `frontend`.

Если `.venv` ещё нет, один раз создайте окружение из корня проекта:

```bash
python3 -m venv .venv
```

Backend, первый терминал (macOS/Linux):

```bash
cd backend
source ../.venv/bin/activate
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

Виртуальное окружение `.venv` хранится в корне проекта.
В PyCharm выберите Script path: `backend/main.py`, Working directory: папка
`backend`, интерпретатор: `.venv/bin/python` из корня проекта.

ASGI-приложение при рабочем каталоге `backend` — `main:app`
(также подходит `app.main:app`).
При наличии `PORT` сервер слушает `0.0.0.0:$PORT` без autoreload;
без этой переменной сохраняется локальный режим на `127.0.0.1:8000`.
Новые зависимости добавляйте в `backend/requirements.txt`.

## Сборка frontend

Из папки `frontend`:

```bash
npm run build
```

Результат — `frontend/dist`. В production веб-сервер должен раздавать эту
папку и перенаправлять `/api` в FastAPI; прокси Vite используется только в разработке.

База данных, авторизация и предметные сущности пока не добавлены.
