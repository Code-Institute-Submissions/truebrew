from django.urls import path
from .views import user_login, user_logout, user_account, user_registration


urlpatterns = [
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),
    path('account/', user_account, name="account"),
    path('register/', user_registration, name="registration"),
]