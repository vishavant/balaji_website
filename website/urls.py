from django.urls import path
from website import views

app_name = 'website'

urlpatterns = [
    path('', views.homepage, name='home'),
    path('index', views.index),
    path('contacts/', views.contact_list, name='contact_list'),
    path('contacts/create/', views.create_contact, name='create_contact'),
    path('contacts/update/<int:contact_id>/', views.update_contact, name='update_contact'),
    path('contacts/delete/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    path('about-us', views.about_us, name='about_us'),
    path('portfolio', views.portfolio, name='portfolio'),
]
