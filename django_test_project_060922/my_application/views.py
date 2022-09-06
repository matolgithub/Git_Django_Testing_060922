from django.http import HttpResponse
from django.shortcuts import render


def start_page(request, message="It is the main page!"):
    return HttpResponse(f"-----{message}-------")
