import sys

def change_email(email):
    email = email.strip()
    if not email:
        return None
    name_surname = email.split('@')[0]
    name, surname = name_surname.split('.')
    name = name.capitalize()
    surname = name.capitalize()
    return (name, surname, email)

def main():
    if len(sys.argv) != 2:
        print("Usage: python names_extractor.py <input_file>")
        return
    input_file = sys.argv[1]
    output_file =  "employees.tsv"
    
    try:
        with open (input_file, 'r') as f:
            emails = f.readlines()  #список строк
        
        list_info = [change_email(email) for email in emails]
            
        with open (output_file, 'w') as f:
            f.write("Name\tSurname\tE-mail\n")
            for entry in list_info:
                f.write(f"{entry[0]}\t{entry[1]}\t{entry[2]}\n")
        
        print(f"Data successfully written to {output_file}")
    
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
            