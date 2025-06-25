# Импортируем всё необходимое
import telebot  # Для работы с Telegram
import time     # Чтобы задерживать ответы
import requests # Чтобы общаться с нейросетью
import json     # Чтобы читать ответы от сервера
import aiohttp  # Асинхронное общение для генерации картинок
import asyncio  # Нужно для async/await
from config import *  # Подключаем наши секретные ключи
import datetime

# Создаём бота с токеном из config.py
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Функция для получения ответа от нейросети
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
        
        # Проверяем статус ответа
        if ответ_от_нейросети.status_code != 200:
            return f"Ошибка API: {ответ_от_нейросети.status_code} - {ответ_от_нейросети.text}"
        
        данные = ответ_от_нейросети.json()
        
        # Проверяем структуру ответа
        if "choices" not in данные:
            return f"Неожиданный формат ответа API: {данные}"
        
        if not данные["choices"]:
            return "API вернул пустой ответ"
        
        if "message" not in данные["choices"][0]:
            return f"Отсутствует сообщение в ответе: {данные['choices'][0]}"
        
        if "content" not in данные["choices"][0]["message"]:
            return f"Отсутствует содержимое в сообщении: {данные['choices'][0]['message']}"
        
        return данные["choices"][0]["message"]["content"]
        
    except requests.exceptions.RequestException as e:
        return f"Ошибка сети при обращении к API: {e}"
    except json.JSONDecodeError as e:
        return f"Ошибка при разборе JSON ответа: {e}"
    except Exception as e:
        return f"Неожиданная ошибка: {e}"

# Асинхронная функция для генерации картинки
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
                        try:
                            ответ = eval(данные.replace("true", "True").replace("false", "False"))
                        except:
                            continue

                        if "status" not in ответ:
                            continue

                        if ответ["status"] == "SUCCESS":
                            return ответ["image_url"]

                        elif ответ["status"] == "WAITING":
                            print(f"⏳ В очереди: {ответ['queue_position']}")

                    except Exception as e:
                        print("❌ Ошибка:", e)

# Функция скачивания и отправки изображения
def скачать_и_отправить_картинку(chat_id, ссылка):
    try:
        ответ = requests.get(ссылка)
        if ответ.status_code == 200:
            # Создаем уникальное имя файла с временной меткой
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"images/generated_image_{timestamp}.png"
            
            # Сохраняем изображение в папку images
            with open(filename, "wb") as файл:
                файл.write(ответ.content)
            
            # Отправляем изображение пользователю
            bot.send_photo(chat_id, open(filename, "rb"))
            
            print(f"✅ Изображение сохранено: {filename}")
        else:
            bot.send_message(chat_id, f"Ошибка при скачивании изображения: {ответ.status_code}")
    except Exception as e:
        bot.send_message(chat_id, f"Ошибка при обработке изображения: {e}")

# Функция для запуска генерации картинки
def запустить_генерацию_картинки(chat_id, описание):
    try:
        bot.send_message(chat_id, "🎨 Начинаю генерацию картинки...")
        
        # Запускаем асинхронную функцию
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        ссылка = loop.run_until_complete(сгенерировать_изображение(описание))
        
        if ссылка:
            bot.send_message(chat_id, "✅ Картинка готова! Скачиваю...")
            скачать_и_отправить_картинку(chat_id, ссылка)
        else:
            bot.send_message(chat_id, "❌ Не удалось сгенерировать картинку. Попробуйте еще раз или измените описание.")
            
    except Exception as e:
        bot.send_message(chat_id, f"❌ Ошибка при генерации: {e}")

# Команда /start
@bot.message_handler(commands=['start'])
def начать(message):
    приветствие = """
🎉 Привет! Я умный бот с искусственным интеллектом!

🤖 Что я умею:
• Отвечать на любые вопросы
• Генерировать картинки по описанию

📝 Команды:
/start - это сообщение
/draw [описание] - нарисовать картинку
/help - показать справку

💡 Примеры:
/draw красивая кошка на закате
/draw космический корабль в стиле аниме
/draw портрет человека в стиле Ван Гога

Просто напишите мне любой вопрос или используйте команду /draw для создания картинки!
"""
    bot.send_message(message.chat.id, приветствие)

# Команда /help
@bot.message_handler(commands=['help'])
def помощь(message):
    справка = """
🤖 Справка по использованию бота:

📝 Команды:
/start - приветствие и описание возможностей
/draw [описание] - генерация картинки по описанию
/help - эта справка

🎨 Генерация картинок:
• Используйте команду /draw с описанием
• Описание должно быть на русском или английском языке
• Чем подробнее описание, тем лучше результат

💬 Чат с ИИ:
• Просто напишите любой вопрос
• Бот ответит используя нейросеть

⚠️ Ограничения:
• Генерация картинок может занять время
• Некоторые запросы могут быть отклонены
• Изображения сохраняются временно
"""
    bot.send_message(message.chat.id, справка)

# Команда /draw
@bot.message_handler(commands=['draw'])
def нарисовать_картинку(message):
    # Получаем описание из команды
    текст_команды = message.text.split(' ', 1)
    
    if len(текст_команды) < 2:
        bot.send_message(message.chat.id, 
                        "❌ Пожалуйста, укажите описание картинки!\n\n"
                        "Пример: /draw красивая кошка на закате\n"
                        "Или: /draw космический корабль в стиле аниме")
        return
    
    описание = текст_команды[1].strip()
    
    if len(описание) < 3:
        bot.send_message(message.chat.id, 
                        "❌ Описание слишком короткое. Пожалуйста, опишите подробнее, что вы хотите нарисовать.")
        return
    
    # Запускаем генерацию
    запустить_генерацию_картинки(message.chat.id, описание)

# Обработка текстовых сообщений
@bot.message_handler(func=lambda message: True)
def обработать_сообщение(message):
    текст = message.text.lower()
    chat_id = message.chat.id

    # Проверяем, не является ли сообщение командой
    if message.text.startswith('/'):
        return

    if "нарисуй" in текст or "картинка" in текст:
        bot.send_message(chat_id, "Хорошо! Сейчас нарисую тебе картинку...")

        # Запускаем асинхронную функцию внутри обычной
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        ссылка = loop.run_until_complete(сгенерировать_изображение(message.text))

        if ссылка:
            скачать_и_отправить_картинку(chat_id, ссылка)
        else:
            bot.send_message(chat_id, "Не смог нарисовать картинку 🙁")
    else:
        bot.send_chat_action(chat_id, 'typing')
        print("Печатает...")
        time.sleep(2)
        ответ = задать_вопрос(message.text)
        bot.send_message(chat_id, ответ)

# Запуск бота
print("🤖 Запуск AI Telegram Bot...")

# Проверяем токены при запуске
from config import проверить_токены
if not проверить_токены():
    print("❌ Проблемы с токенами. Проверьте файл .env")
    print("📝 Создайте файл .env на основе env.example и заполните токены")
    exit(1)

print("✅ Все токены настроены правильно")
print("🚀 Бот запущен...")

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        print("🔄 Перезапуск через 5 секунд...")
        time.sleep(5)