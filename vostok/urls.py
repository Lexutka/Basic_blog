from django.urls import path
from . import views
from django.contrib import auth
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index,name='home'),
    path('new_post',views.create_post,name='new_post'),
    path('post/<int:pk>/',views.post_detail,name='post_detail'),
    path('post/<int:pk>/edit',views.edit_post,name='edit_post'),
    path('accounts/login/', auth.views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth.views.LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', views.register, name='register'),
    path('cabinet',views.cabinet,name='cabinet'),
    path('password-change/', auth.views.PasswordChangeView.as_view(), name='password_change'),
    path('password-change/done/', auth.views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'))
]