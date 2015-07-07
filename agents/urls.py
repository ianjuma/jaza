from django.conf.urls import patterns, url
from agents.views import agent_detail, agent_list, distributor_agent_list


urlpatterns = patterns(
    '',
    url(r'^agents/$', agent_list, name='agent_list'),
    url(r'^distributors/agents/(?P<pk>[0-9]+)$', distributor_agent_list, name='distributor_agent_list'),
    url(r'^agents/(?P<pk>[0-9]+)$', agent_detail, name='agent_detail')
)

# index route last - angular overwrite all endpoints - avoid 404?
# no need for include function