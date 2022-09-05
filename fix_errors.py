import os
import time

try:
    print('Идет проверка модулей')
    import vkbottle
    import requests
    import loguru
    print('Все модули установлены, запускаю бота.')
    os.system('py main.py')
except ModuleNotFoundError:
    installer = input(f"""
У вас не установлен модуль
Введите Вашу операционную систему:
1. Termux
2. Windows
3. Ubuntu (VDS)    
""")

    pip = 'pip'

    if int(installer) == 1:
        pip = 'pip'
    elif int(installer) == 2:
        pip = 'pip'
    elif int(installer) == 3:
        pip = 'pip3'

    print("Package manager. Downloading packages", )
    os.system(f"{pip} install --upgrade pip")
    print("Download package 'requests' ")
    time.sleep(1)
    os.system(f"{pip} install requests")
    os.system("clear" if int(installer) == 1 or int(installer) == 3 else "cls")
    print("Download package 'loguru' ")
    time.sleep(1)
    os.system(f"{pip} install loguru")
    os.system("clear" if int(installer) == 1 or int(installer) == 3 else "cls")
    print("Download package 'vkbottle' ")
    time.sleep(1)
    os.system(f"{pip} install -U https://github.com/vkbottle/vkbottle/archive/master.zip")
    os.system("clear" if int(installer) == 1 or int(installer) == 3 else "cls")
    print("Complete download packages. "
            "\nStarting bot...")
    time.sleep(3)

    if int(installer) != 3:
        os.system("py main.py")
    os.system('python3 main.py')