# rest framework imports
from rest_framework.viewsets import ModelViewSet

# my imports
from .models import Student, Path
from .serializers import StudentSerializer, PathSerializer
  

class StudentMVS(ModelViewSet):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    
    
class PathMVS(ModelViewSet):

    queryset = Path.objects.all()
    serializer_class = PathSerializer
