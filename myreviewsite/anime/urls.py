from django.urls import path
from . import views


urlpatterns = [
    path('',views.index_view,name = "anime_index"),
    path('anime/',views.index_view,name = "list-anime"),
    path('anime/<int:pk>/detail/',views.DetailAnimeView.as_view(),name ='detail-anime'),
    path('anime/create/',views.CreateAnimeView.as_view(),name = 'create-anime'),
    path('anime/<int:pk>/delete/',views.DeleteAnimeView.as_view(),name = 'delete-anime'),
    path('anime/<int:pk>/update/',views.UpdateAnimeView.as_view(),name = 'update-anime'),
    path('anime/<int:anime_id>/review/',views.CreateReviewView.as_view(),name = 'review'),
    path('anime/search/',views.post_search,name = 'anime_search'),
]