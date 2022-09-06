from django.http import HttpResponse
from django.shortcuts import render


def start_page(request, message="It is the main page!"):
    return HttpResponse(f"-----{message}-------")


def main_page(request):
    return render(request, 'index.html')


def list_page(request):
    listing = [1, 2, 3]
    # context = {
    #     '1': 'dgfd',
    #     '2': 'tgrr',
    #     '3': 'tgrg',
    # }
    return render(request, template_name='list_page.html')
