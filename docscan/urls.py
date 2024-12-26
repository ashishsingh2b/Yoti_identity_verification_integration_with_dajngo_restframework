from django.urls import path
from .views import CreateYotiSessionView
from .import views


urlpatterns = [
    path('create-session/', CreateYotiSessionView.as_view(), name='create_yoti_session'),
    path('verification-success/', views.verification_success, name='verification_success'),
    path('verification-error/', views.verification_error, name='verification_error'),



]
    