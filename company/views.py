from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .forms import ContactForm
# Create your views here.


def faq(request):
    """ A view to return the frequently ask question page """

    return render(request, 'company/faq.html')


def privatepolicy(request):
    """ A view to return the private policy """

    return render(request, 'company/private-policy.html')


def about_us(request):
    """A view to return info page"""
    return render(request, 'company/about-us.html')


def contactus(request, *args, **kwargs):
    """
    Displays Contact Us page form.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name'],
            email = form.cleaned_data['email'],
            subject = form.cleaned_data['subject'],
            message = form.cleaned_data['message'],
            form.save()

            # send mail combining field forms
            send_mail({subject}, f'{name}, {email}, {message}',
                      settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER],
                      fail_silently=False)
            messages.success(
                request, 'Thank you for contacting us \
                - we will reply as soon as possible!')

            # redirect to home page
            return redirect(reverse('home'))
        else:
            messages.error(
                request, 'Something went wrong with your submission.\
                Please try again.'
            )
    else:
        form = ContactForm()

    return render(request, 'company/contact-us.html', {'form': form})