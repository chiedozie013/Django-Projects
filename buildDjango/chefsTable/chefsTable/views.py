from django.http import HttpResponse

# Error Handling

def handler404(request, exception):
    return HttpResponse('404 Page not found! ')