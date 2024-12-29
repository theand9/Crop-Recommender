
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('pyield-AdminPanel/', admin.site.urls),
    path('home/', include('webpages.urls')),
    path('', include('accounts.urls')),
]
