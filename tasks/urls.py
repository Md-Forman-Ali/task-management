# from django.urls import path


# from tasks.views import show_task


# urlpatterns = [

#     path('show_task/',show_task)
# ]


from django.urls import path

from tasks.views import create_task,show_specific_task

urlpatterns = [ 
        path('create_task/',create_task)
        path('show_it/<int:id>/', show_specific_task),
]
    
