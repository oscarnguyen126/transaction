from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('user_Mng.urls')),
    path('transactions/', include('money_Mng.urls')),
    path('notifications/', include('noti_Mng')),
]
