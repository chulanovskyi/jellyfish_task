from channels import route


def receive_message(message):
    print(message['text'])


channel_routing = [
    route('websocket.recieve', receive_message)
]

'''
channel_routing = {
    'websocket.connect': 'messapp.consumers.ws_connect',
    'websocket.recieve': 'messapp.consumers.ws_message',
    'websocket.disconnect': 'messapp.consumers.ws_disconnect',
}
'''