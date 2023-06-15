from django.shortcuts import render

# Create your views here.


def faq(request):
    """ A view to return the frequently ask question page """

    return render(request, 'company/faq.html')


def privatepolicy(request):
    """ A view to return the private policy """

    return render(request, 'company/private-policy.html')