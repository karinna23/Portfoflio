from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'myapp'

urlpatterns = [    
    path('', views.portfolio, name='portfolio'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('manage/', views.manage, name='manage'),
    path('about/add/', views.about_create, name='about_add'),
    path('about/edit/<int:pk>/', views.about_edit, name='about_edit'),
    path('skill/delete/<int:pk>/', views.delete_skill, name='delete_skill'),
    path('portfolio/delete/<int:pk>/', views.delete_project, name='delete_project'),
    path('contact/delete/<int:pk>/', views.delete_contact, name='delete_contact'),
    path('home/edit/<int:pk>/', views.home_edit, name='home_edit'),
    path('skill/edit/<int:pk>/', views.skill_edit, name='skill_edit'),
    path('social/edit/<int:pk>/', views.social_edit, name='social_edit'),
    path('profile/edit/<int:pk>/', views.cv_edit, name='cv_edit'),
    path('portfolio/edit/<int:pk>/', views.portfolio_edit, name='portfolio_edit'),
    path('add_skill/', views.add_skill, name='add_skill'),
    path('add_project/', views.add_project, name='add_project'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)