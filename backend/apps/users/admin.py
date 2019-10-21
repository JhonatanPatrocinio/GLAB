from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _

from apps.users.models import UserApp


class UserAppAdmin(admin.ModelAdmin):
    list_display = ('type_user',)
    # search_fields = ('user.email', 'user.first_name', 'user.last_name')
    ordering = ('-id',)
    # list_filter = ('user.is_superuser', 'user.is_active', 'share_email', 'share_phone')
    # readonly_fields = ('user.date_joined',)


admin.site.register(UserApp, UserAppAdmin)

# @admin.register(UserApp)
# class UserAdmin(DjangoUserAdmin):
#     fieldsets = (
#         (None, {'fields': ('user.email', 'password')}),
#         (_('Personal info'), {
#             'fields': (
#                 'user.username',
#                 'user.first_name',
#                 'user.last_name',
#             )
#         }),
#         (_('Permissions'), {'fields': (
#             'user.is_active',
#             'user.is_staff',
#             'user.is_superuser',
#             'share_email',
#             'share_phone',
#             'user.groups',
#             'user.user_permissions',
#         )}),
#         (_('Important dates'), {'fields': ('user.last_login', 'user.date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('user.password1', 'user.password2'),
#         }),
#     )
#     list_display = ('user.email', 'user.first_name', 'user.last_name')
#     search_fields = ('user.email', 'user.first_name', 'user.last_name')
#     ordering = ('-id',)
#     list_filter = ('user.is_superuser', 'user.is_active', 'share_email', 'share_phone')
#     readonly_fields = ('user.date_joined',)
