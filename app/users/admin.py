from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from .models import User, Teacher, Student


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {
            'fields': ('full_name', )
        }),
        (_('Permissions'), {
            'fields': (
                'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'
            )
        }),
        (_('Important dates'), {
            'fields': ('last_login', 'date_joined')
        })
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('password1', 'password2'),
        }),
    )
    list_display = ('email', 'full_name')
    search_fields = ('email', 'full_name')
    ordering = ('-id', )
    list_filter = ('is_superuser', 'is_active')
    readonly_fields = ('date_joined',)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'registry', 'academic_center')
    search_fields = ('registry', 'user')
    ordering = ('-id', )
    list_filter = ('academic_center', )


class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'registry', 'course')
    search_fields = ('registry', 'user')
    ordering = ('-id', )
    list_filter = ('course', )


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
