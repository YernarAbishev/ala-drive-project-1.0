from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('start/', views.start_page, name='start_page'),
    path('news/', views.news_page, name='news_page'),
    path('news/detail/<int:pk>/', views.news_detail_page, name='news_detail_page'),
    path('lessons', views.lessons_page, name='lessons_page'),
    path('lessons/detail/<int:pk>/', views.lessons_detail_page, name='lessons_detail_page'),
    path('simulator/', views.simulator_page, name='simulator_page'),
    path('login/', views.login_view, name='login_view'),
    path('sign-up/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout_view'),
]


