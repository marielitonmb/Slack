import requests
import json

# Constantes
slack_token = '<token>'
slack_canal = '#<nome do canal>'
slack_id_canal = '<id do canal>' # dá pra usar o nome do canal e o ID
slack_icon_emoji = ':hospital:'
slack_usuario = '<nome do usuário>'

# Função que posta diretamente num canal do Slack
def postar_mensagem_no_slack(texto, blocks = None):
    return requests.post('https://slack.com/api/chat.postMessage', {
        'token': slack_token,
        'channel': slack_id_canal,
        'text': texto,
        'icon_emoji': slack_icon_emoji, # sem esse parâmetro o ícone do bot é usado
        'username': slack_usuario,
        'blocks': json.dumps(blocks) if blocks else None
    }).json()

slack_msg = 'Mensagem de Teste'

postar_mensagem_no_slack(slack_msg)
