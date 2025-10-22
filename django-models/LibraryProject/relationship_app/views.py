from django.shortcuts import render
from .models import Book, Library
from django.views.generic import ListView, CreateView, FormView, TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import user_passes_test, login_required, permission_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin

def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# helper to safely check a UserProfile.role value
def has_role(role):
    def check(user):
        if not user.is_authenticated:
            return False
        profile = getattr(user, 'userprofile', None)
        return bool(profile and getattr(profile, 'role', None) == role)
    return check

is_admin = has_role('admin')
is_librarian = has_role('librarian')
is_member = has_role('member')

# Require login to view the libraries list
@method_decorator(login_required(login_url=reverse_lazy('relationship_app:login')), name='dispatch')
class LibraryListView(ListView):
    model = Library
    template_name = 'relationship_app/library_list.html'
    context_object_name = 'library'


class registerationView(CreateView):
    template_name = 'relationship_app/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('relationship_app:login')


class loginView(FormView):
    template_name = 'relationship_app/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('relationship_app:home')

    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        return super().form_valid(form)


class logoutView(TemplateView):
    template_name = 'relationship_app/logout.html'


# admin: require both the custom permission and role check
@method_decorator(permission_required('relationship_app.can_view_admin', login_url=reverse_lazy('relationship_app:login')), name='dispatch')
@method_decorator(user_passes_test(is_admin, login_url=reverse_lazy('relationship_app:login')), name='dispatch')
class admin_view(ListView):
    model = User
    template_name = 'relationship_app/admin_view.html'
    context_object_name = 'users'


# librarian: require permission + role
@method_decorator(permission_required('relationship_app.can_view_librarian', login_url=reverse_lazy('relationship_app:login')), name='dispatch')
@method_decorator(user_passes_test(is_librarian, login_url=reverse_lazy('relationship_app:login')), name='dispatch')
class librarian_view(ListView):
    model = Library
    template_name = 'relationship_app/librarian_view.html'
    context_object_name = 'libraries'


# member: require permission + role
@method_decorator(permission_required('relationship_app.can_view_member', login_url=reverse_lazy('relationship_app:login')), name='dispatch')
@method_decorator(user_passes_test(is_member, login_url=reverse_lazy('relationship_app:login')), name='dispatch')
class member_view(ListView):
    model = Book
    template_name = 'relationship_app/member_view.html'
    context_object_name = 'books'

# Book Create View - Only librarians can create books
@method_decorator(user_passes_test(is_librarian), name='dispatch')
class BookCreateView(PermissionRequiredMixin, CreateView):
    model = Book
    template_name = 'relationship_app/book_form.html'
    fields = ['title', 'author', 'publication_year', 'library']
    success_url = reverse_lazy('relationship_app:book_list')
    permission_required = 'relationship_app.add_book'

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super().form_valid(form)

# Book Update View - Only librarians can edit books
@method_decorator(user_passes_test(is_librarian), name='dispatch')
class BookUpdateView(PermissionRequiredMixin, UpdateView):
    model = Book
    template_name = 'relationship_app/book_form.html'
    fields = ['title', 'author', 'publication_year', 'library']
    success_url = reverse_lazy('relationship_app:book_list')
    permission_required = 'relationship_app.change_book'

# Book Delete View - Only librarians can delete books
@method_decorator(user_passes_test(is_librarian), name='dispatch')
class BookDeleteView(PermissionRequiredMixin, DeleteView):
    model = Book
    template_name = 'relationship_app/book_confirm_delete.html'
    success_url = reverse_lazy('relationship_app:book_list')
    permission_required = 'relationship_app.delete_book'

