from django.urls import path, include
from .views import authView, home, regleView, classementView

urlpatterns = [
 path("", home, name="home"),
 path("regle/", regleView, name="relge"),
 path("classement/", classementView, name="classement"),
 path("signup/", authView, name="authView"),
 path("accounts/", include("django.contrib.auth.urls")),
]
