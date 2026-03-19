import sys

def has_cyrillic(text):
    """Проверяет кириллицу через десятичные коды Unicode"""
    for char in text:
        code = ord(char)
        if 1024 <= code <= 1279:  # Диапазон кириллицы в десятичной системе
            return True
    return False

def apply_caesar(text, shift, operation):
    """Применяет шифр Цезаря к тексту"""
    result = []
    shift = shift % 26  # Нормализуем сдвиг
    
    for char in text:
        if 'a' <= char <= 'z':
            base = ord('a')
            new_pos = (ord(char) - base + (shift if operation == 'encode' else -shift)) % 26
            result.append(chr(base + new_pos))
        elif 'A' <= char <= 'Z':
            base = ord('A')
            new_pos = (ord(char) - base + (shift if operation == 'encode' else -shift)) % 26
            result.append(chr(base + new_pos))
        else:
            result.append(char)
    return ''.join(result)

def main():
    try:
        # Проверяем количество аргументов
        if len(sys.argv) != 4:
            raise ValueError("Использование: python caesar.py [encode|decode] 'текст' сдвиг")
        
        operation = sys.argv[1]
        text = sys.argv[2]
        
        # Проверяем правильность операции
        if operation not in ('encode', 'decode'):
            raise ValueError("Первый аргумент должен быть 'encode' или 'decode'")
        
        # Проверяем на кириллицу
        if has_cyrillic(text):
            raise ValueError("Скрипт пока не поддерживает кириллицу")
        
        # Проверяем что сдвиг - число
        try:
            shift = int(sys.argv[3])
        except ValueError:
            raise ValueError("Сдвиг должен быть целым числом")
        
        # Применяем шифр и выводим результат
        result = apply_caesar(text, shift, operation)
        print(result)
        
    except ValueError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()