from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from accounts.models import UserVerification

# Register your models here.
User = get_user_model()

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)


class UserAdmin(BaseUserAdmin):
    # Custom forms to add and change user instances in Admin site.
    # add_form = UserAdminCreationForm
    # form = UserAdminChangeForm

    # The fields to be used in displaying the User model.
    list_display = (
        '__str__', 'full_name',
        'email', 'mobile',
        'referral_code',
        'is_admin', 'is_staff',
        'is_active',
        'created_at', 'updated_at'
    )
    list_filter = ('is_admin', 'is_staff', 'is_active')
    list_editable = ('is_active', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'referral_code', )}),
        ('Contact info', {'fields': ('email', 'mobile',)}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_active',)}),
    )
    # ('Address', {'fields': ('address', 'city', 'state', 'country')}),

    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'mobile', 'password1', 'password2')}
         ),
    )
    search_fields = ('username', 'first_name', 'last_name', 'email', 'mobile',)
    ordering = ('username',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)




class UserVerificationAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'user', 'nin', 'status']
    list_editable = ['status',]

    class Meta:
        model = UserVerification


admin.site.register(UserVerification, UserVerificationAdmin)