from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.http import HttpResponse

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Imports for Reordering Feature
from django.views import View
from django.shortcuts import redirect
from django.db import transaction

# Import models
from .models import Task

# Create your views here.

# def baseview(request):
#     return HttpResponse('Rohan sodha')

class TaskLoginView(LoginView):
    template_name = 'Taskapp/taskLogin.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

class TaskRegisterView(FormView):
    template_name = 'Taskapp/taskRegister.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(TaskRegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(TaskRegisterView, self).get(*args, **kwargs)

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'Taskapp/taskList.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        return context

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'Taskapp/taskDetail.html'

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'Taskapp/taskCreate.html'
    fields = ['title', 'startTime', 'endTime', 'project']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        # print(form.cleaned_data)
        form.instance.user = self.request.user
        print(self.request)
        return super(TaskCreateView, self).form_valid(form)

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'Taskapp/taskCreate.html'
    fields = ['title', 'startTime', 'endTime', 'project']
    success_url = reverse_lazy('tasks')

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'Taskapp/taskDelete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')






















