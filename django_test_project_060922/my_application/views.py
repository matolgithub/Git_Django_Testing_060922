from django.http import HttpResponse
from django.shortcuts import render

from django_test_project_060922 import settings


def start_page(request, message="It is the main page!"):
    return HttpResponse(f"-----{message}-------")


def hello_page(request):
    user_name = request.GET.get('name')
    if user_name:
        response = f'Hello, dear, {user_name}!'
    else:
        response = 'Hi! What is your name?'

    return HttpResponse(response)


def main_page(request):
    context = {
        'email': settings.CONTACT_EMAIL,
        'address': settings.CONTACT_ADDRESS,
        'phone': settings.CONTACT_PHONE,
    }

    return render(request, 'index.html', context=context)


def list_page(request):
    context = {
        'listing': [1, 2, 3],
        '2': 'tgrr',
        '3': 'tgrg',
    }
    return render(request, template_name='list_page.html', context=context)


def writer_article(request):
    writers = ['Oleg', 'Ivan', 'Igor']
    dict_articles = {
        'Oleg': ['Gfjfj fkfkfkfk fkfkfkf.', 'Kfdhfh fhfhfh vnvnn.', 'Thvhvh nhn rhhr ewkwkk.', 'Hydydu lflf bbknknk.'],
        'Ivan': ['Ujjkfjfj fkfkfkfk fkfkfkf.', 'Lhfh fhfhfh vnvnn.', 'RESvhvh nhn rhhr ewkwkk.'],
        'Igor': ['Kfdhfh fhfhfh vnvnn.', 'MJKKvh nhn rhhr ewkwkk.'],
    }
    # for writer in writers:
    #     for author, articles in dict_articles.items():
    #         if writer == author:
    #             for article in articles:
    #                 context = {
    #                     writer: article
    #                 }
    context = dict_articles

    render(request, 'articles.html', context=context)
