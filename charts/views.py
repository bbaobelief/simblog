from django.views.generic import TemplateView
from base.mixins.views import LoginRequiredMixin

class ChartsView(LoginRequiredMixin, TemplateView):
    template_name = 'charts/index.html'

    def get_context_data(self, **kwargs):
        context = super(ChartsView, self).get_context_data(**kwargs)
        context['host'] = 'localhost'
        # if not self.request.user.is_staff:
        #     context['res_list'] = context['res_list'].filter(user=self.request.user)
        return context