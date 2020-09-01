from django.db import models
from django.db.models import Q


class OfferManager(models.Manager):
    def get_offers_by(self, query):
        qs = self.get_queryset()
        if query:
            return qs.filter(
                Q(entreprise__icontains=query) |
                Q(label__icontains=query) |
                Q(description__icontains=query) |
                Q(profil__icontains=query)
            )
        return qs


class ResumeManager(models.Manager):
    def get_resumes_by(self,query):
        qs = self.get_queryset()
        if query:
            return qs.filter(
                Q(full_name__icontains=query) |
                Q(filiere__icontains=query) |
                Q(promotion__icontains=query)
            )
        return qs