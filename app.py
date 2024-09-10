import ssl, time
import config as cq
from slack_sdk import WebClient
from slack_sdk.socket_mode import SocketModeClient
from slack_sdk.socket_mode.request import SocketModeRequest
from slack_sdk.socket_mode.response import SocketModeResponse

def event_handler(client: SocketModeClient, req: SocketModeRequest):
    if req.type == "events_api":
        client.send_socket_mode_response(SocketModeResponse(envelope_id=req.envelope_id))
        event = req.payload['event']
        if event['type'] == "channel_created":
            channel_id = event['channel']['id']
            try:
                response = action_client.conversations_join(channel=channel_id)
                print(f"Entrou no canal: {response['channel']['name']}")
                mensagem = f"Diversibot entrou no canal: {response['channel']['name']}"
                enviaSlack(mensagem)
            except Exception as e:
                print(f"Erro ao entrar no canal: {str(e)}")
                mensagem = f'O Diversibot não foi incluído no canal {response['channel']['name']}. Segue o erro:\n{str(e)}'
                enviaSlack(mensagem)

def enviaSlack(mensagem, canal):
    sc = WebClient(
        token=cq.notification_bot,
        ssl=ssl_context)
    slack_resp = sc.chat_postMessage(
        channel='#' + canal,
        text=mensagem,
    )

ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

listener_client = WebClient(token=cq.listener_bot_token)
action_client = WebClient(token=cq.action_bot_token)

socket_client = SocketModeClient(
    app_token=cq.slack_app_token,
    web_client=listener_client
)
socket_client.socket_mode_request_listeners.append(event_handler)

def main():
    socket_client.connect()
    try:
        while True:
            time.sleep(0)
    except KeyboardInterrupt:
        print("Script parado manualmente...")
        mensagem = f'O Farejador foi parado manualmente...'
        for canal in cq.canais:
            enviaSlack(mensagem, canal)
    except Exception as e:
        print(f"Ocorreu o erro: {str(e)}")
        mensagem = f'O Farejador parou pelo erro...\n{str(e)}'
        for canal in cq.canais:
            enviaSlack(mensagem, canal)

if __name__ == "__main__":
    main()
