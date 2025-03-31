from django.urls import path
from api import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('profile/<int:user_id>/', views.get_profile, name='profile'),
    path('update/<int:user_id>/', views.update_user, name='update_user'),
    path('delete/<int:user_id>/', views.delete_user, name='delete_user'),
    # ✅ Check karein ki function exist karta hai
    path('users/', views.user_list_view, name='user_list'),
    path('users/create/', views.user_create_view, name='user_create'),
    path('users/update/<int:user_id>/',
         views.user_update_view, name='user_update'),
    path('users/delete/<int:user_id>/',
         views.user_delete_view, name='user_delete'),
]
