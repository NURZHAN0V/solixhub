# 🤖 AI Telegram Bot

Умный Telegram бот с искусственным интеллектом для генерации изображений и чата! 🎨💬

## ✨ Возможности

- 🤖 **Чат с ИИ** - Отвечает на любые вопросы используя нейросеть
- 🎨 **Генерация изображений** - Создает картинки по текстовому описанию
- 📱 **Удобные команды** - Простой интерфейс с эмодзи
- 🔒 **Безопасность** - Токены в защищенном .env файле
- 🚀 **Простота** - Легкая установка и настройка

## 🚀 Быстрый старт

### 1. Клонирование
```bash
git clone https://github.com/your-username/tbotik.git
cd tbotik
```

### 2. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 3. Настройка токенов
```bash
# Скопируйте пример файла
cp env.example .env

# Отредактируйте .env и добавьте ваши токены
```

### 4. Запуск
```bash
python bot.py
```

## 🔑 Получение токенов

### Telegram Bot Token
1. Найдите @BotFather в Telegram
2. Отправьте `/newbot`
3. Следуйте инструкциям
4. Скопируйте токен

### OpenRouter API Key
1. Зарегистрируйтесь на [openrouter.ai](https://openrouter.ai)
2. Создайте API ключ
3. Скопируйте ключ

### NeuroImg API Key
1. Зарегистрируйтесь на [neuroimg.art](https://neuroimg.art)
2. Получите API ключ
3. Скопируйте ключ

## 📱 Использование

### Команды бота
- `/start` - Приветствие и описание возможностей
- `/help` - Подробная справка
- `/draw [описание]` - Создать картинку

### Примеры
```
/draw красивая кошка на закате
/draw космический корабль в стиле аниме
/draw портрет человека в стиле Ван Гога
```

### Чат с ИИ
Просто напишите любой вопрос, и бот ответит используя нейросеть!

## 📁 Структура проекта

```
tbotik/
├── bot.py              # Основной файл бота
├── config.py           # Конфигурация и токены
├── requirements.txt    # Зависимости Python
├── env.example         # Пример файла окружения
├── .gitignore          # Исключения Git
├── README.md           # Этот файл
├── images/             # Папка для сохранения сгенерированных изображений
└── docs/               # Документация
    ├── README.md       # Главная страница документации
    ├── installation-beginner.md
    ├── installation-developer.md
    ├── user-guide.md
    ├── project-structure.md
    ├── bot-commands.md
    ├── api-integrations.md
    ├── configuration.md
    └── troubleshooting.md
```

## 📚 Документация

Полная документация находится в папке [`docs/`](docs/README.md):

- 🚀 [Установка для начинающих](docs/installation-beginner.md)
- 🔧 [Установка для разработчиков](docs/installation-developer.md)
- 📖 [Руководство пользователя](docs/user-guide.md)
- 📁 [Структура проекта](docs/project-structure.md)
- 📱 [Команды бота](docs/bot-commands.md)
- 🔌 [API интеграции](docs/api-integrations.md)
- ⚙️ [Конфигурация](docs/configuration.md)
- 🔧 [Устранение неполадок](docs/troubleshooting.md)

## 🛠️ Технологии

- **Python 3.8+** - основной язык
- **pyTelegramBotAPI** - работа с Telegram
- **OpenRouter API** - доступ к ИИ моделям
- **NeuroImg API** - генерация изображений
- **aiohttp** - асинхронные запросы
- **python-dotenv** - управление переменными окружения

## 🔒 Безопасность

- Токены хранятся в `.env` файле (не в коде)
- Файл `.env` исключен из Git через `.gitignore`
- Пример структуры в `env.example`
- Валидация входных данных
- Обработка ошибок API

## 🚀 Развертывание

### Локально
```bash
python bot.py
```

### Docker
```bash
docker build -t tbotik .
docker run -e TELEGRAM_BOT_TOKEN=your_token tbotik
```

### Docker Compose
```bash
docker-compose up -d
```

## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте ветку для новой функции
3. Внесите изменения
4. Создайте Pull Request

## 📄 Лицензия

Этот проект распространяется под лицензией MIT. См. файл [LICENSE](LICENSE) для подробностей.

## 🆘 Поддержка

Если у вас возникли проблемы:

1. Проверьте [руководство по устранению неполадок](docs/troubleshooting.md)
2. Изучите [техническую документацию](docs/api-integrations.md)
3. Создайте [issue](https://github.com/your-username/tbotik/issues)

## 📊 Статистика

- ⭐ Звезды: [![GitHub stars](https://img.shields.io/github/stars/your-username/tbotik.svg)](https://github.com/your-username/tbotik/stargazers)
- 🔄 Форки: [![GitHub forks](https://img.shields.io/github/forks/your-username/tbotik.svg)](https://github.com/your-username/tbotik/network)
- 🐛 Issues: [![GitHub issues](https://img.shields.io/github/issues/your-username/tbotik.svg)](https://github.com/your-username/tbotik/issues)

## 🙏 Благодарности

- [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) - библиотека для Telegram ботов
- [OpenRouter](https://openrouter.ai) - доступ к ИИ моделям
- [NeuroImg](https://neuroimg.art) - генерация изображений

---

**Версия**: 1.0.0  
**Автор**: AI Assistant  
**Последнее обновление**: 2024 