# Sentiment Analysis Service

Проект для определения тональности текста (позитив/негатив) с использованием предобученной модели трансформеров. Состоит из backend на FastAPI и frontend на Streamlit.

---

## Требования

- Python 3.9+
- pip

---

## Установка

### 1. Клонируйте репозиторий

```bash
git clone <repository_url>
cd <project_folder>
```

### 2. Создайте виртуальные окружения

```bash
# Backend
python -m venv backend/.venv
source backend/.venv/bin/activate  # Linux/Mac
# или
backend\.venv\Scripts\activate  # Windows

# Установите зависимости
pip install -r backend/requirements.txt
deactivate

# Frontend
python -m venv frontend/.venv
source frontend/.venv/bin/activate  # Linux/Mac
# или
frontend\.venv\Scripts\activate  # Windows

# Установите зависимости
pip install -r frontend/requirements.txt
deactivate
```

### Пример `backend/requirements.txt`

```
fastapi==0.115.0
uvicorn==0.30.0
transformers==4.41.0
torch==2.3.0
pydantic==2.7.0
```

### Пример `frontend/requirements.txt`

```
streamlit==1.35.0
requests==2.32.0
```

---

## Запуск

### Запуск backend (FastAPI)

```bash
source backend/.venv/bin/activate  # или activate для Windows
uvicorn backend.main:app --host 127.0.0.1 --port 8000
```

Backend доступен по адресу: `http://127.0.0.1:8000`  
Документация API: `http://127.0.0.1:8000/docs`

### Запуск frontend (Streamlit)

```bash
source frontend/.venv/bin/activate  # или activate для Windows
streamlit run frontend/app.py --server.port 8501
```

Frontend доступен по адресу: `http://127.0.0.1:8501`

---

## Использование

1. Запустите backend и frontend (в отдельных терминалах)
2. Откройте `http://127.0.0.1:8501` в браузере
3. Введите текст в поле ввода
4. Нажмите «Анализировать»
5. Получите результат: позитив/негатив и оценку уверенности

---

## API эндпоинты

| Метод | Путь | Описание |
|-------|------|----------|
| GET | `/` | Проверка работоспособности |
| GET | `/{text}` | Анализ тональности через URL-параметр |
| POST | `/predict` | Анализ тональности через JSON `{"text": "..."}` |

Пример запроса:

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"text": "I love this product"}'
```

Ответ:

```json
[{"label": "POSITIVE", "score": 0.9998}]
```

---

## Примечания

- Первая загрузка модели может занять несколько минут (скачивание весов ~100-400 MB)
- Для работы требуется интернет при первом запуске (если модель не закеширована)
- Проект предназначен для демонстрации и локального использования

---

## Лицензия

MIT