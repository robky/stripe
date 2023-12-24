from django.urls import path

from api import views

app_name = 'orders'

urlpatterns = [
    path('', views.index),
    path(
        'buy/<int:order_id>/',
        views.create_checkout_session,
        name='get_session',
    ),
    path('order/<int:order_id>/', views.to_checkout, name='view_order'),
]
