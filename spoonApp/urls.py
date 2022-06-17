"""spoonApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from polls import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/rest/', include(router.urls)),
    path('admin/', admin.site.urls),
    #path('', views.probasParaIngredientes, name='index'),
    #path('', views.databaseBaserow, name='index'),
    #path('', views.probasParaIngredientes, name='as'), 
    path('añadir/base', views.getIngredientePlatoBaseLink, name='as'),
    path('añadir/personalized', views.getIngredientePlatoPersonalizadoLink, name='as'),
    path('home', views.home, name='home'),
    path('home/<str:busca>', views.home, name='home'),
    path('all', views.homeAll, name='home'),
    path('basedish/<str:ident>', views.datosPlato, name='basedish'),
    path('alldishes/base', views.probaIngredientesCantidad, name='alldishes'),
    path('alldishes/personalized', views.probaIngredientesCantidad, name='allpersonalized'),
    path('dish/<str:plato>/personalize', views.probaIngredientesCantidad, name='personalize'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
