from django.urls import path
from . import views

app_name = 'app'


urlpatterns = [
    path('',views.index_view, name='index'),
    path('index/',views.index_view, name='index'),
    path('dashboard/',views.dashboard_view, name='dashboard'),
   
    path('logout/',views.logout_view, name='logout'),
    path('menu/', views.menu_view, name='menu'),
    path('detail/<int:post_id>/', views.detail_view, name='detail'), 
    path('login/',views.login_view, name ='login'),
    path('success/',views.order_views, name='success'),
    path('orderform/',views.order_page, name='orderform'),
    path('order/', views.vegetable_order, name='order'),
    # path('about/',views.about_view, name='about'),

]
