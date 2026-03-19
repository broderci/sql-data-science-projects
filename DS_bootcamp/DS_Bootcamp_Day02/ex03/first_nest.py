import sys

class Research:
    def __init__(self, file_path):
        self.file_path = file_path
        
    def file_reader(self):
        has_header = True
        data = []
        start_step = 1
        try:
            with open(self.file_path, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            raise FileNotFoundError ("Error: There is no file at your address")
        except PermissionError:
            raise PermissionError ("Error: No permission to access the file for reading")
        except Exception as err:
            raise err
        
        header = lines[0].split(',')
        if (header[0] == '0' and header[1] == '1') or (header[0] == '1' and header[1] == '0'):
            has_header = False
            start_step = 0
        
        for line_str in lines[start_step:]:
            line = line_str.strip().split(',')
            if len(line) != 2:
                ((line[0] == "0" and line[1] == '1') or (line[0] == '1' and line[1] == '0'))
                raise ValueError("Error: Incorrect table structure")
            val1 = int(line[0])
            val2 = int(line[1])
            data.append([val1, val2])
        return data

        
    class Calculations:
        
        def counts(self, data):
            heads = 0
            tails = 0
            
            for row in data:
                if row[0] == 1:
                    heads +=1
                if row[1] == 1:
                    tails += 1
            return heads, tails
            
        def fractions(self, heads_count, tails_count):
            total = heads_count + tails_count
            if total == 0:
                return 0, 0
            
            heads_frac = heads_count / total
            tails_frac = tails_count / total
            
            return heads_frac, tails_frac
        

            
            
def main():
    try:
        if len(sys.argv) != 2:
            raise ValueError("Error: Need one argument - file path")
        
        research = Research(sys.argv[1])
        data = research.file_reader()
        print(data)
        
        
        calculator = research.Calculations()
        
        heads, tails = calculator.counts(data)
        print(heads, tails)
        
        
        heads_frac, tails_frac = calculator.fractions(heads, tails)
        print(f"{heads_frac:.4f} {tails_frac:.4f}")
        
        return 0
        
    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())