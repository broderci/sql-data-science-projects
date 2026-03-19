# Параметры для предсказаний
num_of_steps = 3

# Шаблон отчета
report_template = """Report

We made {total_observations} observations by tossing a coin: {tails} were tails and {heads} were heads.
The probabilities are {tails_pct:.2f}% and {heads_pct:.2f}%, respectively.
Our forecast is that the next {num_predictions} observations will be: {tail_predictions} tail and {head_predictions} heads."""


# Настройки для Telegram
TELEGRAM_BOT_TOKEN = ('8343429182:AAGohS_ujnC67uBUxz4Ohtk663PUWVB4t6I')
TELEGRAM_CHAT_ID = '693736789'
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"

# Настройки логирования
LOG_FILE = 'analytics.log'
LOG_FORMAT = '%(asctime)s %(message)s'
LOG_DATE_FORMAT = '%Y-%m-%d %H:%M:%S'