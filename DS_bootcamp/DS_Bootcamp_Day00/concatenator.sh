#!/bin/sh

# Проверяем наличие файлов партиций
if [ ! -d "partitions" ] || [ -z "$(ls -A partitions)" ]; then
    echo "Error: No partition files found. Run partitioner.sh first." >&2
    exit 1
fi

# Создаем итоговый файл
output_file="hh_concatenated.csv"

# Записываем заголовки из первого файла (все файлы имеют одинаковые заголовки)
head -n 1 partitions/part_*.csv | head -n 1 > "$output_file"

# Объединяем все файлы, исключая заголовки
for file in partitions/part_*.csv; do
    tail -n +2 "$file" >> "$output_file"
done

echo "Success! All partitions concatenated into $output_file"
exit 0