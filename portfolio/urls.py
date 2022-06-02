from django.urls import path

from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.hello, name="hello"),
    path('about_me/', views.about_me, name="about_me"),
    path('skills/', views.skills, name="skills"),
    path('experience/', views.experience, name="experience"),
    path('contact/', views.contact, name="contact"),
]
