from django.shortcuts import render


def hom(request):
    name = 'Bob'

    return render(request, 'home.html')
