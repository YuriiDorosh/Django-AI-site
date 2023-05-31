from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('suggest/', views.suggest, name='suggest'),
    path('explain/', views.explain_code, name='explain'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('past/', views.past, name='past'),
    path('delete_past<Past_id>', views.delete_past, name='delete_past'),
]


# from django.urls import path
# from .views import (
#     HomeView,
#     SuggestView,
#     LoginView,
#     LogoutView,
#     RegisterView,
#     PastView,
#     DeletePastView,
# )
#
# urlpatterns = [
#     path('', HomeView.as_view(), name='home'),
#     path('suggest/', SuggestView.as_view(), name='suggest'),
#     path('login/', LoginView.as_view(), name='login'),
#     path('logout/', LogoutView.as_view(), name='logout'),
#     path('register/', RegisterView.as_view(), name='register'),
#     path('past/', PastView.as_view(), name='past'),
#     path('delete_past/<int:Past_id>/', DeletePastView.as_view(), name='delete_past'),
# ]

