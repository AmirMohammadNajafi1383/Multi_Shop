from django.urls import path
from . import views


app_name = 'account'
urlpatterns = [
    path('login',views.UserLogin.as_view(),name='user_login'),
    path('otplogin',views.OtpLoginView.as_view(),name='user_otp_login'),
    path('checkotp',views.CheckOtpView.as_view(),name='user_checkotp'),
    path('logout',views.User_Logout,name='user_logout'),
    path('add/address',views.AddressAddView.as_view(),name='add_address'),


]