from django.urls import path
from . import views

app_name = "bank"


urlpatterns = [
    path("", views.home, name="home"),
    path('signup/', views.signup, name='signup'),
    path("login/", views.login_request, name="login"),
    path("logout/", views.logout, name="logout"),
    path("create/", views.create, name="create"),
    path("account/", views.account, name="account"),
]