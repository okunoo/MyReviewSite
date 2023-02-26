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
from .models import Anime,Review
from django.core.paginator import Paginator
from .consts import ITEM_PER_PAGE

def index_view(request):
    object_list = Anime.objects.order_by('-id')
    ranking_list = Anime.objects.annotate(avg_score=Avg('review__score')).order_by('-avg_score')
    paginator = Paginator(ranking_list,ITEM_PER_PAGE)
    page_number = request.GET.get('page',1)
    page_obj = paginator.page(page_number)
    return render(request,'anime/index.html',{'object_list':object_list,'ranking_list':ranking_list,'page_obj':page_obj})


# Create your views here.
class AllAnimeView(ListView):
    template_name = 'anime/index.html'
    model = Anime

class DetailAnimeView(DetailView):
    template_name = 'anime/anime_detail.html'
    model = Anime

class CreateAnimeView(LoginRequiredMixin,CreateView):
    template_name = 'anime/anime_create.html'
    model = Anime
    fields = {'name','overview','thumbnail',
              'main_category','sub_category','score','user','comment'}
    success_url = reverse_lazy('anime_index')

class DeleteAnimeView(LoginRequiredMixin,DeleteView):
    template_name = 'anime/anime_delete.html'
    model = Anime
    success_url = reverse_lazy('anime_index')

class UpdateAnimeView(LoginRequiredMixin,UpdateView):
    template_name = 'anime/anime-update.html'
    model = Anime
    fields = {'name','overview','thumbnail',
              'main_category','sub_category','score','comment'}
    success_url = reverse_lazy('anime_index')
     
    def get_success_url(self):
        return reverse('detail-anime',kwargs={'pk':self.object.id})


class CreateReviewView(LoginRequiredMixin,CreateView):
    model = Review
    fields = ('anime','comment','score')
    template_name = 'anime/review_form.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['anime'] = Anime.objects.get(pk = self.kwargs['anime_id'])
        return context
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('detail-anime',kwargs={'pk':self.object.anime.id})