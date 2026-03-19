#!/bin/sh

# Проверяем наличие входного файла
if [ ! -f "../Exercise_03/hh_positions.csv" ]; then
    echo "Error: ../Exercise_03/hh_positions.csv not found. Run exercise 03 first." >&2
    exit 1
fi

# Создаем директорию для партиций (если не существует)
mkdir -p partitions

# Обрабатываем файл
awk -F',' '
BEGIN {
    OFS=","
}
NR == 1 {
    # Сохраняем заголовки
    header = $0
    # Находим столбец created_at
    for (i=1; i<=NF; i++) {
        gsub(/"/, "", $i)
        if ($i == "created_at") {
            created_at_col = i
        }
    }
    next
}
{
    # Извлекаем дату из created_at (формат: 2020-04-11T18:03:53+0300)
    split($created_at_col, dtparts, /T|"/)
    date = dtparts[2]
    
    # Формируем имя файла
    filename = "partitions/part_" date ".csv"
    
    # Если файл еще не создан, записываем заголовки
    if (!(date in files_created)) {
        print header > filename
        files_created[date] = 1
    }
    
    # Записываем строку в соответствующий файл
    print $0 >> filename
}
' "../Exercise_03/hh_positions.csv"

echo "Success! Data partitioned into files in partitions/"
exit 0