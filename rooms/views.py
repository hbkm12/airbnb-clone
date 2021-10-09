from django.views.generic import ListView, DetailView
# from django.shortcuts import render, redirect
# from django.urls import reverse
# from django.utils import timezone
# from django.http import Http404
from . import models

# Create your views here.


class HomeView(ListView):
    """HomeView Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"

class RoomDetail(DetailView):
    """ RoomDetail Definition """
    model = models.Room


# 12.3±îÁö
# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, "rooms/detail.html", {"room": room})
#     except models.Room.DoesNotExist:
#         raise Http404()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     now = timezone.now()
    #     context["now"] = now
    #     return context


# # paginator way
# def all_rooms(request):
#     page = request.GET.get("page", 1)
#     room_list = models.Room.objects.all()
#     paginator = Paginator(room_list, 10, orphans=5)
#     # page = int(page or 1)
#     # page_size = 10
#     # limit = page_size * page
#     # offset = limit - page_size
#     # all_rooms = models.Room.objects.all()[offset:limit]
#     # page_count = ceil(models.Room.objects.count() / page_size)
#     try:
#         rooms = paginator.page(int(page))
#         return render(
#             request,
#             "rooms/home.html",
#             {
#                 "page": rooms,
#                 # "rooms": all_rooms,
#                 # "page": page,
#                 # "page_count": page_count,
#                 # "page_range": range(1, page_count),
#             },
#         )

#     except EmptyPage:
#         return redirect("/")
