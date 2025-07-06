from django.contrib import admin
from users.views import GoogleLogin
from django.urls import path, include

urlpatterns = [
    path('api/auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('admin/', admin.site.urls),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
]
