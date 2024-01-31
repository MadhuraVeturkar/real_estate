from django.urls import path
from . import views

# from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.index, name="index" ),
    path('signup',views.signup, name="signup" ),
    path('login',views.login, name="login" ),
    path('logout',views.logout, name="logout" ),
    path('add_property',views.add_property, name="add_property" ),
    path('about',views.about, name="about" ),
    path('contact',views.contact, name="contact" ),
    # path('search/<str:search_type>/<int:id>',views.search, name="search" ),
]