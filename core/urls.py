from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')), #Only for Browseable API
    path('api/user/',include('accounts.urls')),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/',include('base.urls')),
]
