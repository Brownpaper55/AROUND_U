"""
URL configuration for Events project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
import Suncity.views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls'),name='accounts'),
    path('new_accounts/', Suncity.views.SignUpView.as_view(), name= 'sign_up'),
    path('admin/', admin.site.urls),
    path('', Suncity.views.index, name='home'),
    path('programs/', Suncity.views.programs, name= 'programs'),
    path('addprogram/<int:pk>/', Suncity.views.add_program, name='edit_program'),
    path('addprogram/', Suncity.views.add_program, name='create_program'),
    path('entry_success', Suncity.views.FormSuccesView.as_view(), name= 'entry_success')
    #path('Create_Accounts/', Suncity.views.Create_Accounts)

]
if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
