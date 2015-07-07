from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.shortcuts import render_to_response, RequestContext

from django.db import connection
from agents.views import dict_fetch_all


def handle_page_not_found_404(request):
    page_title = 'Page Not Found'
    return render_to_response('index.html', locals(), context_instance=RequestContext(request))


class IndexView(TemplateView):
    template_name = 'index.html'

    def product_ids(self):
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM products_product WHERE owner_id = %s", [self.request.user.id])
        prods = dict_fetch_all(cursor=cursor)
        prod_ids = []

        for obj in prods:
            keys, values = obj.keys(), obj.values()
            prod_ids.append(values[0])

        cursor.close()
        return prod_ids

    @method_decorator(ensure_csrf_cookie)
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)


class LoginView(TemplateView):
    template_name = 'login.html'

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(LoginView, self).dispatch(*args, **kwargs)