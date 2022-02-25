from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),
    path('faq/', views.faq, name='faq'),
    path('newsLetter/', views.newsLetter, name='newsLetter'),
    path('category/<int:id>/<slug:slug>', views.category, name='category'),
    path('product/<int:id>/<slug:slug>', views.product, name='product')
]
