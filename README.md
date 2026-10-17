# Flask Project Name

## Быстрый старт

### 1. Клонирование репозитория
```bash
git clone https://github.com
cd your-repo-name
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
Создайте файл `.env`:
```env
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-super-secret-key
```

### 5. Запуск приложения
```bash
flask run
```
Адрес: http://127.0.0.1:5000

## Структура проекта

```text
your-repo-name/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── templates/
│   └── static/
├── .env
├── .gitignore
├── requirements.txt
└── run.py
```

## Используемые технологии
* Python
* Flask
