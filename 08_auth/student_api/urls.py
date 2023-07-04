from django.urls import path, include
from rest_framework import routers
from .views import (
    #! class views
    StudentMVS,
    PathMVS
)

router = routers.DefaultRouter()
router.register("student", StudentMVS)
router.register("path", PathMVS)


urlpatterns = [
    #! Model View Set
    path("", include(router.urls))
]

# urlpatterns += router.urls