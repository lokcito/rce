from django.urls import path

from .views import index, kinesiologo, atencion, deportista


urlpatterns = [path('', index),
                path('kinesiologo/kine', kinesiologo),
                path('atencion/atencion', atencion),
                path('depor/deportista', deportista)
                                         
]



