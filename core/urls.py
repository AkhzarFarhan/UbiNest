from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),
    path('', views.homepage, name='homepage'),
    path('profile/', views.profile, name='profile'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),
    path('tasks/update/<int:task_id>/', views.task_update, name='task_update'),
    path('finances/', views.finance_list, name='finance_list'),
    path('finances/create/', views.transaction_create, name='transaction_create'),
    path('events/', views.event_list, name='event_list'),
    path('chat/<int:group_id>/', views.group_chat, name='group_chat'),
]
