
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userapp/', include('userapp.urls')),
    path('advocates/', include('advocates.urls')),
    path('lawfirm/', include('lawfirm.urls')),
    path('registrar/', include('registrar.urls')),
    path('association/', include('association.urls')),
]
