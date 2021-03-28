from django.conf.urls import url, include
from finance import views

urlpatterns = [
    url(r'^$', views.AccountsOverview.as_view()),
]
