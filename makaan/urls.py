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
    path('property-list',views.property_list, name="property_list" ),
    path('property-search',views.search_property, name="property_search" ),

    path('property-type',views.property_type, name="property_type" ),
    path('property-agent',views.property_agent, name="property_agent" ),
    path('view-property/<int:id>',views.view_property, name="view_property" ),
    path('about',views.about, name="about" ),
    path('contact',views.contact, name="contact" ),
    path('testimonial',views.testimonial, name="testimonial" ),

    # path('search/<str:search_type>/<int:id>',views.search, name="search" ),
]