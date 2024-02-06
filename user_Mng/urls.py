from django.urls import path
from user_Mng import views, rest_view


urlpatterns = [
    path('login', views.login_view),
    path('logout', views.logout_view),
    path('', rest_view.UserList.as_view()),
    path("<slug>/", rest_view.UserDetails.as_view()),
]
