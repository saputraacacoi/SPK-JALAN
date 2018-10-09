from django.conf.urls import url
from management.alternatif import views

urlpatterns = [
    url (r'^$', views.ListAlternatifView.as_view(), name='view'),
]