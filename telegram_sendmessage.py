###https://blogs.oracle.com/lad-cloud-experts-pt/post/oracle-funtions---mandando-mensagem-para-o-telegram

####https://api.telegram.org/bot5798237105:AAFXUS4RahSHZhbvSD6NyRoza59VN3c9bzA/getUpdates

###https://www.youtube.com/watch?v=7s7Ng-jBGag

import requests

    
###Telegram informations
token = '5798237105:AAFXUS4RahSHZhbvSD6NyRoza59VN3c9bzA'  ###Token BOT
chat_id = '-868572748'  ###chat ID
message = 'testando envio de mensagem cavalo'
URL = 'https://api.telegram.org/bot'+token+'/sendMessage?chat_id='+chat_id+'&text='+message
resposta = requests.get(URL)    
print(resposta.json())






