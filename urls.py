from . import views
from .views import AdminLogin, AdminLogout
from .views import IndexView
from django.urls import path

urlpatterns = [
    path('', AdminLogin.as_view(), name='login'),  # первый параметор браузер,
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('index/', IndexView.as_view(), name='index'),
    path('', views.dashboard, name='dashboard'),
    path('logout/', AdminLogout.as_view(), name='logout'),
    path('logout', AdminLogout.as_view(), name='logout'),
    path('testing_orm', views.get, name='testing_orm'),
    path('pandas_test', views.test_matplotlib, name='analytics'),
    path('index/edit', views.edit, name='edit'),
    path('test_table', views.test_table, name='test_table'),
    path('test_table_admin', views.test_table_admin, name='test_table_admin'),
    path('analytics', views.analytics, name='analytics')
]