from django.urls import path, include
from .views import home, student_list, student_create, stundent_detail, stundet_update, student_delete, stundet_patch, StudentListCreate, StudentDetail, StudentGAV, StudentDetailGAV, StudentCV, StudentDetailCV, StundentMVS, PathMVS
from rest_framework import routers


router = routers.DefaultRouter()
router.register("student", StundentMVS)
router.register("path", PathMVS)

urlpatterns = [
    path('', home),
    # path("student-list/", student_list),
    # path("stundet-create/", student_create),
    # path("student-detail/<int:pk>/", stundent_detail),
    # path("student-update/<int:pk>/", stundet_update),
    # path("delete/<int:pk>/", student_delete),
    # path("patch/<int:pk>/",  stundet_patch)
    # path("student/", StudentListCreate.as_view()),
    # path("student/<int:pk>", StudentDetail.as_view()),
    # path("student/", StudentGAV.as_view()),
    # path("student/<int:pk>", StudentDetailGAV.as_view()),
    # path("student/", StudentCV.as_view()),
    # path("student/<int:pk>", StudentDetailCV.as_view()),
    path("", include(router.urls))

]
