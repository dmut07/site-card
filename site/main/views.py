from django.shortcuts import render

# Create your views here.

def index_page(request):
    context = {}
    return render(request, 'main/index.html', context)