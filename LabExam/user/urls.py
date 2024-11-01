from django.urls import path
from user.views import UserView

urlpatterns = [
    path('profile/', UserView.as_view()),
]