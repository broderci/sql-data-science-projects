#!/bin/sh

# Проверка аргументов
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <vacancy_name>"
    exit 1
fi

# Кодирование параметра поиска
VACANCY_NAME=$(echo "$1" | sed 's/ /+/g')
API_URL="https://api.hh.ru/vacancies"
PARAMS="?text=${VACANCY_NAME}&per_page=20&page=0"

# Альтернативные User-Agent, которые работают с HH API
USER_AGENTS=(
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    "MyHHApp/1.0 (contact@myhhapp.com)"
    "HH-Parser/1.0"
    "curl/7.64.1"
)

# Пробуем разные User-Agent
for UA in "${USER_AGENTS[@]}"; do
    response=$(curl -s -w "\nHTTP_CODE:%{http_code}" \
                  -H "User-Agent: ${UA}" \
                  -H "HH-User-Agent: ${UA}" \
                  "${API_URL}${PARAMS}")
    
    http_code=$(echo "$response" | tail -1 | cut -d':' -f2)
    
    if [ "$http_code" -eq 200 ]; then
        json_response=$(echo "$response" | sed '$d')
        break
    fi
done

# Проверка успешности запроса
if [ "$http_code" -ne 200 ]; then
    echo "Error: All User-Agent attempts failed" >&2
    echo "Last response:" >&2
    echo "$response" >&2
    echo "Try:" >&2
    echo "1. Waiting some time and trying again" >&2
    echo "2. Using a different network connection" >&2
    echo "3. Checking if https://api.hh.ru/vacancies?text=data is accessible from your browser" >&2
    exit 1
fi

# Форматирование результата
if command -v jq >/dev/null 2>&1; then
    echo "$json_response" | jq '{
        page: .page,
        found: .found,
        per_page: .per_page,
        pages: .pages,
        items: .items
    }' > hh.json
else
    echo "$json_response" > hh.json
    echo "Warning: jq not found, JSON is not formatted" >&2
fi

echo "Success! Data saved to hh.json"
exit 0