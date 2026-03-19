import sys

def find_name_to_email(email):
    try:
        with open("employees.tsv", 'r') as f:
            lines = f.readlines()
            
        for line in lines[1:]:
            name, surname, current_email = line.strip().split("\t")
            if current_email == email:
                return name
            return None
        
    except FileNotFoundError:
        print("Error: employees.tsv not found. Run names_extractor.py first.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None    
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python letter_starter.py <email>")
        return
    
    email = sys.argv[1].strip()
    name = find_name_to_email(email)
    
    if name:
        print(f"Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with you. That’s a precondition for the professionals that our company hires.")
    else:
        print(f"No employee found with email: {email}")
        
if __name__ == "__main__":
    main()
