class Research:
    def file_reader(self):
        """Метод читает файл и возвращает его содержимое, в виде строки"""
        try:
            with open("data.csv", "r") as file:
                content = file.read()
            return content
        except FileNotFoundError:
            return "File data.csv not found"
        except Exception as e:
            return f"Error: {e}"
        
if __name__ == "__main__":
    try:
        research = Research()
        print(research.file_reader())
    except Exception as e:
        print(f"Error: {e}")