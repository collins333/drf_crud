from rest_framework import routers
from .api import ProyectoViewset

router = routers.DefaultRouter()
router.register('api/proyectos', ProyectoViewset, 'proyectos')

urlpatterns = router.urls