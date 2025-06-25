# 🔧 Установка для разработчиков

Подробное руководство по установке и настройке AI Telegram Bot для разработчиков! 🚀

## 📋 Требования

### Системные требования
- **Python**: 3.8 или выше
- **ОС**: Windows 10+, macOS 10.14+, Ubuntu 18.04+
- **RAM**: Минимум 512MB (рекомендуется 1GB+)
- **Дисковое пространство**: 100MB свободного места

### Необходимые инструменты
- **Git** - для клонирования репозитория
- **pip** - менеджер пакетов Python
- **Текстовый редактор** - VS Code, PyCharm, Sublime Text
- **Terminal/Command Prompt** - для выполнения команд

---

## 🚀 Быстрая установка

### 1. Клонирование репозитория
```bash
git clone https://github.com/your-username/tbotik.git
cd tbotik
```

### 2. Создание виртуального окружения
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 4. Настройка переменных окружения
```bash
# Копируем пример файла
cp env.example .env

# Редактируем .env файл
# Добавляем реальные токены
```

### 5. Запуск бота
```bash
python bot.py
```

---

## 🔑 Получение API ключей

### Telegram Bot Token
1. Откройте Telegram и найдите @BotFather
2. Отправьте команду `/newbot`
3. Следуйте инструкциям:
   - Введите имя бота (например: "My AI Assistant")
   - Введите username (например: "my_ai_bot")
4. Скопируйте полученный токен

### OpenRouter API Key
1. Зарегистрируйтесь на [openrouter.ai](https://openrouter.ai)
2. Перейдите в раздел API Keys
3. Создайте новый ключ
4. Скопируйте API ключ

### NeuroImg API Key
1. Зарегистрируйтесь на [neuroimg.art](https://neuroimg.art)
2. В личном кабинете найдите API ключ
3. Скопируйте ключ

---

## ⚙️ Конфигурация

### Структура .env файла
```env
# Telegram Bot Token
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here

# OpenRouter API Key для нейросети
OPENROUTER_API_KEY=your_openrouter_api_key_here

# NeuroImg API Key для генерации изображений
NEUROIMG_API_KEY=your_neuroimg_api_key_here
```

### Проверка конфигурации
```python
from config import проверить_токены

# Проверяем, что все токены настроены
if проверить_токены():
    print("✅ Все токены настроены правильно")
else:
    print("❌ Некоторые токены не настроены")
```

---

## 🧪 Тестирование

### Проверка установки
```bash
# Проверяем версию Python
python --version

# Проверяем установленные пакеты
pip list

# Запускаем тестовый запуск
python -c "import telebot; print('✅ pyTelegramBotAPI установлен')"
```

### Тестирование API
```python
# Тест OpenRouter API
import requests
import json

def test_openrouter():
    response = requests.post(
        'https://openrouter.ai/api/v1/chat/completions',
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "qwen/qwq-32b:free",
            "messages": [{"role": "user", "content": "Привет!"}]
        }
    )
    return response.status_code == 200

# Тест NeuroImg API
def test_neuroimg():
    response = requests.post(
        'https://neuroimg.art/api/v1/free-generate',
        json={
            "token": NEUROIMG_API_KEY,
            "prompt": "test",
            "stream": False
        }
    )
    return response.status_code == 200
```

---

## 🔧 Разработка

### Структура проекта для разработки
```
tbotik/
├── bot.py                 # Основной файл бота
├── config.py              # Конфигурация
├── requirements.txt       # Зависимости
├── requirements-dev.txt   # Зависимости для разработки
├── .env                   # Переменные окружения
├── .env.example           # Пример переменных
├── .gitignore             # Исключения Git
├── images/                # Папка для сохранения изображений
│   └── .gitkeep           # Сохраняет папку в Git
├── tests/                 # Тесты
│   ├── test_bot.py
│   ├── test_config.py
│   └── test_api.py
├── docs/                  # Документация
└── scripts/               # Скрипты для разработки
    ├── setup.sh
    └── deploy.sh
```

### Зависимости для разработки
Создайте файл `requirements-dev.txt`:
```
-r requirements.txt
pytest
pytest-asyncio
pytest-cov
black
flake8
mypy
pre-commit
```

### Установка зависимостей для разработки
```bash
pip install -r requirements-dev.txt
```

---

## 🧪 Тестирование

### Запуск тестов
```bash
# Запуск всех тестов
pytest

# Запуск с покрытием
pytest --cov=.

# Запуск конкретного теста
pytest tests/test_bot.py::test_start_command
```

### Пример теста
```python
# tests/test_bot.py
import pytest
from unittest.mock import Mock, patch
import bot

def test_start_command():
    message = Mock()
    message.chat.id = 123456
    
    with patch('bot.bot') as mock_bot:
        bot.начать(message)
        mock_bot.send_message.assert_called_once()
```

---

## 🔍 Отладка

### Логирование
```python
import logging

# Настройка логирования
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
```

### Отладка в IDE
1. **VS Code**: Настройте launch.json
2. **PyCharm**: Создайте конфигурацию запуска
3. **Добавьте точки останова** в код

### Отладка API запросов
```python
import requests

# Включаем подробное логирование
import http.client as http_client
http_client.HTTPConnection.debuglevel = 1

# Логируем все запросы
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True
```

---

## 🚀 Развертывание

### Локальное развертывание
```bash
# Запуск в фоновом режиме (Linux/macOS)
nohup python bot.py > bot.log 2>&1 &

# Запуск через systemd (Linux)
sudo systemctl enable tbotik
sudo systemctl start tbotik
```

### Docker развертывание
```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "bot.py"]
```

```yaml
# docker-compose.yml
version: '3.8'
services:
  bot:
    build: .
    environment:
      - TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN}
      - OPENROUTER_API_KEY=${OPENROUTER_API_KEY}
      - NEUROIMG_API_KEY=${NEUROIMG_API_KEY}
    restart: unless-stopped
```

### Облачное развертывание
- **Heroku**: Используйте Procfile
- **Railway**: Подключите GitHub репозиторий
- **VPS**: Используйте systemd или Docker

---

## 🔒 Безопасность

### Защита токенов
- Никогда не коммитьте `.env` файл
- Используйте переменные окружения в продакшене
- Регулярно ротируйте API ключи

### Мониторинг
```python
# Добавьте мониторинг в bot.py
import time
import logging

def log_request(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"{func.__name__} took {end_time - start_time:.2f} seconds")
        return result
    return wrapper
```

---

## 📊 Производительность

### Оптимизация
```python
# Используйте пулы соединений
import aiohttp
import asyncio

async def optimized_request():
    connector = aiohttp.TCPConnector(limit=100)
    async with aiohttp.ClientSession(connector=connector) as session:
        # Ваши запросы
        pass
```

### Мониторинг ресурсов
```bash
# Мониторинг CPU и памяти
htop
# или
top

# Мониторинг сети
iftop
```

---

## 🔄 CI/CD

### GitHub Actions
```yaml
# .github/workflows/test.yml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    - name: Install dependencies
      run: |
        pip install -r requirements-dev.txt
    - name: Run tests
      run: |
        pytest
```

---

## 📚 Дополнительные ресурсы

### Полезные ссылки
- [pyTelegramBotAPI документация](https://github.com/eternnoir/pyTelegramBotAPI)
- [OpenRouter API документация](https://openrouter.ai/docs)
- [NeuroImg API документация](https://neuroimg.art/docs)

### Сообщество
- Telegram канал разработчиков
- GitHub Issues
- Stack Overflow

---

## 🆘 Устранение неполадок

### Частые проблемы
1. **Ошибка импорта**: Проверьте виртуальное окружение
2. **Ошибки API**: Проверьте токены и лимиты
3. **Проблемы с сетью**: Проверьте прокси и файрвол

### Получение помощи
1. Проверьте [руководство по устранению неполадок](troubleshooting.md)
2. Создайте issue в репозитории
3. Обратитесь в сообщество

---

**Версия документации**: 1.0.0  
**Последнее обновление**: 2024  
**Автор**: AI Assistant 