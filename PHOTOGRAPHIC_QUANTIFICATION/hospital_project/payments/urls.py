from django.urls import path
from . import views

urlpatterns= [path('payments/', views.payments, name= 'payments'),
             path('paymentsdata/', views.paymentsdata, name = 'paymentsdata'),
             path('paymentsdatawrite/', views.paymentsdatawrite, name = 'paymentsdatawrite'),
             path('paymentsdata/', views.paymentsdata, name = 'paymentsdata'),
             
             
             ]
                                                                     


