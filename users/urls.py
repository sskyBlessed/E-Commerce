from django.urls import path, include
from  .views import RegistrationAPIView, LoginAPIView, UsersAPIView, VerifyTokenView

urlpatterns = [
    path('registration/', RegistrationAPIView.as_view(), name = 'registration'),
    path('login/', LoginAPIView.as_view(), name = 'login'),
    path('token-list/', UsersAPIView.as_view(), name = 'list'),
    path('verify_token/', VerifyTokenView.as_view(), name='verify_token'),
]