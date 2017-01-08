from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.book_deatain, name='book_detail'),
]