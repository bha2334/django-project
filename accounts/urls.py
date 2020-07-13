from django.urls import path
from .views import signup,login,logout,display,edit
urlpatterns =[
    path('signup',signup, name="signup"),
    path('login',login , name="login"),
    path('logout',logout , name="logout"),
    path('display',display,name="display"),
    path('edit',edit,name="edit"),


]