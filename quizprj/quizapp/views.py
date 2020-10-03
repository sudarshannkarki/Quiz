from django.shortcuts import render

# Create your views here.

def quiz_view(request):
    context = {}
    return render(request, 'quizapp/home.html', context)