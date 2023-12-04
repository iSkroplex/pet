from django.shortcuts import render, redirect
from .models import Artikles
from .forms import ArtiklesForm
from django.views.generic import DetailView, UpdateView, DeleteView



def news_home(request):
    news = Artikles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

class NewsUpdateView(UpdateView):
    model = Artikles
    template_name = 'news/add_news.html'
    form_class = ArtiklesForm
    
class NewsDeleteView(DeleteView):
    success_url = '/news/'
    model = Artikles
    template_name = 'news/news-delete.html'


class NewsDetailView(DetailView):
     model = Artikles
     template_name = 'news/details_view.html'
     context_object_name = 'artikle'



def add_news(request):
    error = ''
    if request.method == 'POST':
        form = ArtiklesForm(request.POST)
        if form.is_valid():
            form.save(),
            return redirect('home')
        else:
            error = 'Форма составлена неверно'
    
    form = ArtiklesForm()
    
    data = {
        'form': form,
        'error': error
    }
    
    return render(request, 'news/add_news.html', data)
