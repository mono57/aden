from accounts.admin import send_html_email
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        users = User.objects.filter(is_member=False)
        for user in users:
            context = {
                'full_name': user.get_full_name(),
                'email': user.email,
                'password': 'ensaialumni'
            }
            
            subject = 'Confirmation'
            template_path = 'account/email_member.html'

            send_html_email([user.email], subject, template_path, context)

            self.stdout.write("Mail sended to : {}".format(user.email))