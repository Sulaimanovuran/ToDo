from django.urls import path
from project1.views import *

urlpatterns = [
    path('', BuyProductListView.as_view()),
    path('product_create/', BuyProductCreateView.as_view()),
    path('product_detail/<int:pk>/', BuyProductDetailView.as_view()),
    path('product_update/<int:pk>/', BuyProductUpdateView.as_view()),
    path('product_delete/<int:pk>/', BuyProductDeleteView.as_view()),
]
