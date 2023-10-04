from django.urls import path

from website import views

urlpatterns = [
    path("", views.home, name="home"),
    path("suggest/", views.suggest, name="suggest"),
    path("explain/", views.explain_code, name="explain"),
    path("share/<int:record_id>/", views.share, name="share"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("past/", views.past, name="past"),
    path("delete_past<Past_id>", views.delete_past, name="delete_past"),
    path("past/delete-all", views.delete_all_past, name="delete_all_past"),
    path("welcome/", views.welcome, name="welcome"),
]
