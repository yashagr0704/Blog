from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .forms import CreationForm, ChangeForm
from .models import Rec
class CusUserAdmin(UserAdmin):
    add_form = CreationForm
    form = ChangeForm
    model = Rec
    list_display = ['email', 'username', 'age', 'is_staff', ]
admin.site.register(Rec, CusUserAdmin)