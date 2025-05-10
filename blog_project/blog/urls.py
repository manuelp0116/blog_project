from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('post_list/', views.post_list, name='post_list'),
    path('main_page/', views.main_page, name='main_page'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('create_post/', views.create_post, name='create_post'),
    path('user_hub/', views.user_hub, name='user_hub'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('logout_screen/', views.logout_screen, name='logout_screen'),
    path('signup/', views.register, name='signup'),
    path('home/', views.home, name='home')
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login')
]