###código com as duas funções juntas

import telepot
import requests

###Telegram informations
token = '<TOKEN DO BOT'  ###Token BOT
chat_id = '<CHAT ID'  ###chat ID


###enviando mensagem telegram
def TELEGRAM_MSG():    
    message = "Sua mensagem" ###Mensagem
    URL = 'https://api.telegram.org/bot'+token+'/sendMessage?chat_id='+chat_id+'&text='+message  ##URL de chamada
    resposta = requests.get(URL)

###enviando doc telegram
def TELEGRAM_DOC():
    bot = telepot.Bot(token)
    file="screenshot.png"
    bot.sendDocument(chat_id=chat_id, document=open(file, 'rb'))
    

##chamando as funções
TELEGRAM_MSG()
TELEGRAM_DOC()

    
