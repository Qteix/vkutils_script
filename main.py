from vkbottle.user import User, Message
from funcitons.func import *
from loguru import logger

# Modules

logger.disable('vkbottle')

try:
    print(start_text)
    print('Попытка загрузить конфиг...')
    config_open()
    print('Конфиг успешно загружен')
    auth_vkutils()
except:
    print('Конфиг не найден, заполните данные:')
    config_write()
    auth_vkutils()

app = User(config_open()['TOKEN_VK'])


# Bot

logger.success('Бот успешно запущен')

@app.on.message(text='вгс')
async def audio_to_audiomessage(ctx: Message):
    logger.debug('Выполнение комманды...')
    try:
        AUDIO_LINK = ctx.reply_message.attachments[0].audio.url
        upload_audio(
                from_id=ctx.from_id,
                peer_id=ctx.peer_id,
                audio_link=AUDIO_LINK
            )
        logger.success('Комманда была успешно выполнена')
    except Exception as e:
        logger.error(f'Произошла ошибка: {e}')


app.run_forever()