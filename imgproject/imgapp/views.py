from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from .models import Search
from django.db.models import Q
from django.views.generic import ListView, CreateView, DeleteView
# Create your views here.

class SearchList(ListView):
    model=Search
    template_name='list.html'

    def get_queryset(self):
        q_word=self.request.GET.get('query')

        if q_word:
            object_list=Search.objects.filter(
                Q(title__icontains=q_word))
        else:
            object_list=Search.objects.all()
        return object_list

class CreateList(CreateView):
    model=Search
    template_name='create.html'
    fields=('title', 'images')
    success_url=reverse_lazy('list')

class DeleteList(DeleteView):
    model=Search
    template_name='delete.html'
    success_url=reverse_lazy('list')

    def delete(self,request, *args, **kwargs):
        messages.success(self.request, '写真を削除しました。')
        return super().delete(request, *args, **kwargs)
