from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from accounts.admin import send_html_email
import requests
import os
import json
import datetime

url = os.getenv('USER_DATA_URL',
                'https://ensai-alumni-media-storages.s3.amazonaws.com/media/userdata.json')

User = get_user_model()


class Command(BaseCommand):
    help = 'load user .json data'

    error = None

    def print(self, msg):
        self.stdout.write(msg)

    def print_error(self, error):
        self.print('Error : {}'.format(error))

    def print_success(self, success):
        self.print('Successfuly: {}'.format(success))

    def handle(self, *args, **kwargs):
        if url:
            self.print("load users from {}".format(url))
            r = requests.get(url, allow_redirects=True)
            data = json.loads(r.text)
            for obj in data:
                try:
                    user = User.objects.create_user(
                        email=obj.get('email'),
                        password='ensaialumni'
                    )
                    user.first_name = obj.get('first_name', '')
                    user.last_name = obj.get('last_name', '')
                    user.is_member = True   
                    user.save()
                    profile = user.profile
                    # self.print(str('User :'.format(str(user))))
                    # self.print(str('Profile :'.format(str(profile))))

                    profile.birthday = datetime.datetime.strptime(
                        obj.get('birthday', '01/01/2000'), '%d/%m/%Y').date()
                    profile.birth_location = obj.get('birth_location', '')
                    profile.filiere = obj.get('filiere', '')
                    profile.promo = obj.get('promo', '')
                    profile.gender = 'male' if obj.get(
                        'gender', '') == 'Masculin' else 'female'
                    profile.degree = obj.get('degree', '')
                    profile.in_ensai_year = str(datetime.datetime.strptime(
                        obj.get('in_ensai_year', '01/01/2000'), '%d/%m/%Y').date()).split('-')[0]
                    profile.out_ensai_year = str(datetime.datetime.strptime(
                        obj.get('out_ensai_year', '01/01/2000'), '%d/%m/%Y').date()).split('-')[0]
                    profile.situation = obj.get('situation', '')
                    profile.entreprise = obj.get('entreprise', '')
                    profile.poste = obj.get('poste', '')
                    profile.phone = obj.get('phone', '')
                    profile.waiting = obj.get('waiting', '')
                    profile.contribution = obj.get('contribution', '')
                    profile.region = obj.get('region', '')
                    profile.save()
                    context = {
                        'full_name': user.get_full_name(),
                        'email': user.email,
                        'password': 'ensaialumni'
                    }
                    subject = 'Confirmation'
                    template_path = 'account/email_member.html'
                    send_html_email([user.email], subject, template_path, context)
                    self.print_success('User {} created, mail sended !'.format(user.email))

                except:
                    self.print_error(
                        'Can create user: {}'.format(obj.get('email')))

            self.print("User loaded successfully !")

        else:
            self.print_error('URL not provide !')
