import os
from random import randint

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
            raise FileNotFoundError("Error: There is no file at your address")
        except PermissionError:
            raise PermissionError("Error: No permission to access the file for reading")
        except Exception as err:
            raise err
        

        header = lines[0].strip().split(',')
        if len(header) == 2 and ((header[0].strip() == "0" and header[1].strip() == "1") or 
                               (header[0].strip() == "1" and header[1].strip() == "0")):
            has_header = False
            start_step = 0
        

        for line_str in lines[start_step:]:
            line = line_str.strip().split(',')
            if len(line) != 2 or not ((line[0].strip() == "0" and line[1].strip() == "1") or 
                                    (line[0].strip() == "1" and line[1].strip() == "0")):
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
                    heads += 1
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

class Analytics(Research.Calculations):
    def __init__(self, data):
        self.data = data
        
    def predict_random(self, num_predictions):
        predictions = []
        for _ in range(num_predictions):
            head = randint(0, 1)
            tail = 1 - head
            predictions.append([head, tail])
        return predictions
    
    def predict_last(self):
        if not self.data:
            raise ValueError("No data available")
        return self.data[-1]
    
    def save_file(self, data, filename, extension='txt'):
        """Сохраняет данные в файл с заданным расширением"""
        full_filename = f"{filename}.{extension}"
        
        try:
            with open(full_filename, 'w') as file:
                file.write(str(data))
        except Exception as e:
            raise Exception(f"Error saving file: {e}")