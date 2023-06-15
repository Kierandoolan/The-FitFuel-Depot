from django.shortcuts import render

# Create your views here.

def error_403_view(request, exception):
    '''403 error view'''
    return render(request, '403.html', status=403)


def error_404_view(request, exception):
    '''404 error view'''
    return render(request, '404.html', status=404)


def error_500_view(request):
    """
    404 error view
    """
    return render(request, '500.html', status=500)


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

