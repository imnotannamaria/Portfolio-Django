from django.urls import path

from portfolio.views import hello

urlpatterns = [
    path('', hello),
]
