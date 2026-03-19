
import sys
import time
import requests
import re

def get_financial_data(ticker: str, field: str):
    
    time.sleep(5)  
    
    try:
        url = f"https://finance.yahoo.com/quote/{ticker}"
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
        response = requests.get(url, headers=headers, timeout=10)
        
        # Проверка невалидного тикера
        if "Symbol Lookup" in response.text and "We could not find any results" in response.text:
            raise ValueError(f"Тикер '{ticker}' не найден")
        
        # Проверка статуса кода
        if response.status_code != 200:
            raise ValueError(f"Тикер '{ticker}' не найден. HTTP код: {response.status_code}")
        
        # Дополнительная проверка: тикер должен быть на странице
        if ticker.upper() not in response.text and ticker not in response.text:
            raise ValueError(f"Тикер '{ticker}' не найден на странице")
        
        # Ищем raw данные
        raw_numbers = re.findall(r'"raw":(\d+)', response.text)
        
        # Проверка невалидного поля
        if not raw_numbers:
            if field.lower() in response.text.lower():
                # Поле есть, но данных нет
                raise ValueError(f"Финансовые данные для поля '{field}' не найдены")
            else:
                # Поле вообще не упоминается
                raise ValueError(f"Поле '{field}' не найдено на странице")
        
        # Обрабатываем найденные числа
        int_numbers = {int(n) for n in raw_numbers if int(n) > 1000000}
        
        # Если после фильтрации чисел нет
        if not int_numbers:
            raise ValueError(f"Не найдено подходящих финансовых данных для поля '{field}'")
        
        # Сортируем и форматируем
        sorted_numbers = sorted(int_numbers, reverse=True)
        top_numbers = sorted_numbers[:5]
        formatted = [f"{n:,}" for n in top_numbers]
        
        # Дополняем если нужно
        while len(formatted) < 5:
            formatted.append('0')
        
        return (field,) + tuple(formatted)
        
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Ошибка сети: {e}")
    except Exception as e:
        raise ValueError(f"Ошибка: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 financial_optimal.py <ticker> '<field>'")
        print("Example: python3 financial_optimal.py MSFT 'Total Revenue'")
        return
    
    try:
        result = get_financial_data(sys.argv[1], sys.argv[2])
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()