from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]

urlpatterns += [
    path('listings/', views.listings, name='listings'),
    path('listings/<int:pk>', views.listing, name='listing'),
    path('listings/add', views.ListingCreate.as_view(), name='listing-add'),
    path('listings/<int:pk>/update', views.ListingUpdate.as_view(), name='listing-update'),
    path('listings/<int:pk>/delete', views.ListingDelete.as_view(), name='listing-delete'),
    path('listings/search', views.search, name='search'),
    path('listings/contact', views.contact, name='contact'),
]

urlpatterns += [
    path('realtors/', views.realtors, name='realtors'),
    path('realtors/<int:id>', views.realtor, name='realtor'),
    path('realtors/add', views.realtor_add, name='realtor-add'),
    path('realtors/<int:id>/update', views.realtor_update, name='realtor-update'),
    path('realtors/<int:id>/delete', views.realtor_delete, name='realtor-delete'),
]

urlpatterns += [
    path('accounts/login', views.login, name='login'),
    path('accounts/register', views.register, name='register'),
    path('accounts/logout', views.logout, name='logout'),
    path('accounts/dashboard', views.dashboard, name='dashboard'),
]