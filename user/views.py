from django.shortcuts import render

def Home(request):
    template = 'base.html'
    context = {}
    return render(request, template_name=template, context=context)