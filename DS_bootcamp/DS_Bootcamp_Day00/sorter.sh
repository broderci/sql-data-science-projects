#!/bin/sh


# Сохраняем заголовки (первую строку)
HEADERS=$(head -n 1 "../Exercise_01/hh.csv")

# Сортируем данные (начиная со второй строки)
tail -n +2 "../Exercise_01/hh.csv" | sort -t',' -k2,2 -k1,1 > hh_sorted_temp.csv

# Объединяем заголовки и отсортированные данные
echo "$HEADERS" > hh_sorted.csv
cat hh_sorted_temp.csv >> hh_sorted.csv

# Удаляем временный файл
rm hh_sorted_temp.csv

echo "Successfully sorted. Result saved to hh_sorted.csv"
exit 0