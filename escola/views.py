from escola.models import Estudante,Curso, Matricula
from escola.serializers import EstudanteSerializer,CursoSerializer, MatriculaSerializer, ListaMatriculasEstudanteSerializer, ListaMatriculasCursoSerializer, EstudanteSerializerV2
from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle
from rest_framework.permissions import DjangoModelPermissions
from escola.throttles import MatriculaThrottleAnon

class EstudanteViewSet(viewsets.ModelViewSet):
    queryset = Estudante.objects.all().order_by('id')
    serializer_class = EstudanteSerializer
    permission_classes = [DjangoModelPermissions]
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['nome']
    search_fields = ['nome','cpf']
    def get_serializer_class(self):
        if self.request.version == 'v2':
            return EstudanteSerializerV2
        return EstudanteSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    # permission_classes = [DjangoModelPermissions]
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    permission_classes = [DjangoModelPermissions]
    serializer_class = MatriculaSerializer
    throttle_classes = [UserRateThrottle, MatriculaThrottleAnon]
    http_method_names = ['get','post',] 

class ListaMatriculaEstudante(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions]
    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasEstudanteSerializer

class ListaMatriculaCurso(generics.ListAPIView):
    permission_classes = [DjangoModelPermissions]
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasCursoSerializer