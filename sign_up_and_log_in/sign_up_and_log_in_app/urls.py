from django.urls import path
from .views import home, sign_up_page

urlpatterns = [
        path('', home, name='home'),
        path('sign_up_page', sign_up_page, name='sign_up_page')
]
