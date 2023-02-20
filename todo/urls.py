from rest_framework.urlpatterns import format_suffix_patterns


from rest_framework.routers import DefaultRouter
from todo.views import UserList, UserDetail, ListListView, ListViewSet

# router = DefaultRouter(trailing_slash=False)
router = DefaultRouter()

app_name = "todoapp"


router.register(
    prefix="List",
    viewset=ListViewSet,
    basename="List",
)
router.register("users", UserList)
router.register("users/", UserDetail)
router.register("api/tasks", ListViewSet)


urlpatterns = router.urls
