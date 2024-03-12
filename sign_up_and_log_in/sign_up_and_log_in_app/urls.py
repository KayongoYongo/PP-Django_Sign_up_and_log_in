from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home, sign_up_page, sign_up, log_in_page, log_in, logout_view, user_dashboard, upload_image, send_email

urlpatterns = [
        path('', home, name='home'),
        path('sign_up_page', sign_up_page, name='sign_up_page'),
        path('sign_up', sign_up, name='sign_up'),
        path('log_in_page', log_in_page, name='log_in_page'),
        path('log_in', log_in, name='log_in'),
        path('logout/', logout_view, name='logout'),
        path('user_dashboard', user_dashboard, name='user_dashboard'),
        path('upload_image', upload_image, name='upload_image'),
        path('send_email', send_email, name='send_email'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)