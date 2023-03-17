from django.shortcuts import render
from django.shortcuts import HttpResponse
from home.models import Task
# Create your views here.
def home(request):
    context = {'success': False, 'name':'Harsh'}
    if request.method == "POST":
        # Handle form
        title = request.POST['title']
        desc = request.POST['desc']
        print(title,desc)
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()
        context = {'success':True}
    return render(request, 'index.html', context)

def tasks(request):
    allTasks = Task.objects.all()
    context = {'tasks': allTasks}
    return render(request, 'tasks.html',context)


def edit(request, task_id):
    task = Task.objects.get(id=task_id)
    context = {'title':task.taskTitle, 'description':task.taskDesc}
    print(context)

# def delete(request, task_id):


