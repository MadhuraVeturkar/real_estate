from django.urls import path
from . import views

# from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.index, name="index" ),
    # path('search/<str:search_type>/<int:id>',views.search, name="search" ),
]