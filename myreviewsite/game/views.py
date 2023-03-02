from django.shortcuts import render
from django.views.generic import (ListView,
        DetailView,
        CreateView,
        DeleteView,
        UpdateView,
)
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg
from django.db.models import Q
from django.core.paginator import Paginator

from .consts import ITEM_PER_PAGE

from .models import Game,Game_Review

from .forms import SearchForm


def index_view(request):
    object_list = Game.objects.order_by('-id')
    ranking_list = Game.objects.annotate(avg_score=Avg('game_review__score')).order_by('-avg_score')
    paginator = Paginator(ranking_list,ITEM_PER_PAGE)
    page_number = request.GET.get('page',1)
    page_obj = paginator.page(page_number)
    return render(request,'game/index.html',{'object_list':object_list,'ranking_list':ranking_list,'page_obj':page_obj})


def post_search(request):
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Game.objects.filter(
                Q(name__icontains=query) | Q(main_category__icontains=query))

    return render(request, 'game/game_search.html', {'form': form, 'query': query, 'results': results})

# Create your views here.
class AllGameView(ListView):
    template_name = 'game/index.html'
    model = Game

class DetailGameView(DetailView):
    template_name = 'game/game_detail.html'
    model = Game

class CreateGameView(LoginRequiredMixin,CreateView):
    template_name = 'game/game_create.html'
    model = Game
    fields = {'name','overview','thumbnail',
              'main_category','score','user','comment'}
    success_url = reverse_lazy('game_index')

class DeleteGameView(LoginRequiredMixin,DeleteView):
    template_name = 'game/game_delete.html'
    model = Game
    success_url = reverse_lazy('game_index')

class UpdateGameView(LoginRequiredMixin,UpdateView):
    template_name = 'game/game-update.html'
    model = Game
    fields = {'name','overview','thumbnail',
              'main_category','score','comment'}
    success_url = reverse_lazy('game_index')
     
    def get_success_url(self):
        return reverse('detail-game',kwargs={'pk':self.object.id})


class CreateReviewView(LoginRequiredMixin,CreateView):
    model = Game_Review
    fields = ('game','comment','score')
    template_name = 'game/review_form.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['game'] = Game.objects.get(pk = self.kwargs['game_id'])
        return context
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('detail-game',kwargs={'pk':self.object.game.id})
