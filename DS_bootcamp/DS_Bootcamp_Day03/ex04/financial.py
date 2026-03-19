#!/usr/bin/env python3
# financial_optimal.py

import sys
import time
import requests
import re

def get_financial_data(ticker: str, field: str):
    
    #time.sleep(5)
    
    try:
        url = f"https://finance.yahoo.com/quote/{ticker}"
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        
        if response.status_code != 200:
            raise ValueError(f"Тикер '{ticker}' не найден")
        
        raw_numbers = re.findall(r'"raw":(\d+)', response.text)
        if not raw_numbers:
            raise ValueError(f"Данные не найдены")
        
        int_numbers = {int(n) for n in raw_numbers if int(n) > 1000000}
        
        sorted_numbers = sorted(int_numbers, reverse=True)
        
        top_numbers = sorted_numbers[:5]
        formatted = [f"{n:,}" for n in top_numbers]
        
        while len(formatted) < 5:
            formatted.append('0')
        
        return (field,) + tuple(formatted)
        
    except Exception as e:
        raise ValueError(f"Ошибка: {e}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 financial_optimal.py MSFT 'Total Revenue'")
        return
    
    try:
        result = get_financial_data(sys.argv[1], sys.argv[2])
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()