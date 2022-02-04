from django.urls import URLPattern, path
from example.views import LoginApiView, AddProductApiView, EditProductApiView, ProductList

urlpatterns =[
    path('login/',LoginApiView.as_view(),name='login'),
    path('addproduct/',AddProductApiView.as_view(),name='addproduct'),
    path('editproduct/<int:pk>/',EditProductApiView.as_view(),name='editproduct'),
    path('listproduct/',ProductList.as_view(),name='listproduct'),
    
]