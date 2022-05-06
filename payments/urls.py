from django.urls import path

from .views import GatewayView, PaymentView

urlpatterns = [
    path('gateways/', GatewayView.as_view()),
    path('pay/', PaymentView.as_view())
]
