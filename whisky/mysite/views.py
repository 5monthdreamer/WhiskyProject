from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs: Any)
        context['app_list'] = ['labelscanner','showcase']
        return context
    
    