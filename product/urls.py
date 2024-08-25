from django.urls import path 
from . import views

app_name = 'product'


urlpatterns = [
    path('about-us/', views.about_us, name='about-us'),
    path('products/', views.products, name='products'),
    path('product-page/<str:pk>', views.product_page, name='product-page'),
    path('contact-us/', views.contact_us, name='contact-us'),

]