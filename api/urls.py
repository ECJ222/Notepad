from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import NoteCRUD,UserAuth,ImageCRUD

router= routers.DefaultRouter()
router.register('note',NoteCRUD)
router.register('user',UserAuth)
router.register('image',ImageCRUD)

urlpatterns=[
    path('',include(router.urls))
]