# NONPRO — Система управления пекарней

PWA-приложение для продажи хлеба и управления кассой.

## Технологии

- **Backend:** Python, FastAPI, SQLAlchemy, JWT
- **Frontend:** React.js, Vite, Recharts
- **Database:** SQLite (dev) / PostgreSQL (prod)
- **PWA:** Service Worker, Manifest, Offline Support

## Быстрый старт

### Backend

```bash
cd backend
python -m venv venv
.\venv\Scripts\activate    # Windows
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Откройте http://localhost:3000

### Вход по умолчанию

- **Логин:** admin
- **Пароль:** admin123

## Docker

```bash
docker-compose up -d
```

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- Swagger: http://localhost:8000/docs

## API Endpoints

| Метод | Путь | Описание |
|-------|------|----------|
| POST | /api/auth/login | Авторизация |
| GET | /api/auth/me | Текущий пользователь |
| GET | /api/products | Список товаров |
| POST | /api/sales | Создать продажу |
| GET | /api/sales | История продаж |
| GET | /api/reports/summary | Отчёт за период |
| GET | /api/reports/dashboard | Статистика за сегодня |
| GET/POST | /api/expenses | Расходы |
| GET/POST | /api/users | Пользователи (admin) |

## Структура проекта

```
non/
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── database/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── routers/
│   │   ├── services/
│   │   └── dependencies/
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── api/
│   │   ├── components/
│   │   ├── context/
│   │   ├── pages/
│   │   └── App.jsx
│   ├── public/
│   │   ├── manifest.json
│   │   └── sw.js
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```
