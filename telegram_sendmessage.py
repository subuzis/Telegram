import requests

    
###Telegram informations
token = '<TOKEN DO BOT'  ###Token BOT
chat_id = '<CHAT ID'  ###chat ID
message = 'testando envio de mensagem cavalo'
URL = 'https://api.telegram.org/bot'+token+'/sendMessage?chat_id='+chat_id+'&text='+message
resposta = requests.get(URL)    
print(resposta.json())






