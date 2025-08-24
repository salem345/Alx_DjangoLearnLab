from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library
from .models import Library
from django.views.generic.detail import DetailView
# --------------------
# Function-based view
# --------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

# --------------------
# Class-based view
# --------------------
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    else:
        form = RegisterForm()
    return render(request, "relationship_app/register.html", {"form": form})

# تسجيل الدخول
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/")
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

# تسجيل الخروج
def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")