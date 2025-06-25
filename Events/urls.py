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
import Suncity.api_views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls'),name='accounts'),
    path('new_accounts/', Suncity.views.SignUpView.as_view(), name= 'sign_up'),
    path('admin/', admin.site.urls),
    path('', Suncity.views.index, name='home'),
    path('programs/', Suncity.views.programs, name= 'programs'),
    path('viewprogram/<int:pk>/', Suncity.views.view_program, name='view_program'),
    path('addprogram/<int:pk>/', Suncity.views.add_program, name='edit_program'),
    path('addprogram/', Suncity.views.add_program, name='create_program'),
    path('entry_success', Suncity.views.FormSuccesView.as_view(), name= 'entry_success'),
    path('search/', Suncity.views.search, name='search'),
    path('hub/',Suncity.views.hub, name = 'my_hub'),
    path('delete/<pk>/', Suncity.views.ProgView.as_view(), name='delete_prog'),

    #API
    # Authentication URLs
    path('api/register/', Suncity.api_views.register, name='register'),
    path('api/login/', Suncity.api_views.login, name='login'),
    path('api/logout/', Suncity.api_views.logout, name='logout'),
    
    # User Profile URLs
    path('api/profile/', Suncity.api_views.profile, name='profile'),
    path('api/profile/update/', Suncity.api_views.update_profile, name='update_profile'),
    
    # Program URLs
    path('api/programs/',Suncity.api_views.program_list, name='program_list'),
    path('api/programs/create/',Suncity.api_views.program_create, name='program_create'),
    path('api/programs/<int:pk>/', Suncity.api_views.program_detail, name='program_detail'),
    path('api/programs/<int:pk>/update/', Suncity.api_views.program_update, name='program_update'),
    path('api/programs/<int:pk>/delete/', Suncity.api_views.program_delete, name='program_delete'),
    
    # User-specific program URLs
    path('api/my-programs/', Suncity.api_views.my_programs, name='my_programs'),
    path('api/users/<int:user_id>/programs/', Suncity.api_views.user_programs, name='user_programs'),
    
    # Search and Filter URLs
    #path('programs/search/', Suncity.api_views.search_programs, name='search_programs'),
    path('api/programs/popular/', Suncity.api_views.popular_programs, name='popular_programs'),
    path('api/programs/upcoming/', Suncity.api_views.upcoming_programs, name='upcoming_programs'),

]
if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
