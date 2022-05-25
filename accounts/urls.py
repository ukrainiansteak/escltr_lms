from django.urls import path

from accounts.views import AccountRegister, AccountLogin, MainPage

app_name = 'accounts'

urlpatterns = [
    path('register', AccountRegister.as_view(), name='register'),
    path('login', AccountLogin.as_view(), name='login'),
    path('', MainPage.as_view(), name='index'),
    ]
