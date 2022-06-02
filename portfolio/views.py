from django.shortcuts import render


def hello(request):
    return render(request, 'portfolio/pages/hello.html')


def about_me(request):
    return render(request, 'portfolio/pages/about_me.html')


def skills(request):
    return render(request, 'portfolio/pages/skills.html')


def experience(request):
    return render(request, 'portfolio/pages/experience.html')


def contact(request):
    return render(request, 'portfolio/pages/contact.html')
