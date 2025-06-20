# from django.urls import path


# from tasks.views import show_task


# urlpatterns = [

#     path('show_task/',show_task)
# ]


from django.urls import path

from tasks.views import create_task

urlpatterns = [ 
        path('create_task/',create_task)
]
    
