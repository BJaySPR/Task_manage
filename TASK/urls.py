from django.urls import path
from .import views
urlpatterns = [
    path('index',views.index,name='index'),
    path('signup/',views.sign_up,name='sign_up'),
    path('',views.sign_in,name='sign_in'),
    path('signout/',views.signout,name="signout"),
    path('taskcreate/',views.task_create,name="taskcreate"),
    path('taskview/',views.task_view,name='taskview'),
    path('delete_task/<int:id>',views.task_delete,name='delete_task'),
    path('upate/<int:id>',views.edit,name='edit'),
]
