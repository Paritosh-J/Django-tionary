from django.shortcuts import render
from PyDictionary import PyDictionary

# Create your views here.
def index(request):
    return render(request, 'index.html')

def word(request):
    search = request.GET.get('search')
    dic = PyDictionary()
    means = dic.meaning(search)
    context = { 'meaning' : means }
    return render(request, 'word.html', context)