from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from .models import Topic
# Create your views here.


def bookmark_about(request):
    context = {}
    return render(request, 'bookmark/about.html', context)



# class IndexView(ListView):
#     model = Topic
#     template_name = 'bookmark/index.html'
#     context_object_name = 'topic_list'
#
#     def get_queryset(self):
#         return super(IndexView, self).get_queryset().filter(parent_id=None)



class IndexView(TemplateView):
    template_name = 'bookmark/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        topic_list = Topic.objects.all()

        context.update({
            'topic_list':topic_list
        })
        return context


