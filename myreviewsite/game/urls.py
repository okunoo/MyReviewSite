from django.urls import path
from . import views


urlpatterns = [
    path('',views.index_view,name = "game_index"),
    path('<int:pk>/detail/',views.DetailGameView.as_view(),name ='detail-game'),
    path('create/',views.CreateGameView.as_view(),name = 'create-game'),
    path('<int:pk>/delete/',views.DeleteGameView.as_view(),name = 'delete-game'),
    path('<int:pk>/update/',views.UpdateGameView.as_view(),name = 'update-game'),
    path('<int:game_id>/review/',views.CreateReviewView.as_view(),name = 'game_review'),
    path('search/',views.post_search,name = 'game_search'),
]