from us.models import Status, ActionPlan, InternalRegulation, SocialNetwork


def aden(request):
    lc = request.LANGUAGE_CODE
    kwargs = {}
    kwargs['status'] = Status.objects.filter(language=lc).last()
    kwargs['action_plan'] = ActionPlan.objects.filter(language=lc).last()
    kwargs['internal_regulation'] = InternalRegulation.objects.filter(
        language=lc).last()
    kwargs['social_network'] = SocialNetwork.objects.last()
    return kwargs
