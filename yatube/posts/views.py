from django.http import HttpResponse


def index(request):
    return HttpResponse('Ну типа крутой проект')
