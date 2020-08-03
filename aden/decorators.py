from django.urls import reverse
from django.shortcuts import redirect


def aden_member_required(func):
    def wrap(request, *args, **kwargs):
        user = request.user
        if not user.is_member:
            return redirect('not_allowed')
        return func(request, *args, **kwargs)

    # wrap.__doc__ = func.__doc__
    # wrap.__name__ = func.__name__

    return wrap