from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library
from .models import Library
from django.views.generic.detail import DetailView
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
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

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

UserCreationForm()
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

from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Checkers for roles
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Admin view
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

# Add book
@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author_id = request.POST.get("author")
        if title and author_id:
            Book.objects.create(title=title, author_id=author_id)
            return redirect('list_books')
    return render(request, "relationship_app/add_book.html")

# Edit book
@permission_required('relationship_app.can_change_book')
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title", book.title)
        author_id = request.POST.get("author")
        if author_id:
            book.author_id = author_id
        book.save()
        return redirect('list_books')
    return render(request, "relationship_app/edit_book.html", {"book": book})

# Delete book
@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect('list_books')
    return render(request, "relationship_app/delete_book.html", {"book": book})

from django.http import JsonResponse
from .models import Book

def book_list(request):
    books = Book.objects.all().values()
    return JsonResponse(list(books), safe=False)

def book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        return JsonResponse({
            "id": book.id,
            "title": book.title,
            "author": book.author.name if book.author else None,
        })
    except Book.DoesNotExist:
        return JsonResponse({"error": "Book not found"}, status=404)