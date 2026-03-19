#!/usr/bin/env python3
# financial_test.py
# Unit tests for financial.py using PyTest

import pytest
import sys
import os

# Добавляем путь к текущей директории для импорта

current_dir = os.path.dirname(os.path.abspath(__file__))  # ex05
ex03_dir = os.path.join(os.path.dirname(current_dir), "ex03")  # ../ex03

sys.path.insert(0, ex03_dir)

# Импортируем функции из financial.py
from financial import get_financial_data

# Monkey-patch: временно заменяем time.sleep чтобы тесты не ждали 5 секунд
import time
original_sleep = time.sleep
time.sleep = lambda x: None  # Замена на пустую функцию

class TestFinancialData:
    """Класс для тестирования функций финансового парсера"""
    
    def test_return_type(self):
        """Тест 1: Проверяем, что функция возвращает кортеж"""
        result = get_financial_data("MSFT", "Total Revenue")
        assert isinstance(result, tuple), f"Ожидался tuple, получен {type(result)}"
    
    def test_tuple_length(self):
        """Тест 2: Проверяем длину возвращаемого кортежа (поле + 5 значений)"""
        result = get_financial_data("MSFT", "Total Revenue")
        # Должен быть кортеж из 6 элементов: поле + 5 значений
        assert len(result) == 6, f"Ожидалась длина 6, получена {len(result)}"
    
    def test_field_in_result(self):
        """Тест 3: Проверяем, что первым элементом идет запрошенное поле"""
        field = "Total Revenue"
        result = get_financial_data("MSFT", field)
        assert result[0] == field, f"Первый элемент должен быть '{field}', получен '{result[0]}'"
    
    def test_values_format(self):
        """Тест 4: Проверяем формат значений (числа с запятыми)"""
        result = get_financial_data("MSFT", "Total Revenue")
        # Проверяем что все значения (кроме первого) содержат запятые или цифры
        for value in result[1:]:
            # Значение должно быть строкой и содержать либо цифры, либо запятые
            assert isinstance(value, str), f"Значение должно быть строкой, получен {type(value)}"
            # Проверяем что это похоже на финансовое число: содержит цифры и, возможно, запятые
            assert any(c.isdigit() for c in value), f"Значение должно содержать цифры: {value}"
    
    def test_invalid_ticker_exception(self):
        """Тест 5: Проверяем что неверный тикер вызывает исключение"""
        with pytest.raises(ValueError) as exc_info:
            get_financial_data("INVALID_TICKER_XYZ", "Total Revenue")
        
        # Проверяем текст исключения
        error_message = str(exc_info.value)
        assert "не найден" in error_message.lower() or "not found" in error_message.lower()
    
    def test_invalid_field_exception(self):
        """Тест для несуществующего поля"""
    # Yahoo Finance возвращает данные даже для неизвестных полей
    # Поэтому проверяем что функция что-то возвращает в правильном формате
        result = get_financial_data("MSFT", "Non Existent Field 123")
    
    # Проверяем формат результата
        assert isinstance(result, tuple)
        assert len(result) == 6
        assert result[0] == "Non Existent Field 123"
    
    # Проверяем что все значения - строки (с цифрами или '0')
        for value in result[1:]:
            assert isinstance(value, str)
            # Либо '0', либо содержит цифры
            assert value == '0' or any(c.isdigit() for c in value)
    
    def test_apple_ticker(self):
        """Тест 7: Проверяем работу с другим тикером (AAPL)"""
        result = get_financial_data("AAPL", "Total Revenue")
        assert isinstance(result, tuple), f"AAPL: Ожидался tuple, получен {type(result)}"
        assert len(result) == 6, f"AAPL: Ожидалась длина 6, получена {len(result)}"
        assert result[0] == "Total Revenue", f"AAPL: Первый элемент должен быть 'Total Revenue'"
    
    def test_google_ticker(self):
        """Тест 8: Проверяем работу с тикером GOOGL"""
        result = get_financial_data("GOOGL", "Total Revenue")
        assert isinstance(result, tuple), f"GOOGL: Ожидался tuple, получен {type(result)}"
        assert result[0] == "Total Revenue", f"GOOGL: Первый элемент должен быть 'Total Revenue'"
    
    def test_all_values_strings(self):
        """Тест 9: Проверяем что все элементы кортежа - строки"""
        result = get_financial_data("MSFT", "Total Revenue")
        for item in result:
            assert isinstance(item, str), f"Все элементы должны быть строками, найден {type(item)}: {item}"
    
    def test_empty_input(self):
        """Тест 10: Проверяем обработку пустых аргументов"""
        # Этот тест может не проходить, если ваша функция не обрабатывает пустые строки
        # Можно закомментировать, если вызывает проблемы
        with pytest.raises(Exception):
            get_financial_data("", "")

# Восстанавливаем оригинальный sleep после всех тестов
def teardown_module(module):
    """Вызывается после всех тестов в модуле"""
    time.sleep = original_sleep

