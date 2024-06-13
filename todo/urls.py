from django.urls import path
from rest_framework import routers
from . import views

urlpatterns = []

router = routers.SimpleRouter()
router.register('', views.TodoViewset)
urlpatterns += router.urls
