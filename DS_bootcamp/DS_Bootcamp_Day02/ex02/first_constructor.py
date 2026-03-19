import sys

class Research:
    
    def __init__(self, file_path):
        """Constructor that takes the file path as an argument"""
        self.file_path = file_path
        
    def file_reader(self):
        """Reads the file and returns its content with validation"""
        try:
            with open (self.file_path, "r" )  as file:
                content = file.read().strip()
                return self.table_check(content)
        except Exception as err:
            print(f"exception: {err}")
        
    def table_check(self, table_str):
        """Check the file content structure"""
        table = table_str.split('\n')
        if len(table) < 2:
            raise ValueError("File must contain at least a header and one data line")
        
        header = table[0].split(',')
        if len(header) != 2:
            raise ValueError("Header must contain exactly two columns separated by comma")

        for line_str in table[1:]:
            line = line_str.strip().split(',')
            if len(line) != 2 or not ((line[0] == "0" and line[1] == '1') or (line[0] == '1' and line[1] == '0')):
                
                raise ValueError("Error: Incorrect table structure")
            
        return table_str

def main():
    try:
        if len(sys.argv) != 2:
            raise ValueError("Error: Need one argument - file path")
        
        reader = Research(sys.argv[1])
        print(reader.file_reader())
    except Exception as err:
        print(f"exception: {err}")
        return 1
    return 0

if __name__ == '__main__':
    sys.exit(main())
        
                
        
    