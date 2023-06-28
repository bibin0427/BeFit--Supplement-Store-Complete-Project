from django.urls import path
from Frontendapp import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('aboutpage/', views.aboutpage, name="aboutpage"),
    path('contactpage/', views.contactpage, name="contactpage"),
    path('productdisplay/<itemCatg>', views.productdisplay, name="productdisplay"),
    path('productdetails/<int:dataid>', views.productdetails, name="productdetails"),
    path('reglogdisplay/', views.reglogdisplay, name="reglogdisplay"),
    path('customerdata/', views.customerdata, name="customerdata"),
    path('customerlogin/', views.customerlogin, name="customerlogin"),
    path('userlogout/', views.userlogout, name="userlogout"),
    path('contactsave/', views.contactsave, name="contactsave"),
    path('displaycontact/', views.displaycontact, name="displaycontact"),
    path('Addtocart/<int:dataid>', views.Addtocart, name="Addtocart"),
    path('CheckOut/', views.CheckOut, name="CheckOut"),
    path('Checkoutsave/', views.Checkoutsave, name="Checkoutsave"),

]