# Create your views here.

from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import permission_required, login_required
from .models import Book

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