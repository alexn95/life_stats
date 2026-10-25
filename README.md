# Life Stats

Минимальный каркас: FastAPI + Vue 3 (JavaScript, Vite).

## Структура

```text
backend/
  main.py          # запуск из backend: python main.py
  requirements.txt # зависимости backend
  .env.example     # пример настройки CORS
  app/
    main.py        # приложение FastAPI
    api/routes.py  # маршруты API
frontend/
  src/App.vue      # стартовая страница и проверка API
  src/api.js       # HTTP-запросы
  vite.config.js   # прокси /api на FastAPI
  .env.example     # пример адреса backend
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
Для этого режима `.env` не требуется.

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

Результат — `frontend/dist`. Эту папку публикуйте на хостинге frontend.
Прокси Vite используется только в разработке.

## Frontend и backend на разных доменах

Например, frontend доступен по `https://app.example.com`, backend —
по `https://api.example.com`.

На хостинге frontend задайте переменную **до сборки**:

```dotenv
API_BASE_URL=https://api.example.com
```

Указывайте адрес backend без `/api`: код сам добавит `/api/health`.
Затем выполните `npm ci` и `npm run build` из папки `frontend`.
Переменная встраивается в JavaScript при сборке; после смены адреса
нужно пересобрать и опубликовать frontend. `VITE_*` видны посетителям,
поэтому в них нельзя хранить секреты.

На хостинге backend задайте адрес frontend:

```dotenv
CORS_ALLOW_ORIGINS=https://app.example.com
```

Для нескольких адресов перечислите их через запятую. Указывайте только
origin: протокол, домен и порт при необходимости, без пути.
После изменения перезапустите backend. CORS разрешает браузерные запросы
с указанных адресов; это не заменяет авторизацию API.
Оба публичных адреса должны использовать HTTPS.

Вместо переменных хостинга можно создать `frontend/.env.production`
с `API_BASE_URL` для сборки и `backend/.env` с `CORS_ALLOW_ORIGINS`
для сервера. Backend загружает свой `.env` автоматически, а переменные
окружения хостинга имеют приоритет. Эти файлы исключены из Git;
примеры настроек находятся в `.env.example` каждой папки.

Для локального подключения напрямую, без прокси, создайте `frontend/.env.local`:

```dotenv
API_BASE_URL=http://127.0.0.1:8000
```

Перезапустите Vite после изменения env-файла. Локальные origins
`http://127.0.0.1:5173` и `http://localhost:5173` разрешены backend по умолчанию,
если `CORS_ALLOW_ORIGINS` не задана. Пустая `API_BASE_URL` сохраняет
прежнюю работу через `/api` и прокси Vite.

Подробнее: [env-переменные Vite](https://vite.dev/guide/env-and-mode),
[CORS в FastAPI](https://fastapi.tiangolo.com/tutorial/cors/).

База данных, авторизация и предметные сущности пока не добавлены.
