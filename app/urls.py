from django.urls import path
from . import views


urlpatterns = [
	path('',views.home,name='home'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('hospital_register/',views.hospital_register,name='hospital_register'),
    path('customer_register/',views.customer_register,name='customer_register'),
    path('customer_login/',views.customer_login,name='customer_login'),
    path('hospital_login/',views.hospital_login,name='hospital_login'),
    path('customer_dashboard/',views.customer_dashboard,name='customer_dashboard'),
    path('customer_logout/',views.customer_logout,name='customer_logout'),
    path('logout/',views.logout,name='logout'),
	path('add_facilities/',views.add_facilities,name='add_facilities'),
	path('search/',views.search,name='search'),
	path('detail/<int:pk>/',views.detail,name='detail'),
	path('view_facilities/',views.view_facilities,name='view_facilities'),
]

