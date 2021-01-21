"""
Regular django views are used to decide what data will be sent to the templates. 

Traditional django views are used to customize what 'regular' data is sent to the templates. Whereas, Django REST Framework views are used to customize what 'serialized data' is sent to the templates. 

Django REST Framework, like traditional django ships with generic views. So, I will be using these generic views. 

generics provide commonly needed behavior. In most cases I will only need to subclass a generic view rather than create my own. 
"""

from rest_framework import generics
from .models import Drapi
from .serializers import TodoSerializer


# This view will display all the entries in the model
class ListTodo(generics.ListAPIView):
    # Override parent attributes with my own queryset and subclassed serializer
    queryset = Drapi.objects.all()
    serializer_class = TodoSerializer


# This view will diplay a single entry from the model e.g. api/1/
class DetailTodo(generics.RetrieveAPIView):
    queryset = Drapi.objects.all()
    serializer_class = TodoSerializer
