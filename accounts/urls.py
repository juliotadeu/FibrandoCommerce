from django.urls import path

from .views import SignUpView

app_name = 'accounts'

urlpatterns = [
    path('accounts/', include('accounts.urls')), # new
    path('accounts/', include('django.contrib.auth.urls'))
]