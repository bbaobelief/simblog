# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from ws4redis.redis_store import RedisMessage
from ws4redis.publisher import RedisPublisher

class ChatView(TemplateView):
    template_name = 'chat/index.html'
    facility = 'public'
    audience = {'broadcast': True}
    message = RedisMessage('{"username": "admin", "message": "Hello everybody"}')

    def get(self, request, *args, **kwargs):
        redis_publisher = RedisPublisher(facility=self.facility, **self.audience)
        redis_publisher.publish_message(self.message)
        return super(ChatView, self).get(request, *args, **kwargs)
        