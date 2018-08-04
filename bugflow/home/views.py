from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    #return HttpResponse('<h1>Hello World</h1>')
    #print(request.path)
    nomes = ['Artur', 'Felipe', 'Raniery']
    return render(request, 'home/index.html', {'nomes':nomes})