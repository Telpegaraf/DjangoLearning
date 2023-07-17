from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackForm
from .models import Feedback
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import FormView, CreateView, UpdateView


# Create your views here.


class FeedbackViewUpdate(UpdateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = '/done'


class FeedbackView(CreateView):
    model = Feedback
    # fields = '__all__'
    form_class = FeedbackForm
    template_name = 'feedback/feedback.html'
    success_url = '/done'

    # def form_valid(self, form):
    #     form.save()
    #     return super(FeedbackView, self).form_valid(form)

   # def get(self, request):
   #     form = FeedbackForm()
   #     return render(request, 'feedback/feedback.html', context={'form': form})
#
   # def post(self, request):
   #     form = FeedbackForm(request.POST)
   #     if form.is_valid():
   #         print(form.cleaned_data)
   #         form.save()
   #         return HttpResponseRedirect('/done')
   #     return render(request, 'feedback/feedback.html', context={'form': form})

# class FeedbackView(View):
#     def get(self, request):
#         form = FeedbackForm()
#         return render(request, 'feedback/feedback.html', context={'form': form})
#
#     def post(self, request):
#         form = FeedbackForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return HttpResponseRedirect('/done')
#         return render(request, 'feedback/feedback.html', context={'form': form})


# class UpdateFeedback(View):
#   def post(self, request):


def update_feedback(request, id_feedback):
    feed = Feedback.objects.get(id=id_feedback)
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feed)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return HttpResponseRedirect('/done')
    else:
        form = FeedbackForm(instance=feed)
    form = FeedbackForm(instance=feed)
    return render(request, 'feedback/feedback.html', context={'form': form})


class DoneView(TemplateView):
    template_name = 'feedback/done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Ivanov I.I'
        context['date'] = '23.04.2022'
        return context


# class ListFeedbackView(TemplateView):
#     template_name = 'feedback/list_feedback.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         feedbacks = Feedback.objects.all()
#         context['feedbacks'] = feedbacks
#         return context
#

#class DetailFeedback(TemplateView):
#    template_name = 'feedback/detail_feedback.html'
#
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        id_feedback = kwargs['id_feedback']
#        feedback = Feedback.objects.get(id=id_feedback)
#        context['feedback'] = feedback
#        return context


class DetailFeedback(DetailView):
    template_name = 'feedback/detail_feedback.html'
    model = Feedback
    context_object_name = 'feed'



class ListFeedbackView(ListView):
    template_name = 'feedback/list_feedback.html'
    model = Feedback
    context_object_name = 'feedback'

    def get_queryset(self):
        queryset = super().get_queryset()
        filter_qs = queryset.filter(rating__gt=2)
        return filter_qs
