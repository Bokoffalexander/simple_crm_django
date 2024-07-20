from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddPerson
from .models import Record
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.views.decorators.csrf import requires_csrf_token

@login_required
def add_person(request):
    """Добавить новую персону"""
    if request.method != 'POST':
        # Данные не отправлены, создается пустая форма
        form = AddPerson()
    else:
        # Отправляем данные POST, 
        # обработать данные
        form = AddPerson(data=request.POST)
        if form.is_valid():
            new_person=form.save(commit=False)
          # new_person.owner = request.user
            new_person.save()
            return redirect('home')

    # Вывести пустую или недействительную форму
    context = {'form':form}
    return render(request,'add_person.html', context)


@requires_csrf_token
def home(request):
    records = Record.objects.all().order_by('-date_added')

    # Check: login?
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # authenticate 
        user = authenticate(request, username=username, password= password)

        if user is not None:
            login(request, user)
            messages.success(request, " You logged in!")
            return redirect ('home')
        else:
            messages.success(request, "Wrong username-password!")
            return redirect ('home')
    else:
        return render(request, 'home.html', {'records':records})

# def login_user(request):
#    pass

def logout_user(request):
    logout(request)
    messages.success(request, "You logged out!")
    return redirect("home")

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Successfully registered!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render (request, 'register.html', {'form':form})
    
    return render (request, 'register.html', {'form':form})

