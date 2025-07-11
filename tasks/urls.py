# from django.urls import path


# from tasks.views import show_task


# urlpatterns = [

#     path('show_task/',show_task)
# ]


from django.urls import path

from tasks.views import manager_dashboard,user_dashboard,create_task,view_task,update_task,delete_task

urlpatterns = [ 
        path('manager-dashboard/',manager_dashboard,name="manager-dashboard"),
        path('user-dashboard/',user_dashboard),

        path('create-task/',create_task, name='create-task'),
        path('view_task/',view_task),
        path('update_task/<int:id>/',update_task,name='update_task'),
        path('delete_task/<int:id>/',delete_task,name='delete_task')

]
    
