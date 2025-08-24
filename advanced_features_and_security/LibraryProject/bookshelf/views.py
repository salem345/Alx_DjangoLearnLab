# Create your views here.
from .forms import ExampleForm
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import permission_required, login_required
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

# -------- View: عرض الكتب (requires can_view) --------
@permission_required('bookshelf.can_view', raise_exception=True)
def list_books(request):
    books = Book.objects.all()
    # عرض بسيط (ممكن تربطه بتيمبلت لاحقاً)
    lines = [f"- {b.title}" for b in books]
    return HttpResponse("Books:\n" + "\n".join(lines), content_type="text/plain")


# -------- View: إضافة كتاب (requires can_create) --------
@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        if not title:
            return HttpResponse("Title is required.", status=400)
        Book.objects.create(title=title)
        return redirect('books-list')

    # فورم بسيط
    return HttpResponse(
        "<form method='post'>{% csrf_token %}"
        "<input name='title' placeholder='Title' />"
        "<button type='submit'>Create</button></form>"
        .replace("{% csrf_token %}", f"<input type='hidden' name='csrfmiddlewaretoken' value='{request.META.get('CSRF_COOKIE','')}' />"),
        content_type="text/html"
    )


# -------- View: تعديل كتاب (requires can_edit) --------
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        if not title:
            return HttpResponse("Title is required.", status=400)
        book.title = title
        book.save()
        return redirect('books-list')

    return HttpResponse(
        f"<form method='post'>{{% csrf_token %}}"
        f"<input name='title' value='{book.title}' />"
        f"<button type='submit'>Save</button></form>"
        .replace("{% csrf_token %}", f"<input type='hidden' name='csrfmiddlewaretoken' value='{request.META.get('CSRF_COOKIE','')}' />"),
        content_type="text/html"
    )


# -------- View: حذف كتاب (requires can_delete) --------
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('books-list')

    return HttpResponse(
        f"<p>Delete '{book.title}'?</p>"
        f"<form method='post'>{{% csrf_token %}}"
        f"<button type='submit'>Confirm</button></form>"
        .replace("{% csrf_token %}", f"<input type='hidden' name='csrfmiddlewaretoken' value='{request.META.get('CSRF_COOKIE','')}' />"),
        content_type="text/html"
    )

from django.shortcuts import render, get_object_or_404
from .models import Book, Library
from .forms import SearchForm
from django.db import connection  # لو هتستخدم raw SQL (اختياري)

def book_list(request):
    # ORM آمن افتراضياً
    books = Book.objects.select_related("author").all()
    return render(request, "bookshelf/book_list.html", {"books": books})

def search_books(request):
    form = SearchForm(request.GET or None)
    results = []
    if form.is_valid():
        term = form.cleaned_data["q"]
        if term:
            # استخدام ORM لتفادي SQL Injection
            results = Book.objects.select_related("author").filter(title__icontains=term)
    return render(request, "bookshelf/book_list.html", {"books": results, "form": form})

def library_detail(request, pk):
    library = get_object_or_404(Library, pk=pk)
    books = library.books.select_related("author").all()
    return render(request, "bookshelf/library_detail.html", {"library": library, "books": books})

# مثال اختياري لــ raw SQL آمن بالـ parameters (لو لازم)
def raw_sql_example(request):
    form = SearchForm(request.GET or None)
    rows = []
    if form.is_valid() and form.cleaned_data["q"]:
        term = f"%{form.cleaned_data['q']}%"
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, title FROM bookshelf_book WHERE title LIKE %s", [term])
            rows = cursor.fetchall()
    return render(request, "bookshelf/book_list.html", {"raw_rows": rows, "form": form})