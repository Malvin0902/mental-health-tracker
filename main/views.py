from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306123456',
        'name': 'Pak Bepe',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)