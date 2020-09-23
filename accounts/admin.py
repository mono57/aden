from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from accounts.forms import UserAdminCreationForm, UserAdminChangeForm
from accounts.models import Profile

User = get_user_model()


admin.site.site_title = _("Administration ADEN")
admin.site.site_header = _("ADEN | Panel d'administration")


def send_html_email(recipients, subject, template_name, context):
    template_html = render_to_string(template_name, context)
    msg = EmailMessage(subject=subject, body=template_html,
                       from_email=settings.DEFAULT_FROM_EMAIL, bcc=recipients)

    msg.content_subtype = 'html'

    return msg.send()

class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('email', 'is_active', 'admin', 'is_member')
    list_filter = ('admin', 'is_staff', 'is_member')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': (
            'first_name',
            'last_name',
            'last_login',
        )}),
        ('Permissions', {'fields': ('is_active',
                                    'is_staff', 'admin', 'is_member')}),
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
            
        self.message_user(request, _(
            'Membre(s) confirmé(s)'), messages.SUCCESS)

    confirm_member.short_description = _('Confirmer l\'adhésion')

    def suspend_member(self, request, queryset):
        self.make_actions(queryset, False)

        self.message_user(request, _('Suspension de(s) membre(s) réussie !'))

    suspend_member.short_description = _('Suspendre')


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)


class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'portrait_visible')
    actions = ('portrait_visible', 'portrait_invisible')
    search_fields = ('user__email', 'user__first_name',
                     'user__last_name', 'promo', 'filiere')

    def portrait_invisible(self, request, queryset):
        queryset.update(portrait_visible=False)
        self.message_user(request, 'Le(s) portrait(s) rendu(s) invisible(s)')

    portrait_invisible.short_description = 'Désactiver la visibilité du portrait'

    def portrait_visible(self, request, queryset):
        queryset.update(portrait_visible=True)
        self.message_user(request, 'Le(s) portrait(s) rendu(s) visible(s)')

    portrait_visible.short_description = 'Rendre le portrait visible'


admin.site.register(Profile, ProfileModelAdmin)
