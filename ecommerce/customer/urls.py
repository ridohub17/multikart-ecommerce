from django.urls import path
from . import views

app_name = 'customer'

urlpatterns = [
    path('about-us/',views.about_us,name='about-us'),
    path('FAQ/',views.faq,name='faq'),
]

