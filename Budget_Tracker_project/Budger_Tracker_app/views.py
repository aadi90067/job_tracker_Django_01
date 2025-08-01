from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from .forms import ExpenseForm
from .models import Expense
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib.auth import logout


def home(request):
    return render(request,'index.html')

def user_logout(request):
    logout(request)
    return redirect('user_login')

@login_required
def Dashboard(request):
    form = ExpenseForm()
    
    # Fetch only expenses for the current user
    user_expenses = Expense.objects.filter(user=request.user).order_by('-date_added')

    total_expense = user_expenses.aggregate(Sum('amount'))['amount__sum'] or 0

    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user  # Assign the logged-in user
            expense.save()
            return redirect('Dashboard')


    return render(request, 'Dashboard.html', {
        'form': form,
        'expenses': user_expenses,
        'total': total_expense
    })



@login_required
def clear_expenses(request):
    if request.method == 'POST':
        Expense.objects.filter(user=request.user).delete()
    return redirect('Dashboard')


def Register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')
    
    return render(request, 'register.html')

def user_login(request):  # Renamed to avoid conflict
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('Dashboard')  # fixed route name
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('login')
    return render(request, 'login.html')
