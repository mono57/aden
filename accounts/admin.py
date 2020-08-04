from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

from accounts.forms import UserAdminCreationForm, UserAdminChangeForm
from accounts.models import Profile

User = get_user_model()


admin.site.site_title = "Administration ADEN"
admin.site.site_header = "ADEN | Panel d'administration"

class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('email', 'is_active','admin', 'is_member')
    list_filter = ('admin', 'is_staff', 'is_member')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': (
            'first_name',
            'last_name',
            'last_login',
        )}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'admin','is_member')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
    actions = ('confirm_member', 'suspend_member')

    def make_actions(self, queryset, action):
        for q in queryset:
            q.is_member = action
            q.save()

    def confirm_member(self, request, queryset):
        self.make_actions(queryset, True)

        self.message_user(request, 'Membre(s) confirmé(s)', messages.SUCCESS)

    confirm_member.short_description = 'Confirmer l\'adhésion' 

    def suspend_member(self, request, queryset):
        self.make_actions(queryset, False) 

        self.message_user(request, 'Suspension de(s) membre(s) réussie !') 

    suspend_member.short_description = 'Suspendre'
    
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

class ProfileModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileModelAdmin)