from django.shortcuts import render, redirect,get_object_or_404
from django . contrib import messages

from .models import History

# Create your views here.

def HistoryList(request):
    historylist = History.objects.filter(user=request.user)
    context = {'historylist':historylist}
    return render(request, 'History/historylist.html',context)

def delete_history(request, pk):
    history = get_object_or_404(History, pk=pk, user=request.user)
    history.delete()
    messages.info(request, f"user History deleted successfully❗")
    
    return redirect('History:historylist')