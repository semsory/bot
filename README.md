# ToDo List App (Flask)

Простое и удобное веб-приложение для управления списком задач, созданное на Flask. Позволяет добавлять, редактировать, отмечать как выполненные и удалять задачи.

## Быстрый старт

### 1. Клонирование репозитория
```bash
git clone https://github.com
cd todo-list-flask
```

### 2. Настройка виртуального окружения
```bash
python -m venv venv
```
* **Linux/macOS:**
```bash
source venv/bin/activate
```
* **Windows:**
```bash
venv\Scripts\activate
```

### 3. Установка зависимостей
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Настройка переменных окружения
Создайте файл `.env` в корневой директории:
```env
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-super-secret-key
DATABASE_URL=sqlite:///todo.db
```

### 5. Инициализация базы данных (если требуется)
Если вы используете Flask-Migrate, выполните:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

### 6. Запуск приложения
```bash
flask run
```
Приложение будет доступно по адресу: **http://127.0.0.1:5000**

## Структура проекта
```text
todo-list-flask/
├── app/
│   ├── __init__.py      # Инициализация Flask-приложения и БД
│   ├── routes.py        # Маршруты (просмотр, добавление, удаление задач)
│   ├── models.py        # Модель задачи (Task) для базы данных
│   ├── templates/
│   │   ├── base.html    # Базовый шаблон
│   │   └── index.html   # Главная страница со списком задач
│   └── static/
│       ├── css/
│       │   └── style.css # Стили интерфейса
│       └── js/
├── .env                 # Конфигурация окружения
├── .gitignore
├── requirements.txt     # Зависимости проекта
└── run.py               # Точка запуска приложения
```

## Основной функционал
* ➕ Создание новых задач с описанием и дедлайнами.
* ✔️ Изменение статуса задачи (выполнено / не выполнено).
* ❌ Удаление и редактирование существующих задач.
* 💾 Сохранение данных в локальную базу данных SQLite.

## Используемые технологии
* **Python**
* **Flask** (веб-фреймворк)
* **Flask-SQLAlchemy** (работа с базой данных)
* **SQLite** (СУБД)
* **HTML5 / CSS3** (интерфейс)
