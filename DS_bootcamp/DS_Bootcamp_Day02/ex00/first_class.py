class Must_Read:
    """ Класс, который читает и выводит на экран содержимое файла dats.csv"""
    def __init__(self):
        try:
            with open("data.csv", "r") as file:
                print(file.read())
        except FileNotFoundError:
            print("File data.csv not found")
        except Exception as e:
            print(f"Error: {e}")
            
if __name__ == "__main__":
    reader = Must_Read()