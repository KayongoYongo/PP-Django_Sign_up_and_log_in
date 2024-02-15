from django.urls import path
from .views import home, sign_up_page, log_in_page, sign_up

urlpatterns = [
        path('', home, name='home'),
        path('sign_up_page', sign_up_page, name='sign_up_page'),
        path('sign_up', sign_up, name='sign_up'),
        path('log_in_page', log_in_page, name='log_in_page')
]
