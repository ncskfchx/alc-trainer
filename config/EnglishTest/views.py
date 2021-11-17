from django.shortcuts import render, redirect
from django.views.generic import DetailView, View, CreateView
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from loguru import logger
import random

from .models import TestModel
from peewee import *

conn = SqliteDatabase('/Users/macbookpro/Documents/EnglishTest/config/db.sqlite3')

class BaseModel(Model):
    class Meta:
        database = conn  # соединение с базой, из шаблона выше


class ProgressModel(BaseModel):
    username = CharField(max_length=225, unique=True)
    progress = IntegerField()
    count_question = IntegerField()
    true_count_question = IntegerField()
    false_count_question = IntegerField()

    class Meta:
        table_name = 'progress'





class home(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            return render(request, 'home_auth.html', {'name': user.first_name})
        else:
            return render(request, 'home_is_auth.html')



class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        context  = {'form': form}
        return render(request, 'login.html', context)


    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')

        return render(request, 'login.html', {'form': form})



class RegisrerView(CreateView):
    def get(self, request, *args, **kwargs):
        form = RegisterForm(request.POST or None)
        context = {'form': form}
        return render(request, 'register.html', context)

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()

            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])

            ProgressModel(username=form.cleaned_data['username'], progress=0).save()
            login(request, user)

            return redirect('/')



        context = {'form': form}
        return render(request, 'register.html', context)




class EnglishTestView(View):
    def get(self, request, *args, **kwargs):
        tests = TestModel.objects.all()
        data_tests = []

        for test in tests:
            temp = {
                'question': test.question,
                'true_answer': test.true_answer,
                'false_answer': test.false_answer,
                'false_answer2': test.false_answer2,
                'false_answer3': test.false_answer3,

            }
            data_tests.append(temp)
        question = random.choice(data_tests)

        return render(request, 'testing.html', question)


    def post(self, request, *args, **kwargs):
        logger.success(request.POST)


        tests = TestModel.objects.all()
        data_tests = []

        for test in tests:
            temp = {
                'question': test.question,
                'true_answer': test.true_answer,
                'false_answer': test.false_answer,
                'false_answer2': test.false_answer2,
                'false_answer3': test.false_answer3,

            }
            data_tests.append(temp)
        question = random.choice(data_tests)

        return render(request, 'testing.html', question)




class CabinetView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = User.objects.get(id=request.user.id)
            if user:
                context = {
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'username': user.username,
                    'email': user.email
                }



                return render(request, 'cabinet.html', context)









