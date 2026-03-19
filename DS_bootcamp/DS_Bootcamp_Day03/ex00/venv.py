

import os

def get_virtual_env_path():
    venv_path = os.environ.get('VIRTUAL_ENV')
    return venv_path

def main():
    current_venv = get_virtual_env_path()
    if current_venv:
        print(f'Your current virtual env is {current_venv}')
    else:
        print('No virtual environment is currently active')
        
if __name__ == "__main__":
    main()