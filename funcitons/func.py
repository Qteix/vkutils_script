import json
import requests

client = requests.Session()

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}


def config_open():
    """
    Checks if a config has been created. It is also used for authorization
    """
    with open('config.json', 'r', encoding='utf-8') as f:
        CONFIG = json.load(f)
    return CONFIG




def config_write():
    """
    Writes data to the config
    """
    LOGIN_VK = input('Введите ваш логин от вк: ')
    PASSWORD_VK = input('Введите ваш пароль от вк: ')
    TOKEN_VK = input('Введите ваш токен от вк: ')

    with open('config.json', 'w', encoding='utf-8') as f:
        DATA = {
            'TOKEN_VK': f'{TOKEN_VK}',
            'LOGIN_VK': f'{LOGIN_VK}',
            'PASSWORD_VK': f'{PASSWORD_VK}'
        }
        json.dump(DATA, f, ensure_ascii=True)


def auth():
    """
    Authorizes on vkutils
    """
    cfg = config_open()
    return client.post(
        'https://vkutils.ru/authnew.php?type=pass&app=',
        params={
            'log': f'{cfg["LOGIN_VK"]}',
            'pass': f'{cfg["PASSWORD_VK"]}'
        },
        headers=header
    ).text

def auth_vkutils():
    print('Пробую авторизироваться на vkutils...')
    if auth() == 'incorrect':
        print('Возникла ошибка при авторизации на vkutils')
    else:
        print('Авторизация прошла успешно')


def upload_audio(from_id: int = None, peer_id: int = None, audio_link: str = None):
    """
    Uploads and sends audio as a voice message
    -param from_id: The ID of the user from whom the message was sent
    -param peer_id: Chat ID
    -param audio_link: Link to the audio you want to send as a voice message
    """
    client.post(
        'https://vkutils.ru/audiomsgupload.php',
        data={
            'group': '0',
            'uid': peer_id,
            'id': from_id,
            'dialog': '',
            'disren': 'on',
            'subm': 'Загрузить'
        },
        headers=header,
        files={
            'filename': client.get(audio_link).content
        }
    )

auth()


start_text = """
██╗░░░██╗██╗░░██╗██╗░░░██╗████████╗██╗██╗░░░░░░██████╗  ░██████╗░█████╗░██████╗░██╗██████╗░████████╗
██║░░░██║██║░██╔╝██║░░░██║╚══██╔══╝██║██║░░░░░██╔════╝  ██╔════╝██╔══██╗██╔══██╗██║██╔══██╗╚══██╔══╝
╚██╗░██╔╝█████═╝░██║░░░██║░░░██║░░░██║██║░░░░░╚█████╗░  ╚█████╗░██║░░╚═╝██████╔╝██║██████╔╝░░░██║░░░
░╚████╔╝░██╔═██╗░██║░░░██║░░░██║░░░██║██║░░░░░░╚═══██╗  ░╚═══██╗██║░░██╗██╔══██╗██║██╔═══╝░░░░██║░░░
░░╚██╔╝░░██║░╚██╗╚██████╔╝░░░██║░░░██║███████╗██████╔╝  ██████╔╝╚█████╔╝██║░░██║██║██║░░░░░░░░██║░░░
░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░╚═╝╚══════╝╚═════╝░  ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░

██████╗░██╗░░░██╗  ░██████╗░████████╗███████╗██╗██╗░░██╗
██╔══██╗╚██╗░██╔╝  ██╔═══██╗╚══██╔══╝██╔════╝██║╚██╗██╔╝
██████╦╝░╚████╔╝░  ██║██╗██║░░░██║░░░█████╗░░██║░╚███╔╝░
██╔══██╗░░╚██╔╝░░  ╚██████╔╝░░░██║░░░██╔══╝░░██║░██╔██╗░
██████╦╝░░░██║░░░  ░╚═██╔═╝░░░░██║░░░███████╗██║██╔╝╚██╗
╚═════╝░░░░╚═╝░░░  ░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚═╝╚═╝░░╚═╝
"""