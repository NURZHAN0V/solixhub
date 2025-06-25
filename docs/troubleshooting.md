# 🔧 Устранение неполадок

Подробное руководство по решению проблем с AI Telegram Bot! 🛠️

## 🎯 Обзор

Этот раздел поможет вам решить наиболее частые проблемы, возникающие при использовании бота. Если вы не нашли решение здесь, обратитесь к сообществу.

---

## 🚨 Критические ошибки

### Бот не запускается

#### Ошибка: "ModuleNotFoundError: No module named 'telebot'"
**Причина**: Не установлена библиотека pyTelegramBotAPI

**Решение**:
```bash
pip install pyTelegramBotAPI
# или
pip install -r requirements.txt
```

#### Ошибка: "ModuleNotFoundError: No module named 'dotenv'"
**Причина**: Не установлена библиотека python-dotenv

**Решение**:
```bash
pip install python-dotenv
# или
pip install -r requirements.txt
```

#### Ошибка: "ImportError: cannot import name 'load_dotenv'"
**Причина**: Неправильная версия python-dotenv

**Решение**:
```bash
pip uninstall python-dotenv
pip install python-dotenv==1.0.0
```

### Бот запускается, но не отвечает

#### Проблема: Бот не реагирует на сообщения
**Возможные причины**:
1. Неверный токен Telegram
2. Бот заблокирован
3. Проблемы с интернетом

**Диагностика**:
```python
import telebot

def test_bot():
    try:
        bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
        bot_info = bot.get_me()
        print(f"✅ Бот активен: {bot_info.username}")
        return True
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False
```

**Решение**:
1. Проверьте токен в @BotFather
2. Убедитесь, что бот не заблокирован
3. Проверьте интернет-соединение

---

## 🔑 Проблемы с токенами

### Telegram Bot Token

#### Ошибка: "Unauthorized: Invalid token"
**Причина**: Неверный или устаревший токен

**Решение**:
1. Откройте @BotFather в Telegram
2. Отправьте `/mybots`
3. Выберите вашего бота
4. Нажмите "API Token"
5. Скопируйте новый токен
6. Обновите `.env` файл

#### Ошибка: "Forbidden: bot was blocked by the user"
**Причина**: Пользователь заблокировал бота

**Решение**:
1. Попросите пользователя разблокировать бота
2. Или создайте нового бота через @BotFather

### OpenRouter API Key

#### Ошибка: "401 Unauthorized"
**Причина**: Неверный API ключ

**Решение**:
1. Зайдите на [openrouter.ai](https://openrouter.ai)
2. Перейдите в раздел API Keys
3. Создайте новый ключ
4. Обновите `.env` файл

#### Ошибка: "429 Too Many Requests"
**Причина**: Превышен лимит запросов

**Решение**:
1. Проверьте лимиты в личном кабинете
2. Подождите некоторое время
3. Рассмотрите платный план

### NeuroImg API Key

#### Ошибка: "Invalid token"
**Причина**: Неверный токен

**Решение**:
1. Зайдите на [neuroimg.art](https://neuroimg.art)
2. Проверьте токен в личном кабинете
3. Создайте новый токен при необходимости

#### Ошибка: "Daily limit exceeded"
**Причина**: Превышен дневной лимит генераций

**Решение**:
1. Подождите до следующего дня
2. Рассмотрите платный план

---

## 🌐 Сетевые проблемы

### Проблемы с подключением

#### Ошибка: "Connection timeout"
**Причина**: Медленное интернет-соединение или блокировка

**Решение**:
1. Проверьте скорость интернета
2. Попробуйте использовать VPN
3. Увеличьте таймауты в коде

#### Ошибка: "SSL Certificate Error"
**Причина**: Проблемы с SSL сертификатами

**Решение**:
```python
import ssl
import requests

# Отключение проверки SSL (не рекомендуется для продакшена)
requests.packages.urllib3.disable_warnings()
response = requests.get(url, verify=False)
```

### Проблемы с прокси

#### Ошибка: "Proxy connection failed"
**Причина**: Неправильные настройки прокси

**Решение**:
```python
import requests

proxies = {
    'http': 'http://proxy:port',
    'https': 'https://proxy:port'
}

response = requests.get(url, proxies=proxies)
```

---

## 🎨 Проблемы с генерацией изображений

### Картинка не генерируется

#### Ошибка: "Описание слишком короткое"
**Причина**: Описание менее 3 символов

**Решение**:
- Добавьте больше деталей к описанию
- Используйте минимум 3 символа

#### Ошибка: "Не удалось сгенерировать картинку"
**Причина**: Проблемы с API или сервером

**Диагностика**:
```python
async def test_neuroimg():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                'https://neuroimg.art/api/v1/free-generate',
                json={
                    "token": NEUROIMG_API_KEY,
                    "prompt": "test",
                    "stream": False
                }
            ) as response:
                if response.status == 200:
                    print("✅ NeuroImg API работает")
                    return True
                else:
                    print(f"❌ Ошибка: {response.status}")
                    return False
    except Exception as e:
        print(f"❌ Ошибка подключения: {e}")
        return False
```

**Решение**:
1. Проверьте токен API
2. Убедитесь в наличии лимитов
3. Попробуйте позже

### Долгая генерация

#### Проблема: Генерация занимает больше минуты
**Причина**: Высокая нагрузка на сервер

**Решение**:
1. Подождите завершения
2. Попробуйте в другое время
3. Используйте более простые описания

### Проблемы с сохранением изображений
1. ✅ Проверьте права доступа к папке `images/`
2. ✅ Убедитесь, что папка `images/` существует
3. ✅ Проверьте свободное место на диске

#### Ошибка: "Permission denied" при сохранении
**Причина**: Недостаточно прав для записи в папку `images/`

**Решение**:
```bash
# Windows: запустите от имени администратора
# Linux/macOS: измените права доступа
chmod 755 images/
```

---

## 💬 Проблемы с чатом ИИ

### Бот не отвечает на вопросы

#### Ошибка: "Ошибка API: 401"
**Причина**: Неверный OpenRouter API ключ

**Решение**:
1. Проверьте ключ в личном кабинете
2. Создайте новый ключ при необходимости

#### Ошибка: "Неожиданный формат ответа API"
**Причина**: Изменения в API или неверный запрос

**Диагностика**:
```python
def test_openrouter():
    try:
        response = requests.post(
            'https://openrouter.ai/api/v1/chat/completions',
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "qwen/qwq-32b:free",
                "messages": [{"role": "user", "content": "test"}]
            }
        )
        
        print(f"Статус: {response.status_code}")
        print(f"Ответ: {response.text}")
        
        if response.status_code == 200:
            data = response.json()
            if "choices" in data and data["choices"]:
                print("✅ API работает корректно")
                return True
        
        return False
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False
```

### Неточные ответы

#### Проблема: Бот дает неправильные ответы
**Причина**: Ограничения модели или нечеткий вопрос

**Решение**:
1. Задавайте более конкретные вопросы
2. Добавляйте контекст
3. Используйте английский язык для сложных тем

---

## 🔧 Технические проблемы

### Проблемы с Python

#### Ошибка: "Python version not supported"
**Причина**: Неподдерживаемая версия Python

**Решение**:
```bash
# Проверьте версию
python --version

# Установите Python 3.8+
# Windows: скачайте с python.org
# Linux: sudo apt install python3.8
# macOS: brew install python@3.8
```

#### Ошибка: "Permission denied"
**Причина**: Недостаточно прав

**Решение**:
```bash
# Windows: запустите от имени администратора
# Linux/macOS: используйте sudo
sudo python3 bot.py
```

### Проблемы с зависимостями

#### Конфликт версий
**Причина**: Несовместимые версии библиотек

**Решение**:
```bash
# Создайте новое виртуальное окружение
python -m venv venv_new
source venv_new/bin/activate  # Linux/macOS
venv_new\Scripts\activate     # Windows

# Установите зависимости
pip install -r requirements.txt
```

---

## 📱 Проблемы с Telegram

### Бот не видит сообщения

#### Проблема: Бот не получает обновления
**Причина**: Проблемы с webhook или polling

**Решение**:
```python
# Принудительно используйте polling
bot.remove_webhook()
bot.polling(none_stop=True, timeout=60)
```

#### Ошибка: "Bot was kicked from the group chat"
**Причина**: Бота удалили из группы

**Решение**:
1. Добавьте бота обратно в группу
2. Убедитесь, что у бота есть права на отправку сообщений

### Проблемы с отправкой

#### Ошибка: "Message is too long"
**Причина**: Сообщение превышает лимит 4096 символов

**Решение**:
```python
def split_message(text, max_length=4000):
    """Разбивает длинное сообщение на части"""
    if len(text) <= max_length:
        return [text]
    
    parts = []
    while text:
        if len(text) <= max_length:
            parts.append(text)
            break
        
        # Ищем последний пробел в пределах лимита
        split_point = text.rfind(' ', 0, max_length)
        if split_point == -1:
            split_point = max_length
        
        parts.append(text[:split_point])
        text = text[split_point:].lstrip()
    
    return parts
```

---

## 🔍 Диагностика

### Полная диагностика системы
```python
def full_diagnostic():
    """Выполняет полную диагностику системы"""
    print("🔍 Начинаем диагностику...")
    
    issues = []
    
    # Проверяем Python
    import sys
    if sys.version_info < (3, 8):
        issues.append("Python версия ниже 3.8")
    
    # Проверяем зависимости
    try:
        import telebot
        print("✅ pyTelegramBotAPI установлен")
    except ImportError:
        issues.append("pyTelegramBotAPI не установлен")
    
    try:
        import requests
        print("✅ requests установлен")
    except ImportError:
        issues.append("requests не установлен")
    
    try:
        import aiohttp
        print("✅ aiohttp установлен")
    except ImportError:
        issues.append("aiohttp не установлен")
    
    # Проверяем конфигурацию
    from config import проверить_токены
    if not проверить_токены():
        issues.append("Проблемы с токенами")
    
    # Проверяем интернет
    try:
        import requests
        response = requests.get("https://api.telegram.org", timeout=5)
        print("✅ Интернет работает")
    except:
        issues.append("Проблемы с интернетом")
    
    if issues:
        print("❌ Найдены проблемы:")
        for issue in issues:
            print(f"  - {issue}")
        return False
    else:
        print("✅ Все проверки пройдены")
        return True
```

### Логирование ошибок
```python
import logging

# Настройка логирования
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot_errors.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Использование в коде
try:
    # Ваш код
    pass
except Exception as e:
    logger.error(f"Ошибка: {e}", exc_info=True)
```

---

## 🆘 Получение помощи

### Когда обращаться за помощью

1. **Проблема не решается** после выполнения всех шагов
2. **Новая ошибка**, которой нет в этом руководстве
3. **Проблемы с производительностью** бота
4. **Предложения по улучшению**

### Как описать проблему

При обращении за помощью предоставьте:

1. **Описание проблемы** - что происходит?
2. **Ожидаемое поведение** - что должно происходить?
3. **Шаги для воспроизведения** - как повторить проблему?
4. **Логи ошибок** - полные сообщения об ошибках
5. **Версии** - Python, библиотек, ОС
6. **Конфигурация** - какие токены настроены (без самих токенов!)

### Где получить помощь

1. **GitHub Issues** - для багов и предложений
2. **Telegram группа** - для быстрых вопросов
3. **Stack Overflow** - для технических вопросов
4. **Документация** - для изучения возможностей

---

## 📚 Полезные команды

### Отладка в Python
```python
# Включение отладки
import pdb; pdb.set_trace()

# Логирование переменных
print(f"DEBUG: {variable}")

# Проверка типов
print(f"Type: {type(variable)}")
```

### Системные команды
```bash
# Проверка процессов
ps aux | grep python

# Проверка портов
netstat -tulpn | grep python

# Проверка логов
tail -f bot_errors.log
```

---

## 🔄 Профилактика проблем

### Регулярные проверки
1. **Еженедельно**: Проверяйте лимиты API
2. **Ежемесячно**: Обновляйте зависимости
3. **Ежеквартально**: Ротируйте API ключи

### Мониторинг
```python
def health_check():
    """Проверка здоровья системы"""
    checks = {
        "telegram": test_telegram_token(TELEGRAM_BOT_TOKEN),
        "openrouter": test_openrouter_key(OPENROUTER_API_KEY),
        "neuroimg": test_neuroimg_key(NEUROIMG_API_KEY)
    }
    
    return all(checks.values())
```

---

**Версия документации**: 1.0.0  
**Последнее обновление**: 2024  
**Автор**: AI Assistant 