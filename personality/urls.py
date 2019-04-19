from django.urls import path

from . import views

app_name = 'personality'
urlpatterns = [
    path('', views.home, name='home'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('suggestions/', views.SuggestionCreateView.as_view(), name='suggestion'),
    # path('suggestions/list/', views.suggestions, name="suggestions_list"),
]