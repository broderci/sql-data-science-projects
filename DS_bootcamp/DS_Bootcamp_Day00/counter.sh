#!/bin/sh

# Проверяем наличие входного файла
if [ ! -f "../Exercise_03/hh_positions.csv" ]; then
    echo "Error: ../Exercise_03/hh_positions.csv not found. Run exercise 03 first." >&2
    exit 1
fi

# Обрабатываем файл и сохраняем результат
{
    # Сначала выводим заголовок
    echo '"name","count"'
    
    # Затем обрабатываем и сортируем данные
    awk -F',' '
    NR == 1 {  # Обрабатываем строку заголовков
        for (i = 1; i <= NF; i++) {
            gsub(/"/, "", $i)
            if ($i == "name") {
                name_col = i
            }
        }
        next
    }
    {
        gsub(/"/, "", $name_col)
        if ($name_col != "-") {
            count[$name_col]++
        }
    }
    END {
        for (name in count) {
            printf "\"%s\",%d\n", name, count[name]
        }
    }
    ' "../Exercise_03/hh_positions.csv" | sort -t',' -k2 -nr
} > hh_uniq_positions.csv

echo "Success! Results saved to hh_uniq_positions.csv"
exit 0