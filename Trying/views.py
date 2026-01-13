from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login


def home(request):
    return render(request, 'Trying/home.html')


def about(request):
    return render(request, 'Trying/about.html')


def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            user=request.user,
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            message=request.POST.get('message')
        )
        return redirect('contact_list')

    return render(request, 'Trying/contact.html')


# READ
@login_required
def contact_list(request):
    contacts = Contact.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'Trying/contact_list.html', {'contacts': contacts})



# UPDATE
@login_required
def contact_edit(request, id):
    contact = get_object_or_404(Contact, id=id, user=request.user)
    if request.method == "POST":
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.message = request.POST.get('message')
        contact.save()
        return redirect('contact_list')

    return render(request, 'Trying/contact_edit.html', {'contact': contact})


# DELETE
@login_required
@login_required
def contact_delete(request, id):
    contact = get_object_or_404(Contact, id=id, user=request.user)

    if request.method == "POST":
        contact.delete()
        return redirect('contact_list')

    return render(request, 'Trying/contact_delete.html', {'contact': contact})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('contact_list')

        return render(request, 'Trying/login.html', {'error': 'Invalid credentials'})

    return render(request, 'Trying/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, 'Trying/signup.html', {
                'error': 'Passwords do not match'
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'Trying/signup.html', {
                'error': 'Username already exists'
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        # Auto-login after signup (best UX)
        login(request, user)
        return redirect('contact_list')

    return render(request, 'Trying/signup.html')
