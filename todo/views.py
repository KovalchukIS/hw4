from rest_framework import viewsets, mixins

from .serializers import ListSerializer
from .serializers import UserSerializer
from .filters import ListFilterSet
from rest_framework.schemas.openapi import AutoSchema

from django.contrib.auth.models import User

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from django.views.generic import (
    CreateView,
    ListView,
    View,
    UpdateView,
    DeleteView,
    DetailView,
)
from todo.models import List


class UserList(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListViewSet(
    mixins.ListModelMixin,  # GET /articles
    mixins.CreateModelMixin,  # POST /articles
    mixins.RetrieveModelMixin,  # GET /articles/1
    mixins.DestroyModelMixin,  # DELETE /articles/1
    mixins.UpdateModelMixin,  # PUT /articles/1
    viewsets.GenericViewSet,
):

    queryset = List.objects.all().order_by("-id")
    serializer_class = ListSerializer
    filterset_class = ListFilterSet

    schema = AutoSchema(
        tags=["List"],
        component_name="List",
        operation_id_base="List",
    )

    # pagination_class = None
    # permission_classes = [IsAuthenticated]

    # def get_serializer_class(self):
    #     if self.action == "list":
    #         return NonModelSerializer
    #     return ArticleSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class ListListView(ListView):
    """Представление для отображения множества корзин.

    .._ https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-display/#listview
    """

    context_object_name = "lists_"
    queryset = List.objects.filter(is_done=False)
    # model = Cart
    template_name = "tasks_list.html"


class ListDetailView(DetailView):

    context_object_name = "list"
    queryset = List.objects
    template_name = "Task_detail.html"

    # context_object_name = 'list'
    # queryset = List.objects.filter(is_done=False)
    # # model = Cart
    # template_name = "tasks_list.html"


class ListCreateView(CreateView):
    """Представление для создания одной корзины."""

    model = List
    fields = ["name", "is_done"]
    template_name = "Task_create.html"
    success_url = "/tasks/active"


class ListUpdateView(UpdateView):
    model = List
    fields = ["name", "is_done"]
    template_name = "Task_update.html"
    # template_name_suffix = '_update_form'
    success_url = "/tasks/active"


class ListDeleteView(DeleteView):
    model = List
    success_url = "/tasks/active"
    template_name = "Task_del.html"
