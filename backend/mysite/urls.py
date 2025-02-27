from django.urls import path,include

urlpatterns = [
    path('api/', include('tech_connect.urls')),
]
