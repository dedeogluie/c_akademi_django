from django.urls import path
from .views import home, student_list, student_create, stundent_detail, stundet_update, student_delete, stundet_patch

urlpatterns = [
    path('', home),
    path("student-list/", student_list),
    path("stundet-create/", student_create),
    path("student-detail/<int:pk>/", stundent_detail),
    path("student-update/<int:pk>/", stundet_update),
    path("delete/<int:pk>/", student_delete),
    path("patch/<int:pk>/",  stundet_patch)

]
