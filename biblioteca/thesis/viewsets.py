from rest_framework import viewsets
from rest_framework import filters


from .models      import Thesis
from .serializers import ThesisSerializer


class ThesisViewSet(viewsets.ReadOnlyModelViewSet):
    queryset            = Thesis.objects.all()
    serializer_class    = ThesisSerializer
    filter_backends     = (filters.DjangoFilterBackend, filters.SearchFilter, )
    filter_fields       = ('id', 'career__name', 'author__name', 'line__name', 'year', )
    search_fields       = ('title', 'career__name', 'line__name', )
