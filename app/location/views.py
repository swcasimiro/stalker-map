from django.shortcuts import render, get_object_or_404
from .models import Hood, Location
from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import DetailView
from django.urls import reverse_lazy


def hood_list(request):
    search_query = request.GET.get('search', '')     # связываемся с инпутом и делаем get-запрос
    if search_query:
        model = Hood.objects.filter(Q(name__icontains=search_query))
    else:
        model = Hood.objects.select_related('location')

    paginator = Paginator(model, 7)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'location/base_location.html', {'page_obj': page_obj})


# def hood_list(request, location_slug):
#     model = get_object_or_404(Location, slug=location_slug)
#     model_1 = Hood.objects.all().select_related('location')
#     context = {
#         "model": model,
#         "model_1": model_1
#     }
#     return render(request, 'location/base_location.html', context)

class HoodView(DetailView):
    model = Hood
    template_name = 'location/info_location.html'
    context_object_name = 'hood'

    def get_success_url(self, **kwargs):  # Делаем get-request и получаем уникальный айди под каждый пост.
        return reverse_lazy('stats', kwargs={'pk': self.get_object().id})