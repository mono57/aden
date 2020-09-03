from us.models import Status, ActionPlan, InternalRegulation, SocialNetwork, Footer, AdhesionCondition


def aden(request):
    lc = request.LANGUAGE_CODE
    kwargs = {}
    kwargs['status'] = Status.objects.filter(language=lc).last()
    kwargs['action_plan'] = ActionPlan.objects.filter(language=lc).last()
    kwargs['internal_regulation'] = InternalRegulation.objects.filter(
        language=lc).last()
    kwargs['social_networks'] = SocialNetwork.objects.all()
    kwargs['footer_text'] = Footer.objects.last()
    kwargs['adhesion'] = AdhesionCondition.objects.filter(language=lc).last()
    return kwargs
