from django.urls import path
from .import views

app_name='History' 

urlpatterns = [
    path('history/',views.HistoryList, name='historylist'),
    path('delete_history/<int:pk>',views.delete_history, name='delete_history'),
]
