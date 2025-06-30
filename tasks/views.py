from django.shortcuts import render,redirect
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm, TaskDetailsModelForm

from tasks.models import Employee,Task,TaskDetails,Project
from datetime import date
from django.db.models import Q,Count,Max,Min,Avg
from django.contrib import messages

def manager_dashboard(request):

    type = request.GET.get('type','all')
  
    counts = Task.objects.aggregate(
        total=Count('id'),
        completed=Count('id',filter=Q(status="COMPLETED")),
        in_progress= Count('id',filter=Q(status="IN_PROGRESS")),
        pending =Count('id',filter=Q(status="PENDING")),
        )
        
    #retarving data
    base_query =   tasks = Task.objects.select_related('details').prefetch_related('assigned_to').all()

    if type == 'completed':
        tasks = base_query.filter(status="COMPLETED")
    elif type =='in_progress':
        tasks =base_query.filter(status="IN_PROGRESS")
    elif type == 'pending':
        tasks = base_query.filter(status="PENDING")
    elif type == 'all' :
        tasks = base_query.all()
    
       

    context = {
        "tasks" : tasks,
        "counts" :counts
    }
    return render(request,"dashboard/manager-dashboard.html",context)
def user_dashboard(request):
  
    return render(request, "dashboard/user-dashboard.html", )


def test(request):
    names = ["Mahmud", "Ahamed", "John", "Mr. X"]
    count = 0
    for name in names:
        count += 1
    context = {
        "names": names,
        "age": 23,
        "count": count
    }
    return render(request, 'test.html', context)



# def create_task(request):
#     # employees = Employee.objects.all()
#     task_form = TaskModelForm()  # For GET
#     task_detail_form = TaskDetailsModelForm()

#     if request.method == "POST":
#         task_form = TaskModelForm(request.POST)
#         task_detail_form = TaskDetailsModelForm(request.POST)

#         if task_form.is_valid() and task_detail_form.is_valid():

#             """ For Model Form Data """
#             task = task_form.save()
#             task_detail = task_detail_form.save(commit=False)
#             task_detail.task = task
#             task_detail.save()

#             messages.success(request, "Task Created Successfully")
#             return redirect('create-task')

#     context = {"task_form": task_form, "task_detail_form": task_detail_form}
#     return render(request, "dashboard/task_form.html", context)
def create_task(request):
    # employees = Employee.objects.all()
    task_form = TaskModelForm()  # For GET
    task_detail_form = TaskDetailsModelForm()

    if request.method == "POST":
        task_form = TaskModelForm(request.POST)
        task_detail_form = TaskDetailsModelForm(request.POST)

        if task_form.is_valid() and task_detail_form.is_valid():

            """ For Model Form Data """
            task = task_form.save()
            task_detail = task_detail_form.save(commit=False)
            task_detail.task = task
            task_detail.save()

            messages.success(request, "Task Created Successfully")
            return redirect('create-task')

    context = {"task_form": task_form, "task_detail_form": task_detail_form}
    return render(request, "dashboard/task_form.html", context)


def view_task(request):
    projects = Project.objects.annotate(num_task=Count('task')).order_by('num_task')
    return render(request, "show_task.html", {"projects": projects})
    