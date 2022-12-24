###código para enviar arquivos pelo Telegram

import telepot
    
###Telegram informations
token = '<TOKEN DO BOT'  ###Token BOT
chat_id = '<CHAT ID'  ###chat ID

###Enviar arquivo
bot = telepot.Bot(token)
file="screenshot.png"  ##nesse caso o arquivo está no mesmo diretório do código
bot.sendDocument(chat_id=chat_id, document=open(file, 'rb'))
