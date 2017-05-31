from channels.routing import route


channel_routing = [
    route('http.request', 'messapp.consumers.http_request_consumer')
]