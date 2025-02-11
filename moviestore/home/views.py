from django.shortcuts import render


def index(request):
    template_data = {}
    template_data['title'] = 'M Store: Buy you DVDs with us!'

    return render(request, 'home/index.html', {'template_data': template_data})


def about(request):
    template_data = {}
    template_data['title'] = 'About us'

    return render(request, 'home/about.html', {'template_data': template_data})