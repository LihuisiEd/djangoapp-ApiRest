from django.urls import path
 
from . import views
 
app_name = 'tienda'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('producto',views.SeriesView.as_view(),name='productos'),
    path('producto/<int:producto_id>',views.SerieDetailView.as_view())
]


