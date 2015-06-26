from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.shortcuts import render_to_response, RequestContext


def handle_page_not_found_404(request):
    page_title = 'Page Not Found'
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))


class IndexView(TemplateView):
    template_name = 'index.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)