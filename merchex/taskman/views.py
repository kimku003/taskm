from django.shortcuts import render, redirect
from django.http import HttpResponse
from taskman.forms import CustomUserCreationForm
from django.views import generic
from django import forms
from taskman.models import Task

from taskman.forms import home
from taskman.forms import TaskForm

from taskman.forms import ChatForm
from taskman.models import Chat
from django.template.loader import render_to_string

from django.shortcuts import get_object_or_404, redirect

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required






def home(request):
    return render(request, 'taskman/home.html')

class CustomUserCreationForm(forms.Form):
   name = forms.CharField(required=False)
   email = forms.EmailField()
   message = forms.CharField(max_length=1000)


@login_required
def create_task(request):
    form = TaskForm(request.POST or None)

    #tasks = Task.objects.all()
    tasks = Task.objects.filter(user=request.user)
    if request.method == 'POST' and form.is_valid():
        #form = TaskForm(request.POST or None)
        #tasks = Task.objects.filter(user=request.user)
        #form = TaskForm(request.POST)
        #if form.is_valid():
        #task = form.save(commit=False)
        form.instance.user = request.user
        #task.user = request.user
        form.save()

            # Ajoutez le nouveau message à la liste des messages
            #tasks = Task.objects.filter(user=request.user)
            #tasks = Task.objects.all()
        #form_str = render_to_string('taskman/create_task.html', {'tasks': tasks, 'form': form}, request=request)
        return render(request, 'taskman/task.html', {'tasks': tasks, 'form': form})

    #else:
    #    form = TaskForm()
    #    tasks = Task.objects.all()
    form_str = render_to_string('taskman/create_task.html', {'tasks': tasks, 'form': form}, request=request)
    tasks = Task.objects.filter(user=request.user)
    context = {'tasks': tasks, 'form': form}
    return HttpResponse(form_str)


@login_required
def edit_task(request, task_id):
  task = Task.objects.get(id=task_id)
  return render(request, 'taskman/edit_task.html', {'task': task} )

@login_required
def edit_taskk(request, task_id):
  
  task = Task.objects.get(id=task_id)
  return render(request, 'taskman/edit_taskk.html', {'task': task} )


@login_required
def update_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            print("task edit successfuly")
        form_str = render_to_string('taskman/task.html', {'task': task, 'form': form}, request=request)
        return render(request, 'taskman/task.html', {'task': task, 'form': form})
    else:
        form = TaskForm()
        form_str = render_to_string('taskman/task.html', {'task': task, 'form': form}, request=request)
    return HttpResponse(form_str)

@login_required
def update_taskk(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task  )
        if form.is_valid():
            form.save()
            print("task edit successfuly for detail_task")
        form_str = render_to_string('taskman/detail_task.html', {'task': task, 'form': form}, request=request)
        return render(request, 'taskman/detail_task.html', {'task': task, 'form': form})
    else:
        form = TaskForm()
        form_sttc4r = render_to_string('taskman/detail_task.html', {'task': task, 'form': form}, request=request)
    return HttpResponse(form_str)

@login_required
def detail_task(request, task_id):
    task = Task.objects.get(id=task_id)

    return render(request,
            'taskman/detail_task.html',
            {'task': task}) 

@login_required
def task(request):
    #tasks = Task.objects.all()
    tasks = Task.objects.filter(user=request.user)
    form_str = render_to_string('taskman/task.html', {'tasks': tasks}, request=request)
    return HttpResponse(form_str)



@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return HttpResponse('')

@login_required
def update_chat(request, chat_id):
    newchat = Chat.objects.get(id=chat_id)
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            newchat.content = request.POST['content']
            newchat.comment = request.POST['comment']
            newchat.save()
            print( "chat edited successfuly")
        form_str = render_to_string('taskman/chat.html', {'newchat': newchat, 'form': form}, request=request)
        return render(request, 'taskman/chat.html', {'newchat': newchat, 'form': form})
    else:
        form = ChatForm()
        form_str = render_to_string('taskman/chat.html', {'newchat': newchat, 'form': form}, request=request)
    return HttpResponse(form_str)

@login_required
def udate_chat(request, chat_id):
 if request.method == 'POST':
     chat = Chat.objects.get(id=chat_id)
     chat.content = request.POST['content']
     chat.save()
     return JsonResponse({'status':'success', 'content': chat.content})
 else:
     return JsonResponse({'status':'error', 'message':'Invalid request method'})

@login_required
def detail_chat(request, chat_id):
    chat = Chat.objects.get(id=chat_id)
    return render(request,
            'taskman/detail_chat.html',
            {'chat': chat}) 


@login_required
def create_chat(request):
    chats = Chat.objects.all()
    
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            chat = Chat(

                content=form.cleaned_data['content'],
                comment=form.cleaned_data['comment']
            )
            chat.save()
            print("new chat create")
            # Ajoutez le nouveau message à la liste des messages
            chats = Chat.objects.all()
        form_str = render_to_string('taskman/create_chat.html', {'chats': chats, 'form': form}, request=request)
        return render(request, 'taskman/chat.html', {'chats': chats, 'form': form})
    else:
        form = ChatForm()
        chats = Chat.objects.all()
        form_str = render_to_string('taskman/create_chat.html', {'chats': chats, 'form': form}, request=request)
    return HttpResponse(form_str)

@login_required
def chat(request):
    chats = Chat.objects.all()

    form_str = render_to_string('taskman/chat.html', {'chats': chats}, request=request)
    return HttpResponse(form_str)

@login_required
def delete_chat(request, chat_id):
    chat = get_object_or_404(Chat, pk=chat_id)
    chat.delete()
    return HttpResponse('')


@login_required
def edit_chat(request, chat_id):
  chat = Chat.objects.get(id=chat_id)
  return render(request, 'taskman/edit_chat.html', {'chat': chat} )





















