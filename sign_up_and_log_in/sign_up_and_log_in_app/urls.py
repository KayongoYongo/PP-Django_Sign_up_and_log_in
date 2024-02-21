from django.urls import path
from .views import home, sign_up_page, sign_up, log_in_page, log_in, logout_view

urlpatterns = [
        path('', home, name='home'),
        path('sign_up_page', sign_up_page, name='sign_up_page'),
        path('sign_up', sign_up, name='sign_up'),
        path('log_in_page', log_in_page, name='log_in_page'),
        path('log_in', log_in, name='log_in'),
        path('logout/', logout_view, name='logout'),
]