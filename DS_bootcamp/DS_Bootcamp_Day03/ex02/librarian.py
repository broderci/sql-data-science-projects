
import os
import sys
import subprocess
import tarfile

def check_environment():
    """Проверка виртуального окружения"""
    if 'VIRTUAL_ENV' not in os.environ:
        raise EnvironmentError("Запустите в виртуальном окружении!")

def install_libraries():
    """Установка библиотек"""
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
                          'beautifulsoup4', 'pytest'])

def save_requirements():
    """Сохранение requirements.txt"""
    with open('requirements.txt', 'w') as f:
        subprocess.run([sys.executable, '-m', 'pip', 'freeze'], 
                      stdout=f, check=True)
    
    # Чтение и вывод
    with open('requirements.txt') as f:
        for line in sorted(f):
            print(line.strip())
            
def archive_created():
    venv_path = os.environ['VIRTUAL_ENV']
    venv_name = os.path.basename(venv_path)
    archive_name = f"{venv_name}.tar.gz"
    print(f"\nCreating archive: {archive_name}")
    
    with tarfile.open(archive_name, "w:gz") as tar:
        tar.add(venv_name, arcname=venv_name)
    
    print(f"✓ Archive created: {archive_name}")

def main():
    """Основная логика"""
    check_environment()
    install_libraries()
    save_requirements()
    archive_created()
    print("\n✓ Задание выполнено!")

if __name__ == "__main__":
    main()  # Выполняется ТОЛЬКО при прямом запуске файла