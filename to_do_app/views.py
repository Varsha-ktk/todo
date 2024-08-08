from django.shortcuts import render, redirect

from to_do_app.forms import TestForm, ToDo
from to_do_app.models import Todo


# Create your views here.
def index(request):
    return render(request,'index.html')

def skydash(request):
    return render(request,'skydash.html')

def test(request):
    data = TestForm()
    print(data)
    return render(request,'test.html',{"form":data})

def todo(request):
    td= ToDo()
    if request.method =='POST':
        form = ToDo(request.POST)
        form.is_valid()
        form.save()
    return render(request, 'todo.html',{'td':td})

def todo_view(request):
    td=Todo.objects.all()
    return render(request,'todo_view.html',{'td':td})
def todo_delete(request,id):
    data=Todo.objects.get(id=id)
    data.delete()
    return redirect('todo_view')
def todo_update(request,id):
    data = Todo.objects.get(id=id)
    form = ToDo(instance = data)
    if request.method == 'POST':
        updated_data = ToDo(request.POST,instance = data)
        updated_data.is_valid()
        updated_data.save()
        return redirect("todo_view")
    return render(request,'update.html',{'form':form})

