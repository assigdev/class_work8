from django.views.generic import TemplateView, ListView, DetailView
from .models import Animal


class HomeView(TemplateView):
    template_name = 'index.html'


class AnimalListView(ListView):
    template_name = 'animals.html'
    model = Animal
    paginate_by = 2


class AnimalDetailView(DetailView):
    model = Animal
    template_name = 'animal.html'
