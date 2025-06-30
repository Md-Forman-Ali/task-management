# from django.urls import path


# from tasks.views import show_task


# urlpatterns = [

#     path('show_task/',show_task)
# ]


from django.urls import path

from tasks.views import manager_dashboard,user_dashboard,test,create_task,view_task

urlpatterns = [ 
        path('manager-dashboard/',manager_dashboard,name="manager-dashboard"),
        path('user-dashboard/',user_dashboard),
        path('test/',test),
        path('create-task/',create_task, name='create-task'),
        path('view_task/',view_task)
]
    
