__license__ = 'MIT License <http://www.opensource.org/licenses/mit-license.php>'
__author__ = 'Lucas Theis <lucas@theis.io>'
__docformat__ = 'epytext'

from django.conf.urls import include, url
from publications.views import id, keyword, list, person, unapi, year

urlpatterns = [
        url(r'^$', year),
        url(r'^(?P<publication_id>\d+)/$', id),
        url(r'^year/(?P<year>\d+)/$', year),
        url(r'^tag/(?P<keyword>.+)/$', keyword),
        url(r'^list/(?P<list>.+)/$', list),
        url(r'^unapi/$', unapi),
        url(r'^(?P<name>.+)/$', person),
]
