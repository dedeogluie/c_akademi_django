from django.urls import path, include

from rest_framework import routers

from .views import todo_list_create, todo_detail, Todos, TodoDetail, TodoMVS

router = routers.DefaultRouter()
router.register("todo", TodoMVS)  # todo/ todo/<int:id> todo/method


urlpatterns = [
    #! FBV
    # path("list-create", todo_list_create),
    # path("detail/<int:id>", todo_detail),

    #! CBV
    #? Concreate View
    # path("list-create/", Todos.as_view()),
    # path("detail/<int:id>", TodoDetail.as_view()),

    #? Model View Set
    path("", include(router.urls)),
]
# urlpatterns += router.urls