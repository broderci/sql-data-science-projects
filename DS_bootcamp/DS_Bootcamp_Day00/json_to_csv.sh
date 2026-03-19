#!/bin/sh

# # Проверяем наличие jq
# if ! command -v jq >/dev/null 2>&1; then
#     echo "Error: jq is not installed. Please install jq first." >&2
#     exit 1
# fi

# Выполняем преобразование
jq -r -f filter.jq "../Exercise_00/hh.json" > hh.csv

# Проверяем результат
if [ -s "hh.csv" ]; then
    echo "Successfully converted JSON to CSV. Result saved to hh.csv"
else
    echo "Error: Conversion failed. Output file is empty." >&2
    exit 1
fi

exit 0