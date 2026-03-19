def csv_to_tsv(input_file, output_file):
    """
    Читает CSV-файл, заменяет разделители на табы и сохраняет как TSV.
    Учитывает запятые внутри полей (заключённые в кавычки).
    """
    with open(input_file, 'r', encoding='utf-8') as csv_file:
        with open(output_file, 'w', encoding='utf-8') as tsv_file:
            for line in csv_file:
                # Разбиваем строку с учётом кавычек
                fields = []
                field = []
                in_quotes = False
                
                for char in line.strip('\n'):
                    if char == '"':
                        in_quotes = not in_quotes
                    elif char == ',' and not in_quotes:
                        fields.append(''.join(field))
                        field = []
                        continue
                    field.append(char)
                
                fields.append(''.join(field))  # Добавляем последнее поле
                
                # Соединяем поля через табуляцию
                tsv_file.write('\t'.join(fields) + '\n')

def main():
    input_filename = 'ds.csv'
    output_filename = 'ds.tsv'
    
    try:
        csv_to_tsv(input_filename, output_filename)
        print(f"Success! File '{output_filename}' has been created.")
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    main()