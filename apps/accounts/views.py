from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import EditUserForm
from .models import User
from .tasks import send_verification_email


@login_required
def personal_information(request):
    user = request.user
    context = {
        'user': user,
        'menu': 'personal_information',
    }
    return render(request, 'accounts/personal_information.html', context)


@login_required
def edit_personal_information(request):
    user = request.user
    if request.method == 'POST':
        form = EditUserForm(instance=user, data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.email_verified = False
            user.save()

            send_verification_email.delay(user_id=user.id)

            messages.success(request,
                             'Please confirm your new email address')
            return redirect(reverse('accounts:personal_information'))
    else:
        form = EditUserForm(instance=user)
    context = {
        'form': form,
        'menu': 'personal_information',
    }
    return render(request, 'accounts/edit_personal_information.html', context)


def login_view(request, template_name='accounts/login.html'):
    from .forms import UserAuthForm

    redirect_to = request.POST.get('next', request.GET.get('next', ''))
    do_redirect = False

    if request.user.is_authenticated:
        if redirect_to == request.path:
            raise ValueError('Redirection loop for authenticated user detected.')
        return redirect(reverse('index'))
    elif request.method == 'POST':
        form = UserAuthForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse('index'))
    else:
        form = UserAuthForm(request)

    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


def register(request, template_name='accounts/register.html'):
    from .forms import UserRegistrationForm
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            user.is_active = False
            user.save()

            send_verification_email.delay(user_id=user.id)

            messages.success(request,
                             'Please confirm your email address '
                             'to complete the registration.')
            return redirect(reverse('index'))
    else:
        form = UserRegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)


def logout_view(request):
    _next = request.GET.get('next')
    logout(request)
    return redirect(_next if _next else settings.LOGOUT_REDIRECT_URL)


def activate_user_account(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None:
        user.is_active = True
        user.email_verified = True
        user.save()
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        messages.success(request, 'Your email has been confirmed successfully.')
        return redirect(reverse('index'))
    else:
        messages.error(request, 'Activation link is invalid!')
        return redirect(reverse('index'))
