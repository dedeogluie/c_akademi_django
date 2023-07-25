from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def home(request):
    context = {
        'title': 'cosmios',
        'number': 122,
        'list1' : [1,2, ["a","v"]],
        'dict1' : {
            'a': 1,
            'b': 2
        }
    }
    return render(request, 'student/index.html', context)

#  {{ variable }}
#  {% command %} ---> for loop if else 
#  | -----> filitreleme