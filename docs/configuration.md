# ⚙️ Конфигурация

Подробное руководство по настройке AI Telegram Bot! 🔧

## 🎯 Обзор конфигурации

Конфигурация бота включает в себя настройку токенов, параметров API и системных настроек для оптимальной работы.

---

## 🔐 Управление токенами

### Структура .env файла
```env
# Telegram Bot Token
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here

# OpenRouter API Key для нейросети
OPENROUTER_API_KEY=your_openrouter_api_key_here

# NeuroImg API Key для генерации изображений
NEUROIMG_API_KEY=your_neuroimg_api_key_here
```

### Создание .env файла
1. Скопируйте `env.example` в `.env`
2. Замените placeholder значения на реальные токены
3. Убедитесь, что файл `.env` добавлен в `.gitignore`

### Проверка токенов
```python
from config import проверить_токены

# Проверяем, что все токены настроены
if проверить_токены():
    print("✅ Все токены настроены правильно")
else:
    print("❌ Некоторые токены не настроены")
```

---

## 📱 Telegram Bot Token

### Получение токена
1. Откройте Telegram и найдите @BotFather
2. Отправьте команду `/newbot`
3. Следуйте инструкциям:
   - Введите имя бота (например: "My AI Assistant")
   - Введите username (например: "my_ai_bot")
4. Скопируйте полученный токен

### Формат токена
```
1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
```

### Проверка токена
```python
import telebot

def test_telegram_token(token):
    try:
        bot = telebot.TeleBot(token)
        bot_info = bot.get_me()
        print(f"✅ Бот: {bot_info.username} (@{bot_info.username})")
        return True
    except Exception as e:
        print(f"❌ Ошибка токена: {e}")
        return False
```

---

## 🤖 OpenRouter API Key

### Регистрация
1. Зайдите на [openrouter.ai](https://openrouter.ai)
2. Нажмите "Sign Up" и создайте аккаунт
3. Перейдите в раздел API Keys
4. Создайте новый ключ

### Формат ключа
```
sk-or-v1-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Проверка ключа
```python
import requests

def test_openrouter_key(key):
    try:
        response = requests.post(
            'https://openrouter.ai/api/v1/chat/completions',
            headers={
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "qwen/qwq-32b:free",
                "messages": [{"role": "user", "content": "test"}]
            }
        )
        
        if response.status_code == 200:
            print("✅ OpenRouter API ключ работает")
            return True
        else:
            print(f"❌ Ошибка API: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка подключения: {e}")
        return False
```

---

## 🎨 NeuroImg API Key

### Регистрация
1. Зайдите на [neuroimg.art](https://neuroimg.art)
2. Создайте аккаунт
3. В личном кабинете найдите API ключ
4. Скопируйте ключ

### Формат ключа
```
xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

### Проверка ключа
```python
import requests

def test_neuroimg_key(key):
    try:
        response = requests.post(
            'https://neuroimg.art/api/v1/free-generate',
            json={
                "token": key,
                "prompt": "test",
                "stream": False
            }
        )
        
        if response.status_code == 200:
            print("✅ NeuroImg API ключ работает")
            return True
        else:
            print(f"❌ Ошибка API: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка подключения: {e}")
        return False
```

---

## 🔧 Системные настройки

### Параметры API

#### OpenRouter настройки
```python
# config.py
OPENROUTER_SETTINGS = {
    "model": "qwen/qwq-32b:free",
    "max_tokens": 1000,
    "temperature": 0.7,
    "timeout": 30
}
```

#### NeuroImg настройки
```python
# config.py
NEUROIMG_SETTINGS = {
    "width": 512,
    "height": 512,
    "steps": 20,
    "timeout": 60
}
```

### Лимиты и ограничения
```python
# config.py
LIMITS = {
    "max_prompt_length": 1000,
    "min_prompt_length": 3,
    "max_concurrent_requests": 5,
    "rate_limit_per_minute": 30
}
```

### Настройки файловой системы
```python
# config.py
FILE_SETTINGS = {
    "images_folder": "images/",
    "image_filename_format": "generated_image_{timestamp}.png",
    "timestamp_format": "%Y%m%d_%H%M%S",
    "max_images_per_user": 100
}
```

---

## 🌍 Переменные окружения

### Поддерживаемые переменные
| Переменная | Описание | Обязательная | Пример |
|------------|----------|--------------|--------|
| `TELEGRAM_BOT_TOKEN` | Токен Telegram бота | Да | `1234567890:ABC...` |
| `OPENROUTER_API_KEY` | Ключ OpenRouter API | Да | `sk-or-v1-...` |
| `NEUROIMG_API_KEY` | Ключ NeuroImg API | Да | `xxxxxxxx-...` |
| `DEBUG` | Режим отладки | Нет | `true/false` |
| `LOG_LEVEL` | Уровень логирования | Нет | `INFO/DEBUG/ERROR` |

### Установка переменных

#### Windows
```cmd
set TELEGRAM_BOT_TOKEN=your_token_here
set OPENROUTER_API_KEY=your_key_here
set NEUROIMG_API_KEY=your_key_here
```

#### Linux/macOS
```bash
export TELEGRAM_BOT_TOKEN=your_token_here
export OPENROUTER_API_KEY=your_key_here
export NEUROIMG_API_KEY=your_key_here
```

#### В коде
```python
import os

os.environ['TELEGRAM_BOT_TOKEN'] = 'your_token_here'
os.environ['OPENROUTER_API_KEY'] = 'your_key_here'
os.environ['NEUROIMG_API_KEY'] = 'your_key_here'
```

---

## 🔒 Безопасность

### Защита токенов
1. **Никогда не коммитьте `.env` файл**
2. **Используйте переменные окружения в продакшене**
3. **Регулярно ротируйте API ключи**
4. **Ограничьте доступ к файлам конфигурации**

### Проверка безопасности
```python
def security_check():
    issues = []
    
    # Проверяем, что .env не в Git
    if os.path.exists('.env'):
        with open('.gitignore', 'r') as f:
            if '.env' not in f.read():
                issues.append("⚠️ .env файл не в .gitignore")
    
    # Проверяем права доступа
    if os.path.exists('.env'):
        stat = os.stat('.env')
        if stat.st_mode & 0o777 != 0o600:
            issues.append("⚠️ Небезопасные права доступа к .env")
    
    return issues
```

---

## 📊 Мониторинг конфигурации

### Проверка всех настроек
```python
def check_all_config():
    print("🔍 Проверка конфигурации...")
    
    # Проверяем токены
    if not проверить_токены():
        print("❌ Проблемы с токенами")
        return False
    
    # Проверяем API
    if not test_telegram_token(TELEGRAM_BOT_TOKEN):
        print("❌ Проблемы с Telegram API")
        return False
    
    if not test_openrouter_key(OPENROUTER_API_KEY):
        print("❌ Проблемы с OpenRouter API")
        return False
    
    if not test_neuroimg_key(NEUROIMG_API_KEY):
        print("❌ Проблемы с NeuroImg API")
        return False
    
    print("✅ Все настройки корректны")
    return True
```

### Логирование конфигурации
```python
import logging

def log_config():
    logger = logging.getLogger(__name__)
    
    logger.info("Конфигурация загружена:")
    logger.info(f"Telegram Bot: {'Настроен' if TELEGRAM_BOT_TOKEN else 'Не настроен'}")
    logger.info(f"OpenRouter API: {'Настроен' if OPENROUTER_API_KEY else 'Не настроен'}")
    logger.info(f"NeuroImg API: {'Настроен' if NEUROIMG_API_KEY else 'Не настроен'}")
```

---

## 🚀 Продакшн настройки

### Docker
```dockerfile
# Dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Переменные окружения
ENV TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN}
ENV OPENROUTER_API_KEY=${OPENROUTER_API_KEY}
ENV NEUROIMG_API_KEY=${NEUROIMG_API_KEY}

CMD ["python", "bot.py"]
```

### Docker Compose
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
      - DEBUG=false
      - LOG_LEVEL=INFO
    restart: unless-stopped
```

### Systemd (Linux)
```ini
# /etc/systemd/system/tbotik.service
[Unit]
Description=AI Telegram Bot
After=network.target

[Service]
Type=simple
User=tbotik
WorkingDirectory=/opt/tbotik
Environment=TELEGRAM_BOT_TOKEN=your_token
Environment=OPENROUTER_API_KEY=your_key
Environment=NEUROIMG_API_KEY=your_key
ExecStart=/usr/bin/python3 bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

---

## 🔄 Обновление конфигурации

### Без перезапуска
```python
def reload_config():
    """Перезагрузка конфигурации без перезапуска бота"""
    global TELEGRAM_BOT_TOKEN, OPENROUTER_API_KEY, NEUROIMG_API_KEY
    
    # Перезагружаем переменные окружения
    load_dotenv(override=True)
    
    # Обновляем переменные
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
    NEUROIMG_API_KEY = os.getenv('NEUROIMG_API_KEY')
    
    print("✅ Конфигурация обновлена")
```

### Валидация изменений
```python
def validate_config_changes():
    """Проверка корректности изменений конфигурации"""
    issues = []
    
    # Проверяем токены
    if not проверить_токены():
        issues.append("Некорректные токены")
    
    # Проверяем API
    if not test_telegram_token(TELEGRAM_BOT_TOKEN):
        issues.append("Telegram API недоступен")
    
    return issues
```

---

## 🆘 Устранение проблем

### Частые проблемы

#### Токен не работает
1. Проверьте правильность токена
2. Убедитесь, что бот не заблокирован
3. Проверьте интернет-соединение

#### API недоступен
1. Проверьте лимиты API
2. Убедитесь в правильности ключа
3. Проверьте статус сервиса

#### Ошибки конфигурации
1. Проверьте формат .env файла
2. Убедитесь в отсутствии лишних пробелов
3. Проверьте кодировку файла (UTF-8)

### Диагностика
```python
def diagnose_config():
    """Полная диагностика конфигурации"""
    print("🔍 Диагностика конфигурации...")
    
    # Проверяем файлы
    if not os.path.exists('.env'):
        print("❌ Файл .env не найден")
        return False
    
    # Проверяем токены
    if not проверить_токены():
        print("❌ Проблемы с токенами")
        return False
    
    # Проверяем API
    print("🔍 Проверка API...")
    check_all_config()
    
    return True
```

---

## 📚 Дополнительные ресурсы

### Полезные ссылки
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [OpenRouter API](https://openrouter.ai/docs)
- [NeuroImg API](https://neuroimg.art/docs)
- [python-dotenv документация](https://github.com/theskumar/python-dotenv)

### Примеры конфигурации
- [Пример .env файла](env.example)
- [Docker конфигурация](docker-compose.yml)
- [Systemd сервис](tbotik.service)

---

**Версия документации**: 1.0.0  
**Последнее обновление**: 2024  
**Автор**: AI Assistant 