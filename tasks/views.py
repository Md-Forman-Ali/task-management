from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee,Task,TaskDetails,Project
from datetime import date
from django.db.models import Q,Count,Max,Min,Avg

def manager_dashboard(request):
    return render(request,"dashboard/manager-dashboard.html")


def user_dashboard(request):
    return render(request,"dashboard/user-dashboard.html")

# def test(request):
#     context ={
#         "names":["Forman", "Islam","Hridoy"],
      
#     }
#     return render(request,'test.html',context)
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


def create_task(request):
    employees = Employee.objects.all()
    form = TaskModelForm() # FOR GET

    if request.method== "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
            """For Model Form Data """
            form.save()
            return render(request,'dashboard/task_from.html',{"form": form,"message": "Task Added Succesfully"})

            """For Django Form data """
            # data = form.cleaned_data
            # title = data.get('title')
            # description = data.get('description')

            # due_date = data.get('due_date')
            # assigned_to = data.get('assigned_to')

            # task = Task.objects.create(
            #     title = title, description = description,  due_date = due_date
            # )
            # #assigned for employee

            # for emp_id in assigned_to:
            #     employees = Employee.objects.get(id=emp_id)
            #     task.assigned_to.add(employees)

         
    context = {"form": form}
    return render(request,"dashboard/task_from.html",context)


def view_task(request):
    #retrive all data form task Model
    # tasks = Task.objects.all()
    # retrive a specific task

    # task_3 = Task.objects.get(pk=1)

    #fetch the first task

    # first_task = Task.objects.first()
    # return render(request,"show_task.html",{"tasks":tasks, "task3":task_3,"first_task": first_task})


    # show the task are completed 
    # tasks = Task.objects.filter(status="PENDING")

    # Show the task which due date today
    # tasks = Task.objects.filter(due_date= date.today())
    """Showw The Details Which priority Is High and M and Ja iccha """
    # tasks = TaskDetails.objects.exclude(priority="H")


    """Show The Task Who Contain 'paper' """
    # tasks =Task.objects.filter(title__icontains="c",status="PENDING")

    # tasks = Task.objects.filter(Q(status="PENDING") | Q(status="IN_PROGRESS"))

    # tasks = Task.objects.filter(status="ksgfios").exists()
    """Selected Related (Foreginkey, OneToOneField)"""
    # tasks = TaskDetails.objects.select_related('task').all()
    # tasks = Task.objects.select_related('project').all()

    """Prefetch Related (reverse ForigenKey , ManyToMany)"""
    # tasks = Project.objects.prefetch_related('task_set').all()
    # tasks = Task.objects.prefetch_related("assigned_to").all()
    # tasks = Employee.objects.prefetch_related('tasks').all()


    """Aggreate"""
    # task_count = Task.objects.aggregate(num_task=Count('id'))

    projects = Project.objects.annotate(num_task=Count('task')).order_by('num_task')
    return render(request, "show_task.html", {"projects": projects})
    