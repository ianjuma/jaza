from django.conf.urls import patterns, url, include
# from rest_framework_nested import routers
from agents.views import agent_detail, agent_list

# router = routers.SimpleRouter()
# router.register(r'agents', AgentViewSet)


urlpatterns = patterns(
    '',
    # url(r'^agents', include(router.urls, namespace='api.agents')),
    url(r'^agents/$', agent_list, name='agent_list'),
    url(r'^agents/(?P<pk>[0-9]+)$', agent_detail, name='agent_detail')
)

# index route last - angular overwrite all endpoints - avoid 404?
# no need for include function