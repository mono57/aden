from django.urls import path
from us.views import *

app_name = 'aden'

urlpatterns = [
    path('actions/plans/', ActionPlanListView.as_view(), name='actions'),
    path('general/assembly/', GeneralAssemblyListView.as_view(), name='ga'),
    path('coords/', CoordTemplateView.as_view(), name='coords'),
    path(
        'strategic/comity/',
        StrategicComityTempateView.as_view(),
        name='comity'),
    # path('contact/', ContactCreateView.as_view(), name='contact'),
]
