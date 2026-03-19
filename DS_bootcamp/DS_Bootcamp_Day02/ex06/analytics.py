import os
import logging
from random import randint

# Пытаемся импортировать requests, но если нет - работаем без него
try:
    import requests
    import json
    REQUESTS_AVAILABLE = True
    logging.debug("Requests library is available")
except ImportError:
    REQUESTS_AVAILABLE = False
    logging.warning("Requests library not available - Telegram messages will be simulated")

# Настройка логирования
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='analytics.log',
    filemode='a'
)

class Research:
    def __init__(self, file_path):
        self.file_path = file_path
        logging.debug(f"Research class initialized with file: {file_path}")
        
    def file_reader(self):
        logging.debug("Starting file_reader method")
        has_header = True
        data = []
        start_step = 1
        
        try:
            logging.debug(f"Attempting to open file: {self.file_path}")
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
            logging.debug(f"Successfully read {len(lines)} lines from file")
        except FileNotFoundError:
            logging.error(f"File not found: {self.file_path}")
            raise FileNotFoundError("Error: There is no file at your address")
        except PermissionError:
            logging.error(f"Permission denied for file: {self.file_path}")
            raise PermissionError("Error: No permission to access the file for reading")
        except Exception as err:
            logging.error(f"Unexpected error reading file: {err}")
            raise err
        
        # Автоопределение заголовка
        header = lines[0].strip().split(',')
        if len(header) == 2 and ((header[0].strip() == "0" and header[1].strip() == "1") or 
                               (header[0].strip() == "1" and header[1].strip() == "0")):
            has_header = False
            start_step = 0
            logging.debug("No header detected - reading all lines as data")
        else:
            logging.debug("Header detected - skipping first line")
        
        # Обработка данных
        for i, line_str in enumerate(lines[start_step:], start_step + 1):
            line = line_str.strip().split(',')
            if len(line) != 2 or not ((line[0].strip() == "0" and line[1].strip() == "1") or 
                                    (line[0].strip() == "1" and line[1].strip() == "0")):
                logging.error(f"Incorrect table structure at line {i}: {line}")
                raise ValueError("Error: Incorrect table structure")
            
            val1 = int(line[0])
            val2 = int(line[1])
            data.append([val1, val2])
        
        logging.debug(f"Successfully processed {len(data)} data rows")
        return data

    def send_telegram_message(self, success=True):
        
        """Умная функция Telegram - работает если есть requests, иначе симулирует"""
        logging.debug("Attempting to send Telegram message")
        
        if success:
            message = "The report has been successfully created"
        else:
            message = "The report hasn't been created due to an error"
        
        # Если requests доступен - отправляем настоящее сообщение
        if REQUESTS_AVAILABLE:
            try:
                # Используем переменные окружения или значения по умолчанию
                bot_token = os.getenv('TELEGRAM_BOT_TOKEN', 'test_token')
                chat_id = os.getenv('TELEGRAM_CHAT_ID', 'test_chat_id')
                
                telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
                
                payload = {
                    'chat_id': chat_id,
                    'text': message,
                    'parse_mode': 'HTML'
                }
                
                response = requests.post(telegram_url, data=payload, timeout=10)
                
                if response.status_code == 200:
                    logging.info(f"Telegram message sent successfully: {message}")
                    print(f"✅ Telegram message sent: {message}")
                else:
                    logging.warning(f"Telegram API error: {response.status_code}")
                    print(f"⚠️ Telegram message simulated (API error): {message}")
                    
            except Exception as e:
                logging.error(f"Failed to send Telegram message: {e}")
                print(f"⚠️ Telegram message simulated (error): {message}")
        
        # Если requests не доступен - симулируем отправку
        else:
            logging.info(f"TELEGRAM SIMULATED: {message}")
            print(f"📱 Telegram message simulated (no requests lib): {message}")

    class Calculations:
        def counts(self, data):
            logging.debug("Calculating the counts of heads and tails")
            heads = 0
            tails = 0
            
            for row in data:
                if row[0] == 1:
                    heads += 1
                if row[1] == 1:
                    tails += 1
            
            logging.debug(f"Counts calculated: {heads} heads, {tails} tails")
            return heads, tails
            
        def fractions(self, heads_count, tails_count):
            logging.debug("Calculating fractions as percentages")
            total = heads_count + tails_count
            if total == 0:
                logging.warning("No data available for fraction calculation")
                return 0, 0
            
            heads_frac = heads_count / total
            tails_frac = tails_count / total
            
            logging.debug(f"Fractions calculated: {heads_frac:.4f} heads, {tails_frac:.4f} tails")
            return heads_frac, tails_frac

class Analytics(Research.Calculations):
    def __init__(self, data):
        logging.debug("Analytics class initialized")
        self.data = data
        
    def predict_random(self, num_predictions):
        logging.debug(f"Generating {num_predictions} random predictions")
        predictions = []
        
        for i in range(num_predictions):
            head = randint(0, 1)
            tail = 1 - head
            predictions.append([head, tail])
            logging.debug(f"Prediction {i+1}: [{head}, {tail}]")
        
        logging.debug(f"Generated {len(predictions)} predictions")
        return predictions
    
    def predict_last(self):
        logging.debug("Retrieving last prediction from data")
        if not self.data:
            logging.error("No data available for predict_last")
            raise ValueError("No data available")
        
        last_item = self.data[-1]
        logging.debug(f"Last prediction: {last_item}")
        return last_item
    
    def save_file(self, data, filename, extension='txt'):
        """Сохраняет данные в файл с заданным расширением"""
        logging.debug(f"Attempting to save file: {filename}.{extension}")
        
        full_filename = f"{filename}.{extension}"
        
        try:
            with open(full_filename, 'w') as file:
                file.write(str(data))
            logging.info(f"File saved successfully: {full_filename}")
            print(f"✅ File saved: {full_filename}")
        except Exception as e:
            logging.error(f"Error saving file {full_filename}: {e}")
            raise Exception(f"Error saving file: {e}")