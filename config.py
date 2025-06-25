import os
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

# Получаем токены из переменных окружения или используем значения по умолчанию
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
NEUROIMG_API_KEY = os.getenv('NEUROIMG_API_KEY')

# Проверяем, что все токены установлены
def проверить_токены():
    """Проверяет наличие всех необходимых токенов"""
    отсутствующие = []
    
    if TELEGRAM_BOT_TOKEN == 'your_telegram_bot_token_here':
        отсутствующие.append('TELEGRAM_BOT_TOKEN')
    if OPENROUTER_API_KEY == 'your_openrouter_api_key_here':
        отсутствующие.append('OPENROUTER_API_KEY')
    if NEUROIMG_API_KEY == 'your_neuroimg_api_key_here':
        отсутствующие.append('NEUROIMG_API_KEY')
    
    if отсутствующие:
        print(f"⚠️  Внимание! Следующие токены не настроены: {', '.join(отсутствующие)}")
        print("📝 Создайте файл .env на основе env.example и заполните токены")
        return False
    
    return True