from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

ct = ContentType.objects.get_for_model(Book)

# احصل على الpermissions اللي أضفناها
can_view = Permission.objects.get(codename="can_view", content_type=ct)
can_create = Permission.objects.get(codename="can_create", content_type=ct)
can_edit = Permission.objects.get(codename="can_edit", content_type=ct)
can_delete = Permission.objects.get(codename="can_delete", content_type=ct)

# أنشئ الجروبس
editors, _ = Group.objects.get_or_create(name="Editors")
viewers, _ = Group.objects.get_or_create(name="Viewers")
admins, _  = Group.objects.get_or_create(name="Admins")

# وزّع الصلاحيات
viewers.permissions.set([can_view])

editors.permissions.set([can_view, can_create, can_edit])

admins.permissions.set([can_view, can_create, can_edit, can_delete])

print("Groups & permissions set.")

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
User = get_user_model()

u = User.objects.get(username="saelm")  # غيّر الاسم حسب مستخدمك
admins = Group.objects.get(name="salem")
admins.user_set.add(u)
print("Assigned user to salem.")