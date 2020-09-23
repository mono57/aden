from accounts.admin import send_html_email
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.urls import reverse
from django.conf import settings
from django.template.loader import get_template


User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        users = User.objects.filter(is_member=False)
        for user in users:
            context = {
                'full_name': user.get_full_name(),
                'email': user.email,
                'password': 'ensaialumni',
                'login_url': reverse('account_login')
            }

            subject = 'Confirmation'
            template_path = 'account/email_member.html'

            html_email = get_template(template_path).render(context=context) 

            # send_html_email([user.email], subject, template_path, context)

            send_mail(
                subject=subject,
                message='', 
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list = [user.email,],
                fail_silently = True,
                html_message = html_email
            )

            self.stdout.write("Mail sended to : {}".format(user.email))