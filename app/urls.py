from django.urls import path,include
from .import views

urlpatterns = [
    path("",views.Indexpage,name="index"),
    path("doctorregisterpage/",views.DoctorRegisterPage,name="doctorregisterpage"),
    path("paitentregistepage/",views.PaitentRegisterPage,name="paitentregistepage"),
    path("pharmaregisterpage/",views.PharmacyRegisterPage,name="pharmaregisterpage"),
    path("loginpage/",views.Loginpage,name="loginpage"),
    path("login",views.Loginuser,name="login"),
    path("insert",views.InsertData,name="insert"),
    path("profilepage/<int:pk>",views.ProfilePage,name="profilepage"),
    path("logout/<int:pk>",views.Logout,name="logout"),
    path("alldoctorshow/",views.AllDoctorShow,name="alldoctor")
]