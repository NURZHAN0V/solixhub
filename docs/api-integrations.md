# 🔌 API интеграции

Техническая документация по внешним API, используемым в AI Telegram Bot! 🔧

## 🎯 Обзор API

Бот интегрируется с тремя основными внешними API для обеспечения полного функционала:

1. **Telegram Bot API** - платформа для ботов
2. **OpenRouter API** - доступ к ИИ моделям
3. **NeuroImg API** - генерация изображений

---

## 📱 Telegram Bot API

### Описание
Telegram Bot API предоставляет интерфейс для создания и управления ботами в Telegram.

### Основные возможности
- Отправка и получение сообщений
- Обработка команд
- Отправка медиафайлов
- Управление чатами

### Интеграция в проекте
```python
import telebot

# Создание экземпляра бота
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Обработка команд
@bot.message_handler(commands=['start'])
def начать(message):
    bot.send_message(message.chat.id, "Привет!")

# Обработка текстовых сообщений
@bot.message_handler(func=lambda message: True)
def обработать_сообщение(message):
    # Логика обработки
    pass
```

### Основные методы
| Метод | Описание | Пример |
|-------|----------|--------|
| `send_message()` | Отправка текстового сообщения | `bot.send_message(chat_id, "Текст")` |
| `send_photo()` | Отправка изображения | `bot.send_photo(chat_id, photo)` |
| `send_chat_action()` | Показать действие | `bot.send_chat_action(chat_id, 'typing')` |
| `polling()` | Запуск бота | `bot.polling(none_stop=True)` |

### Обработка ошибок
```python
try:
    bot.polling(none_stop=True)
except Exception as e:
    print(f"Ошибка Telegram API: {e}")
    time.sleep(5)
```

### Лимиты и ограничения
- **Частота сообщений**: 30 сообщений в секунду
- **Размер сообщения**: 4096 символов
- **Размер файла**: 50MB
- **Размер изображения**: 10MB

---

## 🤖 OpenRouter API

### Описание
OpenRouter предоставляет доступ к различным ИИ моделям через единый API интерфейс.

### Поддерживаемые модели
- **qwen/qwq-32b:free** - основная модель (бесплатная)
- **gpt-3.5-turbo** - OpenAI GPT-3.5
- **claude-3-haiku** - Anthropic Claude
- **llama-2-70b** - Meta Llama 2

### Интеграция в проекте
```python
def задать_вопрос(вопрос):
    try:
        ответ_от_нейросети = requests.post(
            url='https://openrouter.ai/api/v1/chat/completions',
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "model": "qwen/qwq-32b:free",
                "messages": [{"role": "user", "content": вопрос}]
            })
        )
        
        # Проверка статуса
        if ответ_от_нейросети.status_code != 200:
            return f"Ошибка API: {ответ_от_нейросети.status_code}"
        
        данные = ответ_от_нейросети.json()
        return данные["choices"][0]["message"]["content"]
        
    except Exception as e:
        return f"Ошибка: {e}"
```

### Структура запроса
```json
{
  "model": "qwen/qwq-32b:free",
  "messages": [
    {
      "role": "user",
      "content": "Привет, как дела?"
    }
  ],
  "max_tokens": 1000,
  "temperature": 0.7
}
```

### Структура ответа
```json
{
  "id": "chatcmpl-123",
  "object": "chat.completion",
  "created": 1677652288,
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Привет! У меня все хорошо, спасибо!"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 9,
    "completion_tokens": 12,
    "total_tokens": 21
  }
}
```

### Обработка ошибок
```python
# Проверка структуры ответа
if "choices" not in данные:
    return f"Неожиданный формат ответа API: {данные}"

if not данные["choices"]:
    return "API вернул пустой ответ"

if "message" not in данные["choices"][0]:
    return f"Отсутствует сообщение в ответе: {данные['choices'][0]}"

if "content" not in данные["choices"][0]["message"]:
    return f"Отсутствует содержимое в сообщении: {данные['choices'][0]['message']}"
```

### Лимиты и тарификация
- **Бесплатный план**: 1000 запросов/день
- **Платные планы**: от $5/месяц
- **Токены**: зависит от модели
- **Скорость**: до 100 запросов/минуту

---

## 🎨 NeuroImg API

### Описание
NeuroImg API предоставляет возможности генерации изображений по текстовому описанию.

### Основные возможности
- Генерация изображений по промпту
- Поддержка различных стилей
- Стриминг результатов
- Очередь запросов

### Интеграция в проекте
```python
async def сгенерировать_изображение(описание):
    url = "https://neuroimg.art/api/v1/free-generate"
    
    payload = {
        "token": NEUROIMG_API_KEY,
        "prompt": описание,
        "stream": True
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as response:
            async for line in response.content:
                if line:
                    try:
                        данные = line.decode('utf-8')
                        ответ = eval(данные.replace("true", "True").replace("false", "False"))
                        
                        if "status" not in ответ:
                            continue
                            
                        if ответ["status"] == "SUCCESS":
                            return ответ["image_url"]
                            
                        elif ответ["status"] == "WAITING":
                            print(f"⏳ В очереди: {ответ['queue_position']}")
                            
                    except Exception as e:
                        print("❌ Ошибка:", e)
```

### Структура запроса
```json
{
  "token": "your_api_token",
  "prompt": "красивая кошка на закате",
  "stream": true,
  "width": 512,
  "height": 512,
  "steps": 20
}
```

### Структура ответа (стриминг)
```json
{"status": "WAITING", "queue_position": 5}
{"status": "PROCESSING", "progress": 50}
{"status": "SUCCESS", "image_url": "https://example.com/image.png"}
```

### Обработка статусов
```python
# Ожидание в очереди
if ответ["status"] == "WAITING":
    print(f"⏳ В очереди: {ответ['queue_position']}")

# Обработка
elif ответ["status"] == "PROCESSING":
    print(f"🔄 Обработка: {ответ['progress']}%")

# Успех
elif ответ["status"] == "SUCCESS":
    return ответ["image_url"]

# Ошибка
elif ответ["status"] == "ERROR":
    print(f"❌ Ошибка: {ответ['error']}")
```

### Скачивание изображения
```python
def скачать_и_отправить_картинку(chat_id, ссылка):
    try:
        ответ = requests.get(ссылка)
        if ответ.status_code == 200:
            # Создаем уникальное имя файла с временной меткой
            import datetime
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"images/generated_image_{timestamp}.png"
            
            # Сохраняем изображение в папку images
            with open(filename, "wb") as файл:
                файл.write(ответ.content)
            
            # Отправляем изображение пользователю
            bot.send_photo(chat_id, open(filename, "rb"))
            
            print(f"✅ Изображение сохранено: {filename}")
        else:
            bot.send_message(chat_id, f"Ошибка при скачивании: {ответ.status_code}")
    except Exception as e:
        bot.send_message(chat_id, f"Ошибка при обработке: {e}")
```

### Лимиты и ограничения
- **Бесплатный план**: 10 изображений/день
- **Размер изображения**: 512x512 пикселей
- **Время генерации**: 30-60 секунд
- **Поддерживаемые форматы**: PNG, JPG

---

## 🔄 Асинхронная обработка

### Зачем асинхронность?
- Генерация изображений занимает время
- Неблокирующая обработка запросов
- Лучшая производительность

### Реализация в проекте
```python
# Запуск асинхронной функции в синхронном коде
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
ссылка = loop.run_until_complete(сгенерировать_изображение(описание))
```

### Альтернативный подход
```python
import asyncio
import threading

def run_async_in_thread(coro):
    def run_in_thread():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        return loop.run_until_complete(coro)
    
    thread = threading.Thread(target=run_in_thread)
    thread.start()
    thread.join()
```

---

## 🔒 Безопасность API

### Защита токенов
```python
# Использование переменных окружения
import os
from dotenv import load_dotenv

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
NEUROIMG_API_KEY = os.getenv('NEUROIMG_API_KEY')
```

### Валидация запросов
```python
def validate_prompt(prompt):
    if len(prompt) < 3:
        return False, "Описание слишком короткое"
    
    # Проверка на запрещенный контент
    forbidden_words = ["violence", "nude", "explicit"]
    if any(word in prompt.lower() for word in forbidden_words):
        return False, "Запрещенный контент"
    
    return True, "OK"
```

### Rate Limiting
```python
import time
from collections import defaultdict

class RateLimiter:
    def __init__(self, max_requests, time_window):
        self.max_requests = max_requests
        self.time_window = time_window
        self.requests = defaultdict(list)
    
    def can_make_request(self, user_id):
        now = time.time()
        user_requests = self.requests[user_id]
        
        # Удаляем старые запросы
        user_requests = [req for req in user_requests if now - req < self.time_window]
        self.requests[user_id] = user_requests
        
        if len(user_requests) < self.max_requests:
            user_requests.append(now)
            return True
        return False
```

---

## 📊 Мониторинг API

### Логирование запросов
```python
import logging
import time

def log_api_request(api_name, duration, status):
    logging.info(f"API {api_name}: {duration:.2f}s, status: {status}")

# Использование
start_time = time.time()
try:
    response = requests.post(url, json=data)
    duration = time.time() - start_time
    log_api_request("OpenRouter", duration, response.status_code)
except Exception as e:
    duration = time.time() - start_time
    log_api_request("OpenRouter", duration, f"ERROR: {e}")
```

### Метрики производительности
```python
class APIMetrics:
    def __init__(self):
        self.requests = 0
        self.errors = 0
        self.total_time = 0
    
    def record_request(self, duration, success=True):
        self.requests += 1
        self.total_time += duration
        if not success:
            self.errors += 1
    
    def get_stats(self):
        avg_time = self.total_time / self.requests if self.requests > 0 else 0
        error_rate = self.errors / self.requests if self.requests > 0 else 0
        return {
            "total_requests": self.requests,
            "error_rate": error_rate,
            "avg_response_time": avg_time
        }
```

---

## 🚀 Оптимизация

### Кэширование ответов
```python
import hashlib
import json
from functools import lru_cache

@lru_cache(maxsize=1000)
def cached_ai_response(question_hash):
    # Логика получения ответа от ИИ
    pass

def get_ai_response(question):
    question_hash = hashlib.md5(question.encode()).hexdigest()
    return cached_ai_response(question_hash)
```

### Пул соединений
```python
import aiohttp

async def create_session():
    connector = aiohttp.TCPConnector(
        limit=100,
        limit_per_host=30,
        ttl_dns_cache=300
    )
    return aiohttp.ClientSession(connector=connector)
```

### Retry логика
```python
import asyncio
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
async def api_request_with_retry(url, data):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as response:
            if response.status >= 500:
                raise Exception(f"Server error: {response.status}")
            return await response.json()
```

---

## 🔧 Устранение неполадок

### Частые проблемы API

#### Telegram API
- **Ошибка 401**: Неверный токен
- **Ошибка 429**: Превышен лимит запросов
- **Ошибка 400**: Неверный формат запроса

#### OpenRouter API
- **Ошибка 401**: Неверный API ключ
- **Ошибка 429**: Превышен лимит токенов
- **Ошибка 400**: Неверная модель или параметры

#### NeuroImg API
- **Ошибка 401**: Неверный токен
- **Ошибка 429**: Превышен лимит генераций
- **Ошибка 400**: Неверный промпт

### Диагностика
```python
def diagnose_api_issues():
    issues = []
    
    # Проверка Telegram API
    try:
        bot_info = bot.get_me()
        print(f"✅ Telegram API: {bot_info.username}")
    except Exception as e:
        issues.append(f"Telegram API: {e}")
    
    # Проверка OpenRouter API
    try:
        response = requests.post(
            'https://openrouter.ai/api/v1/chat/completions',
            headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}"},
            json={"model": "qwen/qwq-32b:free", "messages": [{"role": "user", "content": "test"}]}
        )
        if response.status_code == 200:
            print("✅ OpenRouter API: OK")
        else:
            issues.append(f"OpenRouter API: {response.status_code}")
    except Exception as e:
        issues.append(f"OpenRouter API: {e}")
    
    return issues
```

---

## 📚 Дополнительные ресурсы

### Официальная документация
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [OpenRouter API](https://openrouter.ai/docs)
- [NeuroImg API](https://neuroimg.art/docs)

### Сообщество
- [pyTelegramBotAPI GitHub](https://github.com/eternnoir/pyTelegramBotAPI)
- [OpenRouter Discord](https://discord.gg/openrouter)
- [Telegram Bot Developers](https://t.me/botfather)

---

**Версия документации**: 1.0.0  
**Последнее обновление**: 2024  
**Автор**: AI Assistant 