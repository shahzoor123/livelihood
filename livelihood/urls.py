from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    
    path('', include('dashboard.urls')),
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('django.contrib.auth.urls')),
    

]
