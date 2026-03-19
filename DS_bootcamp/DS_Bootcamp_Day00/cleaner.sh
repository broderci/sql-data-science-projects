#!/bin/sh

# # Проверяем наличие входного файла
# if [ ! -f "../Exercise_02/hh_sorted.csv" ]; then
#     echo "Error: ../Exercise_02/hh_sorted.csv not found. Run exercise 02 first." >&2
#     exit 1
# fi

# Создаем временный файл для обработки
temp_file=$(mktemp)

# Обрабатываем CSV файл
awk -F',' 'BEGIN {OFS=","} {
    if (NR == 1) {
        # Находим индекс колонки "name" в заголовке
        for (i=1; i<=NF; i++) {
            if ($i == "\"name\"") {
                name_col = i
            }
        }
        print $0  # Печатаем заголовки без изменений
    } else {
        # Извлекаем уровень из названия позиции
        level = "-"
        if (match($name_col, /[Jj]unior/)) {
            level = "Junior"
        }
        if (match($name_col, /[Mm]iddle/)) {
            level = (level == "-") ? "Middle" : level "/Middle"
        }
        if (match($name_col, /[Ss]enior/)) {
            level = (level == "-") ? "Senior" : level "/Senior"
        }
        
        # Заменяем название позиции на уровень
        $name_col = "\"" level "\""
        print $0
    }
}' "../Exercise_02/hh_sorted.csv" > "$temp_file"

# Сохраняем результат
mv "$temp_file" hh_positions.csv

echo "Successfully processed. Result saved to hh_positions.csv"
exit 0