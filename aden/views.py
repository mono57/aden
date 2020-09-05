from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.views.generic import TemplateView, FormView, ListView
from aden.forms import ContactForm
from aden.decorators import aden_member_required
from com.models import Event, News, Galery, Post, Faq, StrategicComity
from us.models import About, Footer, InstitutionalPresentation, Filiere


User = get_user_model()


class EnsaiTemplateView(TemplateView):
    template_name = 'ensai.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lc = self.request.LANGUAGE_CODE
        context['presentation'] = InstitutionalPresentation.objects.filter(
            language=lc).last()
        context['filiere'] = Filiere.objects.filter(language=lc).last()
        return context


class ContactFormView(SuccessMessageMixin, FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = 'Votre message a été bien envoyé, nous vous répondrons très bientôt !'

    def form_valid(self, form):
        data = form.cleaned_data
        message = '''
            
        '''
        subject = 'Mail de : {}'.format('name')
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
@method_decorator(aden_member_required, name='dispatch')
class NetworkTemplateView(TemplateView):
    template_name = 'network.html'


class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        first_galery = Galery.objects.first()
        context['news'] = News.objects.all()
        context['events'] = Event.objects.all()[:3]
        context['photos'] = first_galery.images.all()[
            :6] if first_galery else []
        context['posts_count'] = Post.objects.all().count()
        context['posts'] = Post.objects.all()[:3]
        context['members_count'] = User.objects.filter(is_member=True).count()
        context['photos_count'] = sum(
            [g.images.all().count() for g in Galery.objects.all()])
        context['faqs'] = Faq.objects.all()[:3]
        context['footer_text'] = Footer.objects.last()
        context['com_news'] = StrategicComity.objects.all()[:3]
        return context


class AboutTemplateView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.filter(
            language=self.request.LANGUAGE_CODE).first()
        return context


class FaqListView(ListView):
    template_name = 'faq.html'
    model = Faq
    context_object_name = 'faqs'


class LegalMentions(TemplateView):
    template_name = 'legal_mentions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Mentions légales'
        return context
