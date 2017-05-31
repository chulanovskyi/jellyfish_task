import json
from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels.channel import Group


def http_request_consumer(message):
    response = HttpResponse('You asked for %s' % message.content['path'])
    for chunk in AsgiHandler.encode_response(response):
        message.reply_channel.send(chunk)


def ws_connect(message):
    Group('chat').add(message.reply_channel)


def ws_message(message):
    Group('chat').send({'text': json.dumps({
        'message': message.content['text'],
        'sender': message.reply_channel.name
    })})


def ws_disconnect(message):
    Group('chat').discard(message.reply_channel)
