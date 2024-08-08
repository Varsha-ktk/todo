from django.urls import path

from to_do_app import views

# from to_do_app import views

urlpatterns=[
    path('',views.index,name='index'),
    path('skydash',views.skydash,name='skydash'),
    path('test',views.test,name='test'),
    path('todo',views.todo,name='todo'),
    path('todo_view',views.todo_view,name='todo_view'),
    path('todo_delete/<int:id>/', views.todo_delete, name='todo_delete'),
    path('todo_update/<int:id>/', views.todo_update, name='todo_update')
]