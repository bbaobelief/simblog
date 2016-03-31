from django.views.generic import TemplateView

class ChatView(TemplateView):
    template_name = 'chat/index.html'

    def get_context_data(self, **kwargs):
        context = super(ChatView, self).get_context_data(**kwargs)
        context['host'] = 'localhost'
        # if not self.request.user.is_staff:
        #     context['res_list'] = context['res_list'].filter(user=self.request.user)
        return context